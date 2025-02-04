from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
collection = client.mydb.accounts

# Création d'un index
collection.create_index("address.city", name="city_index")

# Agrégation : total des soldes par ville
pipeline = [
    {"$group": {"_id": "$address.city", "total_balance": {"$sum": "$balance"}}},
    {"$sort": {"total_balance": -1}}
]

for result in collection.aggregate(pipeline):
    print(f"{result['_id']}: {result['total_balance']}")