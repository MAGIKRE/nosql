from connect import run_query

# Récupérer toutes les personnes
query_all_persons = "MATCH (p:Person) RETURN p.name, p.age"
results = run_query(query_all_persons)

for record in results:
    print(f"Name: {record['p.name']}, Age: {record['p.age']}")

# Trouver les amis d'une personne
def get_friends(name):
    query = f"""
    MATCH (p:Person {{name: '{name}'}})-[:FRIEND]->(friend)
    RETURN friend.name, friend.age
    """
    return run_query(query)

friends = get_friends("Alice")
for friend in friends:
    print(f"Friend: {friend['friend.name']} (Age: {friend['friend.age']})")
