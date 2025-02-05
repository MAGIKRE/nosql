from neo4j import GraphDatabase

# Connexion à la base Neo4j
uri = "bolt://localhost:7687"
user = "neo4j"
password = "password"  # Remplacez par votre mot de passe

driver = GraphDatabase.driver(uri, auth=(user, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result
