from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize the Chrome driver
driver_options = ChromeOptions()
# driver_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=driver_options)

# Open the webpage
driver.get('https://supermercadosnacional.com/carnes-pescados-y-mariscos/carnes')

# Wait for the page to load
time.sleep(5)

# Scroll down to the bottom of the page until no more new products are loaded
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(15)

    # # Check if the "Load More" button exists
    # try:
    #     # Find the 'a' tag within the 'div' tag with a specific class
    #     load_more_button = driver.find_element_by_xpath("//div[@class='ias-trigger ias-trigger-next']//a")
    #     # Click the button
    #     load_more_button.click()

    #     time.sleep(6)
    # except Exception as e:
    #     print(e)
    #     break

# Once all products are loaded, you can use Beautiful Soup to parse the page HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')

# print(soup)

# Find all product elements (replace 'product_css_selector' with the actual CSS selector for the products)
products = soup.find_all('li', class_='product-item')

# Loop through the products and extract the information
for product in products:
    # Extract the product name (replace 'name_css_selector' with the actual CSS selector for the product name)
    name = product.find('a', class_='product-item-link').text.strip()

    # Extract the product price (replace 'price_css_selector' with the actual CSS selector for the product price)
    price = product.find('span', class_='price').text.strip()

    print(f'Product Name: {name}, Price: {price}')



# Close the driver
driver.quit()
