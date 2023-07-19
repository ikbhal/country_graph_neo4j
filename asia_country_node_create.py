from neo4j import GraphDatabase
from asia_country_list import asian_countries as countries

# Establish a connection to Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"


def create_asia_country_node_list():
    driver = GraphDatabase.driver(uri, auth=(username, password))
    # Create a session to execute queries
    with driver.session() as session:
        for country in countries:
            session.run(
                """
                CREATE (:Country {
                    name: $name,
                    population: $population, 
                    area: $area, 
                    capital: $capital})
                """,
                name=country["name"],
                population=country["population"],
                area=country["area"],
                capital=country["capital"]
            )
            print("create node for " + country["name"])

    # Close the connection
    driver.close()


def create_relation_asia_country_to_asia():
    driver = GraphDatabase.driver(uri, auth=(username, password))
    # Create a relationship between Africa continent and Africa countries
    with driver.session() as session:
        for country in countries:
            session.run(
                """
                MATCH (c:Country {name: $country}), (cn:Continent {name: 'Asia'})
                CREATE (c)-[:PART_OF]->(cn)
                """,
                country=country
            )
            print("create relation between Asia continent and Asia country $country")
    # Close the connection
    driver.close()

if __name__ == '__main__':
    # create_asia_country_node_list()
    create_relation_asia_country_to_asia()