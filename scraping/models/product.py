from pydantic import BaseModel


class Price(BaseModel):
    price: float
    date: str


class Product(BaseModel):
    id: str
    productName: str
    productPrices: list[Price]
    category: str
    imageUrl: str
    productUrl: str
    origin: str
    extractionDate: str


def serialize_product(product) -> Product:
    if product is None:
        return None
    return {**product, "id": str(product["_id"])}


def serialize_products(products) -> list[Product]:
    return [{**product, "id": str(product["_id"])} for product in products]
