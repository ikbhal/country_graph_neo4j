from neo4j import GraphDatabase
from karnataka_districts import karnataka_districts as districts

# Establish a connection to Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Create a session to execute queries
with driver.session() as session:
    
    for district in districts:
        session.run(
            """
            MATCH (s:State {name: 'Karnataka'})
            CREATE (d:District {
                name: $name, 
                population: $population, 
                area: $area, 
                headquarter: $headquarter
            }) 
            -[p:PART_OF]->(s)
            """,
            name=district["name"],
            population=district["population"],
            area=district["area"],
            headquarter=district["headquarter"]
        )
        print ("create node for  district " + district["name"])

# Close the connection
driver.close()
