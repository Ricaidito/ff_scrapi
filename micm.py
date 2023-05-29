from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint


URL = "https://preciosjustos.micm.gob.do/"


def get_basic_basket_html(url: str) -> str:
    driver = webdriver.Chrome()

    driver.get(url)
    driver.implicitly_wait(3)

    html_doc = driver.page_source

    driver.quit()

    return html_doc


def get_meat_html(url: str) -> str:
    driver = webdriver.Chrome()

    driver.get(url)
    driver.implicitly_wait(3)

    html_doc = driver.page_source

    driver.quit()

    return html_doc


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


basic_basket_html = get_basic_basket_html(URL)
basic_basket = extract_basic_basket(basic_basket_html)
pprint(basic_basket)
