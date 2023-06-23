from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from categories.category import JumboCategory
from datetime import datetime


class Jumbo:
    def __init__(self, category: JumboCategory):
        self.__category = category
        self.__url = f"https://jumbo.com.do/supermercado/{self.__category.value}?product_list_limit=all"

    def __extract_products(self) -> str:
        driver_options = ChromeOptions()
        driver_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=driver_options)

        driver.get(self.__url)

        html = driver.page_source

        driver.quit()

        return html

    def __parse_price(self, price: str) -> float:
        return float(price.split("$")[1].replace(",", ""))

    def __get_products(self, html_content: str) -> list[dict[str, str]]:
        items = []
        soup = BeautifulSoup(html_content, "html.parser")

        products = soup.find_all("div", class_="product-item-info")

        for product in products:
            name = product.find("div", class_="product-item-tile__name").text.strip()
            price = product.find(
                "span", class_="product-item-tile__price-current"
            ).text.strip()
            image = product.find("img", class_="product-item-tile__img")["src"]
            items.append(
                {
                    "productName": name,
                    "productPrice": self.__parse_price(price),
                    "category": self.__category.value.lower(),
                    "imageUrl": image,
                    "origin": "jumbo",
                    "extractionDate": str(datetime.now()).split(".")[0],
                }
            )

        return items

    def switch_category(self, category: JumboCategory):
        self.__category = category
        self.__url = f"https://jumbo.com.do/supermercado/{self.__category.value}?product_list_limit=all"

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
    jumbo = Jumbo(JumboCategory.CARNES)
    meats = jumbo.get_products()
    # Jumbo.print_products(meats)
    print(meats)


if __name__ == "__main__":
    main()
