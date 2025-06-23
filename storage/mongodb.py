from pymongo import MongoClient
from typing import List, Dict

class MongoStorage:
    def __init__(
        self,
        uri="mongodb://root:rootpassword@localhost:27017/sentiment_monitor?authSource=admin",
        db_name="sentiment_monitor",
        collection_name="posts"
    ):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_posts(self, posts):
        if posts:
            self.collection.insert_many(posts)

    def find(self, query={}, limit=50):
        return list(self.collection.find(query).limit(limit))