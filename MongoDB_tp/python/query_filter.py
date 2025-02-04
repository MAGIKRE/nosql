from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
collection = client.mydb.mycollection

# Opérateurs logiques
query = {"$and": [{"age": {"$gt": 25}}, {"email": {"$regex": "@example\\.com$"}}]}
for doc in collection.find(query):
    print(doc)

# Projection
projection = {"_id": 0, "name": 1, "email": 1}
for doc in collection.find({}, projection):
    print(doc)

# Tri des résultats
for doc in collection.find().sort("name"):
    print(doc)