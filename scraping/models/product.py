from pydantic import BaseModel


class Product(BaseModel):
    id: str
    productName: str
    productPrice: str
    category: str
    extractionDate: str


def serialize_product(product) -> Product:
    if product is None:
        return None
    return {**product, "id": str(product["_id"])}


def serialize_products(products) -> list[Product]:
    return [{**product, "id": str(product["_id"])} for product in products]
