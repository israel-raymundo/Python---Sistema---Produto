from database.connection import get_connection


def inserir_produto(nome, preco, estoque):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, preco, estoque)
        VALUES (?, ?, ?)
    """, (nome, preco, estoque))

    conn.commit()
    conn.close()

def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos WHERE ativo = 1")
    produtos = cursor.fetchall()

    conn.close()
    return produtos

def buscar_produto_por_id(produto_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos WHERE id = ? AND ativo = 1", (produto_id,))
    produto = cursor.fetchone()

    conn.close()
    return produto

def atualizar_estoque(produto_id, nova_quantidade):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE produtos
        SET estoque = ?
        WHERE id = ?
    """, (nova_quantidade, produto_id))

    conn.commit()
    conn.close()