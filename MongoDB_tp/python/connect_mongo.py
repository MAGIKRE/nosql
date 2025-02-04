from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Accès à la base de données
print("Connexion réussie à MongoDB")