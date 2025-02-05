from connect import run_query

# Création des nœuds
persons = [
    "CREATE (p:Person {name: 'Alice', age: 30})",
    "CREATE (p:Person {name: 'Bob', age: 25})",
    "CREATE (p:Person {name: 'Charlie', age: 35})"
]

for person in persons:
    run_query(person)
