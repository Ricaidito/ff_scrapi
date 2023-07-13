from pydantic import BaseModel
from datetime import datetime


class BasketProduct(BaseModel):
    productName: str
    productPrice: float
    imageUrl: str


class BasicBasket(BaseModel):
    id: str
    productsAmount: int
    totalAmount: float
    products: list[BasketProduct]
    extractionDate: str
    origin: str


def serialize_basic_basket(basic_basket_products: list[BasketProduct]) -> BasicBasket:
    return {
        "productsAmount": len(basic_basket_products),
        # "totalAmount": __calculate_total_amount(basic_basket_products),
        "products": basic_basket_products,
        "extractionDate": datetime.now().isoformat(),
    }
