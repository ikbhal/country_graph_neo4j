from neo4j import GraphDatabase
from island_countries import island_countries as countries

# Establish a connection to Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Create a session to execute queries
with driver.session() as session:
    # Create countries and add properties

    
    for country in countries:
        session.run(
            """
            CREATE (:Country {
            name: $name, 
            population: $population,
            area: $area,
            capital: $capital
            })
            """,
            name=country["name"],
            population=country["population"],
            area=country["area"],
            capital=country["capital"]
        )
        print("create node for " + country["name"])

# Close the connection
driver.close()
