from neo4j import GraphDatabase

# Establish a connection to Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Create a session to execute queries
with driver.session() as session:
    # Define a list of continents
    continents = ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]

    # Create continent nodes
    for continent in continents:
        session.run(
            """
            CREATE (:Continent {name: $name})
            """,
            name=continent
        )
        print("continent created is " + continent)

# Close the connection
driver.close()
