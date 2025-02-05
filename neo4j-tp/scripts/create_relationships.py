from connect import run_query

# Création des relations
relationships = [
    "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'}) CREATE (a)-[:FRIEND]->(b)",
    "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)",
    "MATCH (a:Person {name: 'Bob'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)"
]

for relation in relationships:
    run_query(relation)
