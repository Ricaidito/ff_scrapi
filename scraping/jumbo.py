from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = "https://jumbo.com.do/supermercado/carnes-pescados-y-mariscos/carnes.html?p=1"

# Initialize the Chrome driver
driver = webdriver.Chrome('path_to_your_chromedriver')

# Get the web page
driver.get(url)

while True:
    # Wait for the page to load
    time.sleep(3)

    # Get the HTML content of the web page
    html = driver.page_source

    # Parse the HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all product containers
    product_containers = soup.find_all('div', class_='product-item-details')

    for product in product_containers:
        # Extract product name
        product_name = product.find('a', class_='product-item-tile__link').text.strip()

        # Extract product price
        product_price = product.find('span', class_='product-item-tile__price-current').text.strip()

        print(f'Product: {product_name}, Price: {product_price}')

    # Try to click the "next page" button
    try:
        next_button = driver.find_element_by_css_selector('a[title="Siguiente"]')
        next_button.click()
    except Exception as e:
        # If the "next page" button is not found, we're probably on the last page
        print("End of pages")
        break

# Close the driver
driver.quit()
