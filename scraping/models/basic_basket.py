from pydantic import BaseModel
from scraping.models.product import Product


class BasicBasket(BaseModel):
    productsAmount: int
    totalAmount: float
    products: list[Product]


def serialize_basic_basket(basic_basket_products: list[Product]) -> BasicBasket:
    return {
        "productsAmount": len(basic_basket_products),
        "totalAmount": 0,  # WIP: Calculate total amount
        "products": basic_basket_products,
    }
