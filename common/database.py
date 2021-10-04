# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import os
import urllib
from typing import Dict, List, Union

import pymongo
from dotenv import load_dotenv

load_dotenv()
print(os.environ.get("MONGO_USER"))


class Database:

    try:
        client = pymongo.MongoClient(
            "mongodb+srv://" +
            urllib.parse.quote_plus(os.environ.get("MONGO_USER")) +
            ":" +
            urllib.parse.quote_plus(os.environ.get("MONGO_PWD")) +
            "@main.rajun.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        )
        DATABASE = client.Main

    except TypeError as NoCredentialsError:
        print("MongoDB credentials not available")
        raise Exception(
            "MongoDB credentials not available"
        ) from NoCredentialsError

    @staticmethod
    def insert(collection: str, data: Union[Dict, List[Dict]]):
        if isinstance(data, Dict):
            Database.DATABASE[collection].insert_one(data)
        else:
            Database.DATABASE[collection].insert_many(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.CursorType:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(
            query, data, upsert=True
        )

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].delete_many(filter=query)
