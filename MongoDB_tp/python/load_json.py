import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
collection = client.mydb.accounts

with open('python/accounts.json') as file:
    data = json.load(file)

result = collection.insert_many(data)
print("IDs des documents insérés:", result.inserted_ids)