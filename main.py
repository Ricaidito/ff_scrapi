import uvicorn
from fastapi import FastAPI
from scraping.models.product import Product, serialize_products, serialize_product
from scraping.models.basic_basket import BasicBasket, serialize_basic_basket
from scraping.db.db_service import DBService
from bson import ObjectId


PORT = 8000
app = FastAPI()

product_collection = DBService().get_collection("products")


@app.get("/", description="Root of the API, returns the docs url")
def api_root():
    return {"docs": f"http://localhost:{PORT}/docs"}


@app.get("/products", response_model=list[Product], description="Get all products")
def get_products():
    products = serialize_products(product_collection.find().limit(10))
    return products


@app.get(
    "/product/{product_id}", response_model=Product, description="Get a product by id"
)
def get_product(product_id: str):
    product = serialize_product(
        product_collection.find_one({"_id": ObjectId(product_id)})
    )
    return product


@app.get(
    "/basic-basket", response_model=BasicBasket, description="Get the basic basket"
)
def get_basic_basket():
    basic_basket_products = serialize_products(
        product_collection.find({"category": "basic_basket"})
    )
    basic_basket = serialize_basic_basket(basic_basket_products)
    return basic_basket


if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, reload=True)
