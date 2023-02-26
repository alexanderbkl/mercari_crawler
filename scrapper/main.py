import csv
from .notification import notify
from .mercari_driver import MercariDriver, get_scrapper_driver
from .input import Input



def main():
    
    
    # create an input (1 or 2) to select if the program needs manual input or text file input

    while True:
        try:
            input_type = int(
                input("[1]: Introducción manual de datos \n[2]: Introducción desde input.csv:\n"))
            if input_type == 1:
                input_class = Input()
                input_class.set_MERCARI_URL()
                input_class.set_QUANTITY()
                input_class.set_PRODUCT_CATEGORY()
                input_class.set_INTEREST_RATE()
                input_class.set_TRANS_LANG()
                
                MERCARI_URL = input_class.get_MERCARI_URL()
                QUANTITY = input_class.get_QUANTITY()
                PRODUCT_CATEGORY = input_class.get_PRODUCT_CATEGORY()
                INTEREST_RATE = input_class.get_INTEREST_RATE()
                TRANS_LANG = input_class.get_TRANS_LANG()
                
                driver = get_scrapper_driver()
                m_scrapper = MercariDriver(driver)
                m_scrapper.move_page(MERCARI_URL)


                latest_item_url_list = m_scrapper.get_items_url(quantity=QUANTITY)

                for item_url in latest_item_url_list:

                    m_scrapper.move_page(item_url)
                    item_name, item_price, item_description = m_scrapper.get_name_and_price()
                    if item_name is None or item_price is None or item_description is None:
                        continue
                    
                    notify(item_url, item_name, item_price, item_description, TRANS_LANG, INTEREST_RATE, PRODUCT_CATEGORY)

                driver.close()
                driver.quit()

                break
            elif input_type == 2:
                
                #read input.csv file, ignore first line.
                #enumerate the lines and assign the values to the variables
                driver = get_scrapper_driver()

                with open('input.csv') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    #create a for loop for row in csv_reader
           
                    
                    for row in csv_reader:
                        
                        
                        if line_count == 0:
                            #print(f'Column names are {", ".join(row)}')
                            line_count += 1
                        else:
                            print(f'\tPalabra clave: {row[0]} Nº productos: {row[1]} Categoría: {row[2]} Tasa de interés: {row[3]} Idioma: {row[4]}.')
                            

                            
                            MERCARI_URL = "https://jp.mercari.com/search?keyword=" + row[0]
                            QUANTITY = int(row[1])
                            PRODUCT_CATEGORY = row[2]
                            INTEREST_RATE = float(row[3])
                            TRANS_LANG = row[4]
                            
                            m_scrapper = MercariDriver(driver)

                            m_scrapper.move_page(MERCARI_URL)


                            latest_item_url_list = m_scrapper.get_items_url(quantity=QUANTITY)

                            for item_url in latest_item_url_list:
                            
                                m_scrapper.move_page(item_url)
                                item_name, item_price, item_description = m_scrapper.get_name_and_price()

                                if item_name is None or item_price is None or item_description is None:
                                    print("No se ha podido obtener el nombre, precio o descripción del producto")
                                    continue
                                
                                notify(item_url, item_name, item_price, item_description, TRANS_LANG, INTEREST_RATE, PRODUCT_CATEGORY)

                            
                            line_count += 1
                            
                                
                    print(f'Procesadas {line_count-1} entradas.')
                driver.close()
                driver.quit()

                break
                
                
            else:
                print("Por favor, introducir 1 o 2!!!")
                continue
        except ValueError:
            print("Por favor, introducir un número y no letra!!!")
            continue



if __name__ == '__main__':
    main()
