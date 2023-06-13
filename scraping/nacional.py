from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time

url = 'https://supermercadosnacional.com/carnes-pescados-y-mariscos/carnes'

def page_source_html(driverLink):

    # Inicializa el driver de Selenium (Asegúrate de tener el driver correcto para tu navegador y SO)
    driver_options = ChromeOptions()
    # driver_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=driver_options)
    # Abre la página
    driver.get(driverLink)

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # scroll down to bottom
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        # wait to load page
        time.sleep(20)

        # calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # get page source
    page_source = driver.page_source

    driver.quit()

    return page_source


# Obtiene el contenido de la página
html = page_source_html(url)

# Utiliza Beautiful Soup para analizar el contenido
soup = BeautifulSoup(html, 'html.parser')

# Encuentra todos los productos y sus precios
products = soup.find_all('li', class_='product-item') # Ajusta la clase según sea necesario

# print(products)

for product in products:
    name = product.find('a', class_='product-item-link').text.strip() # Ajusta la clase según sea necesario
    # print(name)
    price = product.find('span', class_='price').text.strip() # Ajusta la clase según sea necesario
    # print(price)
    print(f'Producto: {name}, Precio: {price}')

# Cierra el driver
