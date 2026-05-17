try:
    import mysql.connector
    from mysql.connector import Error
except ImportError:
    print("Error: mysql-connector-python is not installed. Install it using: pip install mysql-connector-python")
    exit(1)

def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='marketplace_db',
            user='root',
            password='Muriloanbu72'
        )
        if conexao.is_connected():
            print('Conexao estabelecida com sucesso!')
            return conexao
    except Error as e:
        print(f'Erro ao conectar: {e}')
        return None

def executar_consulta(conexao, query):
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except Error as e:
        print(f'Erro na consulta: {e}')
        return None

def exibir_produtos(conexao):
    query = "SELECT p.nome, p.preco, p.quantidade_estoque, v.nome_loja, c.nome AS categoria FROM PRODUTO p JOIN VENDEDOR v ON p.id_vendedor = v.id_vendedor LEFT JOIN CATEGORIA c ON p.id_categoria = c.id_categoria ORDER BY p.preco DESC"
    resultados = executar_consulta(conexao, query)
    if resultados:
        print("LISTA DE PRODUTOS - MARKETPLACE")
        for produto in resultados:
            print(f"Produto: {produto['nome']}")
            print(f"Preco: R$ {produto['preco']}")
            print(f"Estoque: {produto['quantidade_estoque']} unidades")
            print(f"Vendedor: {produto['nome_loja']}")
            print(f"Categoria: {produto['categoria']}")
            print("-" * 40)

def exibir_pedidos_cliente(conexao, id_cliente):
    query = f"SELECT p.id_pedido, p.data_pedido, p.status, p.valor_total, pg.metodo FROM PEDIDO p JOIN PAGAMENTO pg ON p.id_pedido = pg.id_pedido WHERE p.id_cliente = {id_cliente} ORDER BY p.data_pedido DESC"
    resultados = executar_consulta(conexao, query)
    if resultados:
        print(f"PEDIDOS DO CLIENTE {id_cliente}")
        for pedido in resultados:
            print(f"Pedido #{pedido['id_pedido']} - {pedido['data_pedido']}")
            print(f"Status: {pedido['status']} | Valor: R$ {pedido['valor_total']}")
            print(f"Pagamento: {pedido['metodo']}")
            print("-" * 40)

if __name__ == '__main__':
    conexao = conectar_banco()
    if conexao:
        exibir_produtos(conexao)
        exibir_pedidos_cliente(conexao, 1)
        conexao.close()
        print('Conexao encerrada.')