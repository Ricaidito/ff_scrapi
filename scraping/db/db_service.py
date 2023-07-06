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

        # Gather all the price history entries for the product and sort them by date, the "date" field has this format "2023-07-06 14:28:40.349967"
        price_history_entries = sorted(
            self.__prices_collection.find({"productUrl": product["productUrl"]}),
            key=lambda entry: entry["date"],
            reverse=True,
        )

        # Remove all the _id fields from the price history entries and productUrl from the product
        for entry in price_history_entries:
            print(entry)
            del entry["_id"]
            del entry["productUrl"]

        # Add the priceHistory field to the product
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
                    "priceHistory": {
                        "$push": {
                            # "_id": "$priceHistory._id",
                            # "productUrl": "$priceHistory.productUrl,
                            "productPrice": "$priceHistory.productPrice",
                            "date": "$priceHistory.date",
                        }
                    },
                }
            },
            {
                "$addFields": {
                    "priceHistory": {
                        "$map": {
                            "input": "$priceHistory",
                            "as": "price",
                            "in": {
                                "_id": "$$price._id",
                                "productPrice": "$$price.productPrice",
                                "date": "$$price.date",
                            },
                        }
                    }
                }
            },
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
    product_service = ProductService()
    products = product_service.get_products(0, 10)
    for product in products:
        pprint(product)
        print("\n")

    # product = product_service.get_product_by_id("64a707d8a481b7c527b91b5d")
    # pprint(product)


if __name__ == "__main__":
    main()
