GET_NEXT_BUTTON_SCRIPT = "return document.querySelector('[data-testid=pagination-next-button] > button')"





MERCARI_DEFAULT_URL = "https://jp.mercari.com"

GET_ITEM_NAME = "return document.querySelector('#item-info > section:nth-child(1) > div > mer-heading').shadowRoot.querySelector('div > div > h1').textContent"

GET_ITEM_PRICE = "return document.querySelector('mer-price').shadowRoot.querySelector('span:nth-of-type(2)').textContent"


"""
xpath=//div[@id='item-info']/section[2]
"""
GET_ITEM_DESCRIPTION = "return document.querySelector('#item-info > section:nth-child(2)').textContent"

#xpath=//main[@id='main']/article/div/section/div/div/div/div/div/div/div/div/div/div/div/div/mer-item-thumbnail (check if mer-item-thumbnail has sticker="sold" attribute)
GET_ITEM_SOLD = "return document.querySelector('#main > article > div:nth-child(1) > section > div > div > div > div > div > div > div > div > div > div > div > div > mer-item-thumbnail').getAttribute('sticker')"


