from typing import Union
from bson import ObjectId
from pymongo import MongoClient
from pprint import pprint


class DBService:
    def __init__(self, mongo_uri: str = "mongodb://localhost:27017/"):
        self.__client = MongoClient(mongo_uri)

    def get_collection(self, collection_name: str):
        return self.__client["foodforecast"][collection_name]


class ProductService:
    def __init__(self):
        self.__products_collection = DBService().get_collection("products")
        self.__prices_collection = DBService().get_collection("prices")

    def get_product_by_id(self, product_id: str):
        product = self.__products_collection.find_one({"_id": ObjectId(product_id)})

        if product is None:
            return None

        price_history_entries = self.__prices_collection.find(
            {"productUrl": product["productUrl"]}
        ).sort("date", -1)

        product["priceHistory"] = list(price_history_entries)

        return product

    def get_products(self, skip: int, limit: int):
        pipeline = [
            {
                "$lookup": {
                    "from": "prices",
                    "localField": "productUrl",
                    "foreignField": "productUrl",
                    "as": "priceHistory",
                }
            },
            {"$unwind": "$priceHistory"},
            {"$sort": {"priceHistory.date": -1}},
            {
                "$group": {
                    "_id": "$_id",
                    "productName": {"$first": "$productName"},
                    "category": {"$first": "$category"},
                    "imageUrl": {"$first": "$imageUrl"},
                    "productUrl": {"$first": "$productUrl"},
                    "origin": {"$first": "$origin"},
                    "extractionDate": {"$first": "$extractionDate"},
                    "priceHistory": {"$push": "$priceHistory"},
                }
            },
            {"$sort": {"productName": 1}},
            {"$skip": skip},
            {"$limit": limit},
        ]

        products = self.__products_collection.aggregate(pipeline)
        return list(products)

    def upload_products_and_prices_to_db(
        self, products: list[dict[str, str]], prices: list[dict[str, Union[str, float]]]
    ):
        self.__products_collection.insert_many(products)
        self.__prices_collection.insert_many(prices)
        print("Products and prices uploaded successfully to the database.")


def main():
    page = 1
    limit = 10
    skip_value = (page - 1) * limit

    product_service = ProductService()

    products = product_service.get_products(skip_value, limit)

    for product in products:
        pprint(product)
        print("\n")

    # product = product_service.get_product_by_id("64a707d8a481b7c527b91b5d")
    # pprint(product)


if __name__ == "__main__":
    main()
