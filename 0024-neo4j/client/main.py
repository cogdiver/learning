from connection import conn
from query import run_query, run_query_from_file


# run_query_from_file("/data/init.cypher")

# Realizar una consulta
result = run_query("MATCH (n) RETURN n LIMIT 5")
if result:
    for record in result:
        print(record)
else:
    print("Not results")

# Cerrar la conexión
conn.close()
