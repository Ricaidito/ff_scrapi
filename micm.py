from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from pprint import pprint


URL = "https://preciosjustos.micm.gob.do/"
WAIT_TIME = 3


# Save the html to a file
def save_to_html(html_content, file_name):
    with open(file_name, "w") as f:
        f.write(html_content)


# Get the html of the basic basket
def get_basic_basket_html(url: str) -> str:
    driver_options = ChromeOptions()
    driver_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=driver_options)

    driver.get(url)
    driver.implicitly_wait(WAIT_TIME)

    html_doc = driver.page_source

    driver.quit()

    return html_doc


# Save the html of the basic basket
def save_basic_basket_html(url: str, file_name: str):
    html_doc = get_basic_basket_html(url)
    save_to_html(html_doc, file_name)


# Get the html of a section
def get_section_html(url: str, category_name: str) -> str:
    driver_options = ChromeOptions()
    driver_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=driver_options)

    driver.get(url)
    driver.implicitly_wait(WAIT_TIME)

    # Switch to meat category
    meat_category = driver.find_element(
        By.CSS_SELECTOR, f"li.nav-item[data-category='{category_name}'] a.nav-link"
    )
    meat_category.click()

    # Wait for the click to be done
    driver.implicitly_wait(WAIT_TIME)

    while True:
        try:
            # Wait for the products to load
            driver.implicitly_wait(WAIT_TIME)

            # Find the "Mas Productos" button and click it
            mas_productos_button = driver.find_element(
                By.XPATH, "//*[contains(text(), 'Mas Productos')]"
            )
            # Click the button using javascript
            driver.execute_script("arguments[0].click();", mas_productos_button)

            # If the button to get more products is hidden, stop the loop
            if not mas_productos_button.is_displayed():
                break

        # If any of the elements are not found, stop the loop
        except NoSuchElementException:
            break

    # Wait for the products to load
    driver.implicitly_wait(WAIT_TIME)

    html_content = driver.page_source

    driver.quit()

    return html_content


# Save the html of a section
def save_get_section_html(url: str, category_name: str, file_name: str):
    html_content = get_section_html(url, category_name)
    save_to_html(html_content, file_name)


# Extract the products and prices from the basic basket
def extract_basic_basket(html_content: str) -> list[dict[str, str]]:
    basic_basket = []
    soup = BeautifulSoup(html_content, "html.parser")

    products = soup.find_all("div", class_="product-card")

    for product in products:
        name = product.find("span", class_="productTitle").text.strip()
        price = product.find("strong", class_="productPrice").text.strip()
        basic_basket.append(
            {
                "productName": name,
                "productPrice": price,
            }
        )

    return basic_basket


# Extract the products and prices from a section
def extract_section_prices(html_content: str, category: str) -> list[dict[str, str]]:
    items = []
    soup = BeautifulSoup(html_content, "html.parser")

    products = soup.find_all("div", class_="product-card")

    for product in products:
        name = product.find("span", class_="productTitle").text.strip()
        price = product.find("strong", class_="productPrice").text.strip()
        items.append(
            {
                "productName": name,
                "productPrice": price,
                "category": category.lower(),
            }
        )

    return items


# Driver code
def main():
    # save_get_section_html(URL, "Carnes", "carnes.html")

    # products = extract_basic_basket(html_content=get_basic_basket_html(URL))
    # pprint(products)

    products = extract_section_prices(
        html_content=get_section_html(URL, "Vegetales"), category="vegetales"
    )
    pprint(products, indent=4)


if __name__ == "__main__":
    main()
