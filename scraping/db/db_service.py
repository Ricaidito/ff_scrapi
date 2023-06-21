from pymongo import MongoClient


# https://pymongo.readthedocs.io/en/stable/tutorial.html
class DBService:
    def __init__(self, mongo_uri: str = "mongodb://localhost:27017/"):
        self.__client = MongoClient(mongo_uri)

    def get_collection(self, collection_name: str):
        return self.__client["foodforecast"][collection_name]
