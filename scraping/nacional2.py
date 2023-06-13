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


page_count = 1

# Open the webpage
driver.get(f'https://supermercadosnacional.com/carnes-pescados-y-mariscos/carnes/res?p={page_count}')

# Wait for the page to load
time.sleep(7)

# Get the page source
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

products = soup.find_all('li', class_='product-item')

first_products = products.copy()


while True:

    page_count += 1

    driver.get(f'https://supermercadosnacional.com/carnes-pescados-y-mariscos/carnes/res?p={page_count}')

    # Wait for the page to load
    time.sleep(7)

    new_page_source = driver.page_source

    new_souop = BeautifulSoup(new_page_source, 'html.parser')

    new_products = new_souop.find_all('li', class_='product-item')

    # print(new_products)

    if first_products == new_products:
        break
    else:
        products.append(new_products)
        print('New products added')


# print(products)

driver.quit()
