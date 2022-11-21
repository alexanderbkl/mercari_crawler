# create a class with input methods and assign it to a variable for other modules to use

class Input:
    def __init__(self, MERCARI_URL = 0, QUANTITY = 0, PRODUCT_CATEGORY = "", INTEREST_RATE = 0, TRANS_LANG = ""):
        self._MERCARI_URL = MERCARI_URL
        self._QUANTITY = QUANTITY
        self._PRODUCT_CATEGORY = PRODUCT_CATEGORY
        self._INTEREST_RATE = INTEREST_RATE
        self._TRANS_LANG = TRANS_LANG
    
    
    def get_INTEREST_RATE(self):
        return self._INTEREST_RATE
    
    def get_PRODUCT_CATEGORY(self):
        return self._PRODUCT_CATEGORY
    
    def get_TRANS_LANG(self):
        return self._TRANS_LANG
    
    def get_QUANTITY(self):
        return self._QUANTITY
    
    def get_MERCARI_URL(self):
        return self._MERCARI_URL
    

    # assign the keyword to MERCARI_URL
    def set_MERCARI_URL(self):
            # ask for a keyword input (default is nintendo) with error checking
        while True:
            self.keyword = input("Introducir palabra clave a buscar (ej.: nintendo): ")
            if self.keyword == "":
                self.keyword = "nintendo"
            else:
                break
        self._MERCARI_URL = "https://jp.mercari.com/search/?keyword=" + self.keyword
    def set_QUANTITY(self):
        # get a number input of quantity of products with error checks and default value of 10
        self._QUANTITY = 10
    
        while True:
            try:
                self._QUANTITY = int(input("Cuántos productos quieres obtener? (ej.: 10): "))
                if self._QUANTITY < 1:
                    print("Por favor, introducir un número mayor a 0!!!")
                    continue
            except ValueError:
                print("Por favor, introducir un número y no letra!!!")
                continue
            else:
                break

    def set_PRODUCT_CATEGORY(self):
        self._PRODUCT_CATEGORY = ''
    
        # ask for a product category input (default is Consolas y videojuegos>Consolas y videojuegos) with error checking

        while True:
            self._PRODUCT_CATEGORY = input("Introducir categoría de producto (ej.: Consolas y videojuegos>Nintendo): ")
            if self._PRODUCT_CATEGORY == "":
                self._PRODUCT_CATEGORY = 'Consolas y videojuegos>Nintendo'
                break
            else:
                break
            
    def set_INTEREST_RATE(self):
        # ask for an interest rate (default is 50%) with error checking

        self._INTEREST_RATE = 50

        while True:
            try:
                interest_input = input("Introducir interés a calcular en porcentaje (ej.: 50): ")
                if self._INTEREST_RATE < 0:
                    print("Por favor, introducir un número mayor a 0!!!")
                    continue
                if interest_input == "":
                    self._INTEREST_RATE = 50
                    break
                else:
                    self._INTEREST_RATE = float(interest_input)
                    break
            except ValueError:
                print("Por favor, introducir un número y no letra!!!")
                continue
            
    def set_TRANS_LANG(self):
        # ask for a translation dest language input (default is en) with error checking
        while True:
            self._TRANS_LANG = input("Introducir lenguaje de destino de traducción (ej.: en, es, de, ...): ")
            if self._TRANS_LANG == "":
                self._TRANS_LANG = 'en'
                break
            else:
                break
            
