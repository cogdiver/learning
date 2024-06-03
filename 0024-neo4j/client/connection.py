from neo4j import GraphDatabase


# Manejo de la conexión a la base de datos
class Neo4jConnection:

    def __init__(self, uri, user, pwd):
        self._driver = GraphDatabase.driver(uri, auth=(user, pwd))

    def close(self):
        self._driver.close()

    def query(self, query, parameters=None):
        session = None
        response = None

        try:
            session = self._driver.session()
            response = session.run(query, parameters)

            return [record for record in response]

        except Exception as e:
            print("Query failed:", e)

        finally:
            if session is not None:
                session.close()
