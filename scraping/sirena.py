from scraping.categories.category import SirenaCategory
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class Sirena:
    def __init__(self, category: SirenaCategory, wait_time_seconds: int = 5):
        self.__wait_time = wait_time_seconds
        self.__category = category
        self.__base_url = f"https://sirena.do/products/category/{self.__category.value}?page=1&limit=0&sort=1"

    def __extract_products(self) -> str:
        driver_options = ChromeOptions()
        driver_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=driver_options)

        driver.get(self.__base_url)

        WebDriverWait(driver, self.__wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.item-product-info"))
        )
        driver.implicitly_wait(self.__wait_time)

        html_doc = driver.page_source

        driver.quit()

        return html_doc

    def __get_products(self, html_content: str) -> list[dict[str, str]]:
        items = []
        soup = BeautifulSoup(html_content, "html.parser")

        products = soup.find_all("div", class_="item-product-info")

        for product in products:
            name = product.find("p", class_="item-product-title").text.strip()
            price = product.find("p", class_="item-product-price").strong.text.strip()
            items.append(
                {
                    "productName": name,
                    "productPrice": price,
                    "category": self.__category.value.lower(),
                }
            )
        return items

    def switch_category(self, category: SirenaCategory):
        self.__category = category
        self.__base_url = f"https://sirena.do/products/category/{self.__category.value}?page=1&limit=0&sort=1"

    def get_products(self) -> list[dict[str, str]]:
        html = self.__extract_products()
        products = self.__get_products(html)
        return products

    def print_products(products: list[dict[str, str]]):
        for product in products:
            print(
                f"{product['productName']}: {product['productPrice']} - {product['category']}"
            )
        print("\n")


def main():
    sirena = Sirena(SirenaCategory.CARNES)
    meats = sirena.get_products()
    sirena.switch_category(SirenaCategory.DELI)
    deli = sirena.get_products()

    Sirena.print_products(meats)
    Sirena.print_products(deli)


if __name__ == "__main__":
    main()
