from vars import URL, USERNAME, PASSWORD
from connection import Neo4jConnection


# Conectar a la base de datos
conn = Neo4jConnection(uri=URL, user=USERNAME, pwd=PASSWORD)

# Realizar una consulta
result = conn.query("MATCH (n) RETURN n LIMIT 5")
for record in result:
    print(record)

# Cerrar la conexión
conn.close()
