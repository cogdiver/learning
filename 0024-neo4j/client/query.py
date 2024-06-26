from connection import conn


def run_query(query):
    # Realizar una consulta
    result = conn.query(query)

    # Devolver los resultados de la consulta
    return result


def run_query_from_file(filepath):
    # Leer contenido del archivo
    with open(filepath) as f:
        content = f.read()

    # Devolver los resultados de la consulta
    return run_query(content)
