from pydantic import BaseModel
from scraping.models.product import Product


class BasicBasket(BaseModel):
    productsAmount: int
    totalAmount: float
    products: list[Product]


def __calculate_total_amount(basic_basket_products: list[Product]) -> float:
    total_amount = 0
    for product in basic_basket_products:
        total_amount += product["productPrice"]

    return round(total_amount, 2)


def serialize_basic_basket(basic_basket_products: list[Product]) -> BasicBasket:
    return {
        "productsAmount": len(basic_basket_products),
        "totalAmount": __calculate_total_amount(basic_basket_products),
        "products": basic_basket_products,
    }
