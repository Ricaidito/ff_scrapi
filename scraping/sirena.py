from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from enum import Enum


url = "https://sirena.do/products/category/carnes?page=1&limit=0&sort=1"
wait_time = 2

driver_options = ChromeOptions()
driver_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=driver_options)

driver.get(url)

driver.implicitly_wait(wait_time)

html_doc = driver.page_source

driver.quit()

soup = BeautifulSoup(html_doc, "html.parser")

product_divs = soup.find_all("div", class_="item-product-info")
print("Found", len(product_divs), "products")

for product_div in product_divs:
    title = product_div.find("p", class_="item-product-title").text.strip()
    price = product_div.find("p", class_="item-product-price").strong.text.strip()

    print("Title:", title)
    print("Price:", price)
    print("---")


class SirenaCategory(Enum):
    CARNES = "carnes"
    CONGELADOS = "congelados"
    DELI = "deli"
    DESPENSA = "despensa"
    GALLETAS_Y_DULCES = "galletas-y-dulces"
    LACTEOS_Y_HUEVOS = "lacteos-y-huevos"
    LISTOS_PARA_COMER = "listos-para-comer"
    PANADERIA_Y_REPOSTERIA = "panaderia-y-reposteria"
    PESCADOS_Y_MARISCOS = "pescados-y-mariscos"
    PICADERAS = "picaderas"


class Sirena:
    def __init__(self, category: SirenaCategory, wait_time_seconds: int = 2):
        self.__wait_time = 2
        self.__base_url = "https://sirena.do/products/category/"
