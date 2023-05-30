from scraping.micm import MICMP, MICMPCategory


def main():
    micmp = MICMP()
    basket = micmp.get_basic_basket()
    meat = micmp.get_prices_by_category(MICMPCategory.CARNES)

    MICMP.print_products(basket)
    MICMP.print_products(meat)


if __name__ == "__main__":
    main()
