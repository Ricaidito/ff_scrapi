from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint


URL = "https://preciosjustos.micm.gob.do/"
WAIT_TIME = 3


def save_to_html(html_content, file_name):
    with open(file_name, "w") as f:
        f.write(html_content)


def get_basic_basket_html(url: str) -> str:
    driver = webdriver.Chrome()

    driver.get(url)
    driver.implicitly_wait(WAIT_TIME)

    html_doc = driver.page_source

    driver.quit()

    save_to_html(html_doc, "basic_basket.html")

    return html_doc


def get_meat_html(url: str) -> str:
    driver = webdriver.Chrome()

    driver.get(url)
    driver.implicitly_wait(WAIT_TIME)

    # Switch to meat category
    meat_category = driver.find_element(
        By.CSS_SELECTOR, "li.nav-item[data-category='Carnes'] a.nav-link"
    )
    meat_category.click()

    # Wait for the click to be done
    driver.implicitly_wait(WAIT_TIME)

    # Find the "Mas Productos" button and click it
    mas_productos_button = driver.find_element(
        By.XPATH, "//*[contains(text(), 'Mas Productos')]"
    )

    # Click the button using javascript
    driver.execute_script("arguments[0].click();", mas_productos_button)

    driver.implicitly_wait(WAIT_TIME)

    save_to_html(driver.page_source, "meat.html")

    return driver.page_source


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


def extract_meat_prices(html_content: str) -> list[dict[str, str]]:
    pass


def main():
    x = get_meat_html(URL)


if __name__ == "__main__":
    main()
