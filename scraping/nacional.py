from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from datetime import datetime


class Nacional:
    def __init__(self, wait_time_seconds: int = 7):
        self.__wait_time = wait_time_seconds

    def __parse_price(self, price: str) -> float:
        return float(price.replace("$", "").replace(",", ""))

    def __extract_products(self) -> list[dict[str, str]]:
        driver_options = ChromeOptions()
        driver_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=driver_options)

        driver.get("https://supermercadosnacional.com/lacteos-y-huevos/leches")

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(self.__wait_time)

            new_height = driver.execute_script("return document.body.scrollHeight")

            try:
                mas_productos_button = driver.find_element(
                    By.XPATH, "//*[contains(text(), 'Ver Más')]"
                )

                driver.execute_script("arguments[0].click();", mas_productos_button)
                time.sleep(self.__wait_time)

                if not mas_productos_button.is_displayed():
                    if new_height == last_height:
                        break

            except Exception:
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
            image = product.find("img", class_="product-image-photo")["src"]
            product_url = product.find("a", class_="product photo product-item-photo")[
                "href"
            ]
            items.append(
                {
                    "productName": name,
                    "productPrice": self.__parse_price(price),
                    "category": "res",
                    "imageUrl": image,
                    "productUrl": product_url,
                    "origin": "nacional",
                    "extractionDate": str(datetime.now()).split(".")[0],
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
