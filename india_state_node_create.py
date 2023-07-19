from neo4j import GraphDatabase
from india_states import indian_states as states

# Establish a connection to Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Create a session to execute queries
with driver.session() as session:
    
    for state in states:
        session.run(
            """
            MATCH (c:Country {name: 'India'})
            CREATE (:State {
                name: $name, 
                population: $population, 
                area: $area, 
                language: $language, 
                capital: $capital
            }) 
            -[p:PART_OF]->(c)
            """,
            name=state["name"],
            population=state["population"],
            area=state["area"],
            language=state["language"],
            capital=state["capital"]
        )
        print ("create node for  state " + state["name"])

# Close the connection
driver.close()
