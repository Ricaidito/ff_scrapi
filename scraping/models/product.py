from pydantic import BaseModel


class Price(BaseModel):
    id: str
    productPrice: float
    productUrl: str
    date: str


class Product(BaseModel):
    id: str
    productName: str
    priceHistory: list[Price]
    category: str
    imageUrl: str
    productUrl: str
    origin: str
    extractionDate: str


def serialize_product(product) -> Product:
    if product is None:
        return None

    if "_id" in product:
        product["id"] = str(product.pop("_id"))

    if "priceHistory" in product:
        for price_history in product["priceHistory"]:
            if "_id" in price_history:
                price_history["id"] = str(price_history.pop("_id"))

    return product


def serialize_products(products) -> list[Product]:
    return [serialize_product(product) for product in products]
