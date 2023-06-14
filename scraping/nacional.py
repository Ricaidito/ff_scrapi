from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize the Chrome driver
driver_options = ChromeOptions()
driver_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=driver_options)

# Open the webpage
driver.get(f'https://supermercadosnacional.com/carnes-pescados-y-mariscos/carnes/res')

SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


html = driver.page_source

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

driver.quit()
