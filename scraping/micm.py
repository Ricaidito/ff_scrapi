from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from enum import Enum


class MICMPCategory(Enum):
    CARNES = "Carnes"
    GRANOS = "Granos"
    EMBUTIDOS = "Embutidos"
    LACTEOS = "Lacteos"
    PAN = "Pan"
    VEGETALES = "Vegetales"


class MICMP:
    def __init__(self, category: MICMPCategory, wait_time_seconds: int = 1):
        self.__url = "https://preciosjustos.micm.gob.do/"
        self.__wait_time = wait_time_seconds
        self.__category = category

    def __get_basket_html(self) -> str:
        driver_options = ChromeOptions()
        driver_options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=driver_options)

        driver.get(self.__url)

        driver.implicitly_wait(self.__wait_time)

        html_doc = driver.page_source

        driver.quit()

        return html_doc

    def __get_section_html(self) -> str:
        driver_options = ChromeOptions()
        driver_options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=driver_options)

        driver.get(self.__url)
        driver.implicitly_wait(self.__wait_time)

        # Switch to meat category
        meat_category = driver.find_element(
            By.CSS_SELECTOR,
            f"li.nav-item[data-category='{self.__category.value}'] a.nav-link",
        )
        meat_category.click()

        # Wait for the click to be done
        driver.implicitly_wait(self.__wait_time)

        while True:
            try:
                # Wait for the products to load
                driver.implicitly_wait(self.__wait_time)

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
        driver.implicitly_wait(self.__wait_time)

        html_content = driver.page_source

        driver.quit()

        return html_content

    def __extract_basket(self, html_content: str) -> list[dict[str, str]]:
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

    def __extract_section(self, html_content: str) -> list[dict[str, str]]:
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
                    "category": self.__category.value.lower(),
                }
            )

        return items

    def get_basic_basket(self):
        html = self.__get_basket_html()
        basic_basket = self.__extract_basket(html)
        return basic_basket

    def get_prices_by_category(self):
        html = self.__get_section_html()
        items = self.__extract_section(html)
        return items

    def switch_category(self, category: MICMPCategory):
        self.__category = category

    def print_products(products: list[dict[str, str]]):
        if "category" in products[0]:
            for product in products:
                print(
                    f"{product['productName']}: {product['productPrice']} - {product['category']}"
                )
        else:
            for product in products:
                print(f"{product['productName']}: {product['productPrice']}")
        print("\n")


def main():
    micmp = MICMP(MICMPCategory.CARNES)
    basket = micmp.get_basic_basket()
    meat = micmp.get_prices_by_category()

    MICMP.print_products(basket)
    MICMP.print_products(meat)


if __name__ == "__main__":
    main()
