import uvicorn
from fastapi import FastAPI, HTTPException
from scraping.models.product import Product, serialize_products, serialize_product
from scraping.models.basic_basket import BasicBasket, serialize_basic_basket
from scraping.db.db_service import ProductService


PORT = 8000
app = FastAPI()
product_service = ProductService()


@app.get(
    "/",
    description="Root of the API, returns the docs url",
    responses={200: {"description": "Root of the API, returns the docs url"}},
)
def api_root():
    return {"docs": f"http://localhost:{PORT}/docs"}


@app.get(
    "/products",
    response_model=list[Product],
    description="Get all products",
    responses={
        200: {"description": "Get all products"},
        400: {"description": "Page or limit value must be greater than 0."},
    },
)
def get_products(page: int = 1, limit: int = 10):
    if page <= 0 or limit <= 0:
        raise HTTPException(
            status_code=400,
            detail="Page or limit value must be greater than 0.",
        )

    skip_value = (page - 1) * limit

    products = serialize_products(product_service.get_products(skip_value, limit))

    return products


@app.get(
    "/product/{product_id}",
    response_model=Product,
    description="Get a product by id",
    responses={
        200: {"description": "Get a product by id"},
        404: {"description": "Product not found"},
    },
)
def get_product(product_id: str):
    product = serialize_product(product_service.get_product_by_id(product_id))

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product


# TODO: Switch the logic to gather the products by category to the db service

# @app.get(
#     "/products/{category}",
#     response_model=list[Product],
#     description="Get all products by category",
#     responses={200: {"description": "Get all products by category"}},
# )
# def get_products_by_category(category: str):
#     products = serialize_products(product_collection.find({"category": category}))
#     return products


# TODO: Switch the logic to gather the basic basket to the db service

# @app.get(
#     "/basic-basket",
#     response_model=BasicBasket,
#     description="Get the basic basket",
#     responses={200: {"description": "Get the basic basket"}},
# )
# def get_basic_basket():
#     basic_basket_products = serialize_products(
#         product_collection.find({"category": "basket"})
#     )
#     basic_basket = serialize_basic_basket(basic_basket_products)
#     return basic_basket


if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, reload=True)
