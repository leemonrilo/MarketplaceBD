import mysql.connector
from mysql.connector import Error
from tabulate import tabulate


CONFIG_BD = {
    'host': 'localhost',
    'database': 'marketplace_db',
    'user': '',      # Altere para seu usuario MySQL
    'password': ''     # Altere para sua senha MySQL
}


def conectar_banco():
    """Estabelece conexao com o banco de dados MySQL."""
    try:
        conexao = mysql.connector.connect(**CONFIG_BD)
        if conexao.is_connected():
            print("Conexao estabelecida com sucesso!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def executar_consulta(conexao, query):
    """Executa uma consulta SELECT e retorna os resultados."""
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except Error as e:
        print(f"Erro na consulta: {e}")
        return None

def exibir_resultados(resultados, titulo):
    """Exibe os resultados em formato de tabela."""
    if not resultados:
        print("Nenhum resultado encontrado.")
        return

    print(f"{'='*60}")
    print(f"RESULTADO: {titulo}")
    print(f"{'='*60}")

    headers = resultados[0].keys()
    rows = [list(r.values()) for r in resultados]
    print(tabulate(rows, headers=headers, tablefmt='grid', stralign='left'))

    print(f"Total de registros: {len(resultados)}")
    print(f"{'='*60}")

def consulta_1_in(conexao):
    """Consulta 1 - IN: Produtos de categorias especificas"""
    query = """
        SELECT p.nome, p.preco, c.nome AS categoria
        FROM PRODUTO p
        JOIN CATEGORIA c ON p.id_categoria = c.id_categoria
        WHERE c.nome IN ('Celulares', 'Notebooks', 'Eletronicos')
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "IN - Produtos de categorias especificas")

def consulta_2_not_in(conexao):
    """Consulta 2 - NOT IN: Clientes que nao fizeram pedidos"""
    query = """
        SELECT nome, email, data_cadastro
        FROM CLIENTE
        WHERE id_cliente NOT IN (
            SELECT DISTINCT id_cliente FROM PEDIDO
        )
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "NOT IN - Clientes que nao fizeram pedidos")

def consulta_3_between(conexao):
    """Consulta 3 - BETWEEN: Pedidos com valor entre R$500 e R$3000"""
    query = """
        SELECT id_pedido, valor_total, status, data_pedido
        FROM PEDIDO
        WHERE valor_total BETWEEN 500 AND 3000
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "BETWEEN - Pedidos com valor entre R$500 e R$3000")

def consulta_4_operadores(conexao):
    """Consulta 4 - Operadores >= e <=: Produtos com preco a partir de R$1.000 e estoque <= 50"""
    query = """
        SELECT nome, preco, quantidade_estoque
        FROM PRODUTO
        WHERE preco >= 1000 AND quantidade_estoque <= 50
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "Operadores >= e <= - Produtos caros com estoque baixo")

def consulta_5_and_or(conexao):
    """Consulta 5 - AND e OR: Pedidos pendentes ou pagos com valor alto"""
    query = """
        SELECT id_pedido, status, valor_total, data_pedido
        FROM PEDIDO
        WHERE (status = 'pendente' OR status = 'pago') AND valor_total > 1000
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "AND e OR - Pedidos pendentes ou pagos com valor alto")

def consulta_6_limit(conexao):
    """Consulta 6 - LIMIT: Top 5 produtos mais caros"""
    query = """
        SELECT nome, preco, quantidade_estoque
        FROM PRODUTO
        ORDER BY preco DESC
        LIMIT 5
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "LIMIT - Top 5 produtos mais caros")

def consulta_7_count(conexao):
    """Consulta 7 - COUNT: Total de pedidos por status"""
    query = """
        SELECT status, COUNT(*) AS total_pedidos
        FROM PEDIDO
        GROUP BY status
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "COUNT - Total de pedidos por status")

def consulta_8_sum(conexao):
    """Consulta 8 - SUM: Valor total de vendas por vendedor"""
    query = """
        SELECT v.nome_loja, SUM(ip.subtotal) AS total_vendas
        FROM VENDEDOR v
        JOIN PRODUTO p ON v.id_vendedor = p.id_vendedor
        JOIN ITEM_PEDIDO ip ON p.id_produto = ip.id_produto
        GROUP BY v.id_vendedor, v.nome_loja
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "SUM - Valor total de vendas por vendedor")

def consulta_9_min_max(conexao):
    """Consulta 9 - MIN, MAX e AVG: Preco minimo, maximo e medio dos produtos"""
    query = """
        SELECT 
            MIN(preco) AS preco_minimo,
            MAX(preco) AS preco_maximo,
            AVG(preco) AS preco_medio
        FROM PRODUTO
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "MIN, MAX e AVG - Estatisticas de precos")


def consulta_10_group_by(conexao):
    """Consulta 10 - GROUP BY e ORDER BY: Media de avaliacoes por vendedor"""
    query = """
        SELECT 
            v.nome_loja,
            AVG(a.nota) AS media_avaliacao,
            COUNT(a.id_avaliacao) AS total_avaliacoes
        FROM VENDEDOR v
        LEFT JOIN AVALIACAO a ON v.id_vendedor = a.id_vendedor
        GROUP BY v.id_vendedor, v.nome_loja
        ORDER BY media_avaliacao DESC
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "GROUP BY e ORDER BY - Media de avaliacoes por vendedor")



def consulta_11_inner_join(conexao):
    """Consulta 11 - INNER JOIN: Detalhes completos dos pedidos"""
    query = """
        SELECT 
            p.id_pedido,
            c.nome AS cliente,
            p.data_pedido,
            p.status,
            p.valor_total,
            pg.metodo AS forma_pagamento
        FROM PEDIDO p
        INNER JOIN CLIENTE c ON p.id_cliente = c.id_cliente
        INNER JOIN PAGAMENTO pg ON p.id_pedido = pg.id_pedido
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "INNER JOIN - Detalhes completos dos pedidos")

def consulta_12_left_join(conexao):
    """Consulta 12 - LEFT JOIN: Todos os clientes e seus pedidos"""
    query = """
        SELECT 
            c.nome,
            c.email,
            p.id_pedido,
            p.valor_total,
            p.status
        FROM CLIENTE c
        LEFT JOIN PEDIDO p ON c.id_cliente = p.id_cliente
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "LEFT JOIN - Todos os clientes e seus pedidos")

def consulta_13_right_join(conexao):
    """Consulta 13 - RIGHT JOIN: Todos os produtos e seus itens de pedido"""
    query = """
        SELECT 
            p.nome AS produto,
            p.preco,
            ip.id_pedido,
            ip.quantidade
        FROM ITEM_PEDIDO ip
        RIGHT JOIN PRODUTO p ON ip.id_produto = p.id_produto
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "RIGHT JOIN - Todos os produtos e itens de pedido")


def consulta_14_union(conexao):
    """Consulta 14 - UNION: Emails de clientes e vendedores ativos"""
    query = """
        SELECT nome, email, 'Cliente' AS tipo
        FROM CLIENTE
        WHERE status = 'ativo'
        UNION
        SELECT nome_loja AS nome, email, 'Vendedor' AS tipo
        FROM VENDEDOR
        WHERE status = 'ativo'
        ORDER BY tipo, nome
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "UNION - Emails de clientes e vendedores ativos")

def consulta_15_union_all(conexao):
    """Consulta 15 - UNION ALL: Todos os registros de pagamentos"""
    query = """
        SELECT 
            id_pagamento, id_pedido, metodo, status, valor,
            'APROVADO' AS situacao
        FROM PAGAMENTO
        WHERE status = 'aprovado'
        UNION ALL
        SELECT 
            id_pagamento, id_pedido, metodo, status, valor,
            'PENDENTE' AS situacao
        FROM PAGAMENTO
        WHERE status = 'pendente'
        ORDER BY valor DESC
    """
    resultados = executar_consulta(conexao, query)
    exibir_resultados(resultados, "UNION ALL - Todos os registros de pagamentos")


def exibir_menu():
    """Exibe o menu de opcoes."""
    print("" + "="*70)
    print("SISTEMA DE CONSULTAS - MARKETPLUS")
    print("="*70)
    print("3.8.1 PARAMETROS DE SELECAO:")
    print("  [1]  IN      - Produtos de categorias especificas")
    print("  [2]  NOT IN  - Clientes que nao fizeram pedidos")
    print("  [3]  BETWEEN - Pedidos com valor entre R$500 e R$3000")
    print("  [4]  >= <=   - Produtos caros com estoque baixo")
    print("  [5]  AND OR  - Pedidos pendentes ou pagos com valor alto")
    print("  [6]  LIMIT   - Top 5 produtos mais caros")
    print("3.8.2 FUNCOES DE AGREGACAO:")
    print("  [7]  COUNT   - Total de pedidos por status")
    print("  [8]  SUM     - Valor total de vendas por vendedor")
    print("  [9]  MIN MAX - Preco minimo, maximo e medio")
    print("3.8.3 AGRUPAMENTO E ORDENACAO:")
    print("  [10] GROUP BY - Media de avaliacoes por vendedor")
    print("3.8.4 FUNCOES DE JUNCAO:")
    print("  [11] INNER JOIN - Detalhes completos dos pedidos")
    print("  [12] LEFT JOIN  - Todos os clientes e seus pedidos")
    print("  [13] RIGHT JOIN - Todos os produtos e itens de pedido")
    print("3.8.5 FUNCAO DE UNIAO:")
    print("  [14] UNION     - Emails de clientes e vendedores ativos")
    print("  [15] UNION ALL - Todos os registros de pagamentos")
    print("OUTRAS OPCOES:")
    print("  [T]  Executar TODAS as consultas sequencialmente")
    print("  [S]  Sair")
    print("="*70)

def executar_todas(conexao):
    """Executa todas as 15 consultas em sequencia."""
    consultas = [
        consulta_1_in, consulta_2_not_in, consulta_3_between,
        consulta_4_operadores, consulta_5_and_or, consulta_6_limit,
        consulta_7_count, consulta_8_sum, consulta_9_min_max,
        consulta_10_group_by, consulta_11_inner_join,
        consulta_12_left_join, consulta_13_right_join,
        consulta_14_union, consulta_15_union_all
    ]

    for i, consulta in enumerate(consultas, 1):
        print(f"{'#'*70}")
        print(f"EXECUTANDO CONSULTA {i} DE 15")
        print(f"{'#'*70}")
        consulta(conexao)
        input("Pressione Enter para continuar...")

def main():
    """Funcao principal."""
    print("Iniciando Sistema de Consultas MarketPlus...")

    conexao = conectar_banco()
    if not conexao:
        print("Nao foi possivel conectar ao banco de dados.")
        print("Verifique as configuracoes em CONFIG_BD no inicio do script.")
        return

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip().upper()

        if opcao == 'S':
            print("Saindo do sistema. Ate logo!")
            break
        elif opcao == 'T':
            executar_todas(conexao)
        elif opcao == '1':
            consulta_1_in(conexao)
        elif opcao == '2':
            consulta_2_not_in(conexao)
        elif opcao == '3':
            consulta_3_between(conexao)
        elif opcao == '4':
            consulta_4_operadores(conexao)
        elif opcao == '5':
            consulta_5_and_or(conexao)
        elif opcao == '6':
            consulta_6_limit(conexao)
        elif opcao == '7':
            consulta_7_count(conexao)
        elif opcao == '8':
            consulta_8_sum(conexao)
        elif opcao == '9':
            consulta_9_min_max(conexao)
        elif opcao == '10':
            consulta_10_group_by(conexao)
        elif opcao == '11':
            consulta_11_inner_join(conexao)
        elif opcao == '12':
            consulta_12_left_join(conexao)
        elif opcao == '13':
            consulta_13_right_join(conexao)
        elif opcao == '14':
            consulta_14_union(conexao)
        elif opcao == '15':
            consulta_15_union_all(conexao)
        else:
            print("Opcao invalida! Tente novamente.")

        if opcao != 'T':
            input("Pressione Enter para voltar ao menu...")

    if conexao.is_connected():
        conexao.close()
        print("Conexao com o banco de dados encerrada.")

if __name__ == "__main__":
    main()
