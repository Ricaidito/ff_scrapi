from pydantic import BaseModel


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


def serialize_basic_basket(basic_basket: BasicBasket) -> BasicBasket:
    basic_basket["id"] = str(basic_basket.pop("_id"))
    return basic_basket
