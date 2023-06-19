from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
import time


class Nacional:
    def __init__(self, wait_time_seconds: int = 5):
        self.__wait_time = wait_time_seconds

    def __extract_products(self) -> list[dict[str, str]]:
        driver_options = ChromeOptions()
        driver_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=driver_options)

        driver.get(
            "https://supermercadosnacional.com/carnes-pescados-y-mariscos/carnes/res"
        )

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(self.__wait_time)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        html = driver.page_source

        items = []

        soup = BeautifulSoup(html, "html.parser")

        products = soup.find_all("li", class_="product-item")

        for product in products:
            name = product.find("a", class_="product-item-link").text.strip()
            price = product.find("span", class_="price").text.strip()
            items.append(
                {
                    "productName": name,
                    "productPrice": price,
                    "category": "res",
                }
            )

        driver.quit()

        return items

    def get_products(self) -> list[dict[str, str]]:
        products = self.__extract_products()
        return products

    def print_products(products: list[dict[str, str]]):
        for product in products:
            print(
                f"{product['productName']}: {product['productPrice']} - {product['category']}"
            )
        print("\n")


def main():
    nacional = Nacional()
    products = nacional.get_products()
    Nacional.print_products(products)


if __name__ == "__main__":
    main()
