from database.connection import get_connection

def inserir_cliente(nome, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO clientes (nome, email)
        VALUES (?, ?)
    """, (nome, email))

    conn.commit()
    conn.close()

def listar_clientes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    conn.close()
    return clientes