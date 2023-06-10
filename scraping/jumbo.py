from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup


# TODO: Add categories and the ability to switch between them
class Jumbo:
    def __init__(self):
        self.__url = "https://jumbo.com.do/supermercado/carnes-pescados-y-mariscos/carnes.html?product_list_limit=all"

    def __extract_products(self) -> str:
        driver_options = ChromeOptions()
        driver_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=driver_options)

        driver.get(self.__url)

        html = driver.page_source

        driver.quit()

        return html

    def __get_products(self, html_content: str) -> list[dict[str, str]]:
        items = []
        soup = BeautifulSoup(html_content, "html.parser")

        products = soup.find_all("div", class_="product-item-details")

        for product in products:
            name = product.find("a", class_="product-item-tile__link").text.strip()
            price = product.find(
                "span", class_="product-item-tile__price-current"
            ).text.strip()

            items.append(
                {
                    "productName": name,
                    "productPrice": price,
                    # "category": self.__category.value.lower(),
                }
            )

        return items

    def get_products(self) -> list[dict[str, str]]:
        html = self.__extract_products()
        products = self.__get_products(html)
        return products


def main():
    jumbo = Jumbo()
    meats = jumbo.get_products()
    print(meats)


if __name__ == "__main__":
    main()
