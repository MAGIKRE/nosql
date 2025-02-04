from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
collection = db.mycollection

# Création (Insertion)
document = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
result = collection.insert_one(document)
print("ID du document inséré:", result.inserted_id)

# Lecture (Query)
query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)

# Mise à jour
update = {"$set": {"age": 31}}
result = collection.update_one(query, update)
print("Nombre de documents modifiés:", result.modified_count)

# Suppression
result = collection.delete_one(query)
print("Nombre de documents supprimés:", result.deleted_count)