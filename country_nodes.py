from neo4j import GraphDatabase

# Establish a connection to Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Create a session to execute queries
with driver.session() as session:
    # Create countries and add properties
    countries = [
        {"name": "Afghanistan", "population": 38928346, "area": 652230, "population_density": 59.6, "capital": "Kabul"},
        {"name": "Albania", "population": 2877797, "area": 28748, "population_density": 105.3, "capital": "Tirana"},
        {"name": "Algeria", "population": 43851044, "area": 2381741, "population_density": 18.4, "capital": "Algiers"},
        # Add more countries here...
    ]
    
    for country in countries:
        session.run(
            """
            CREATE (:Country {name: $name, population: $population, area: $area, population_density: $population_density, capital: $capital})
            """,
            name=country["name"],
            population=country["population"],
            area=country["area"],
            population_density=country["population_density"],
            capital=country["capital"]
        )

# Close the connection
driver.close()
