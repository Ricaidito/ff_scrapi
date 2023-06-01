from scraping.categories.category import MICMPCategory, SirenaCategory
from scraping.micm import MICMP
from scraping.sirena import Sirena


def main():
    micmp = MICMP(MICMPCategory.CARNES)
    basket = micmp.get_basic_basket()
    meat = micmp.get_prices_by_category()

    MICMP.print_products(basket)
    MICMP.print_products(meat)

    sirena = Sirena(SirenaCategory.DELI)
    deli = sirena.get_products()
    sirena.switch_category(SirenaCategory.LISTOS_PARA_COMER)
    ready_to_eat = sirena.get_products()

    Sirena.print_products(deli)
    Sirena.print_products(ready_to_eat)


if __name__ == "__main__":
    main()
