from connect import run_query

def recommend_movies(liked_actor_name):
    query = f"""
    MATCH (liked_actor:Actor {{name: '{liked_actor_name}'}})-[:ACTED_IN]->(liked_movie:Movie)
    MATCH (other_actor:Actor)-[:ACTED_IN]->(liked_movie)
    MATCH (other_actor)-[:ACTED_IN]->(recommended_movie:Movie)
    WHERE NOT (liked_actor)-[:ACTED_IN]->(recommended_movie)
    RETURN DISTINCT recommended_movie.title AS title, recommended_movie.year AS year
    ORDER BY year DESC
    """
    return run_query(query)

liked_actor = "Tom Hanks"
recommendations = recommend_movies(liked_actor)

print(f"Recommendations based on liking {liked_actor}:")
for rec in recommendations:
    print(f"{rec['title']} ({rec['year']})")
