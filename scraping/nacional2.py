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

first_page_source = driver.page_source

while True:

    page_count += 1

    driver.get(f'https://supermercadosnacional.com/carnes-pescados-y-mariscos/carnes/res?p={page_count}')

    # Wait for the page to load
    time.sleep(7)

    new_page_source = driver.page_source

    if first_page_source == new_page_source:
        break
    else:
        page_source += new_page_source


print(page_source)

driver.quit()
