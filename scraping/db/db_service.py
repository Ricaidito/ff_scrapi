from typing import Union
from pymongo import MongoClient


# https://pymongo.readthedocs.io/en/stable/tutorial.html
class DBService:
    def __init__(self, mongo_uri: str = "mongodb://localhost:27017/"):
        self.__client = MongoClient(mongo_uri)

    def get_collection(self, collection_name: str):
        return self.__client["foodforecast"][collection_name]


class ProductService:
    def __init__(self):
        self.__products_collection = DBService().get_collection("products")
        self.__prices_collection = DBService().get_collection("prices")

    def upload_products(
        self, products: list[dict[str, str]], prices: list[dict[str, Union[str, float]]]
    ):
        self.__products_collection.insert_many(products)
        self.__prices_collection.insert_many(prices)
