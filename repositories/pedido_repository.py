from database.connection import get_connection

def criar_pedido(cliente_id, total):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pedidos (cliente_id, total)
        VALUES (?, ?)
    """, (cliente_id, total))

    pedido_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return pedido_id

def inserir_item_pedido(pedido_id, produto_id, quantidade, preco_unitario):

    if not isinstance(quantidade, int) or quantidade <= 0:
        print("Quantidade inválida.")
        return False

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario)
        VALUES (?, ?, ?, ?)
    """, (pedido_id, produto_id, quantidade, preco_unitario))

    conn.commit()
    conn.close()

    return True


def listar_pedidos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            pedidos.id AS pedido_id,
            clientes.nome AS cliente_nome,
            produtos.nome AS produto_nome,
            itens_pedido.quantidade,
            itens_pedido.preco_unitario,
            pedidos.total,
            pedidos.status
        FROM pedidos
        JOIN clientes ON pedidos.cliente_id = clientes.id
        JOIN itens_pedido ON itens_pedido.pedido_id = pedidos.id
        JOIN produtos ON itens_pedido.produto_id = produtos.id
    """)

    pedidos = cursor.fetchall()
    conn.close()
    return pedidos

def buscar_pedido_por_id(pedido_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (pedido_id,))
    pedido = cursor.fetchone()

    conn.close()
    return pedido

def buscar_itens_por_pedido(pedido_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM itens_pedido
        WHERE pedido_id = ?
    """, (pedido_id,))

    itens = cursor.fetchall()
    conn.close()
    return itens

def cancelar_pedido_db(pedido_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE pedidos
        SET status = 'cancelado'
        WHERE id = ?
    """, (pedido_id,))

    conn.commit()
    conn.close()