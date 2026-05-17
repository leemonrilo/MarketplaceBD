-- Insercao de CLIENTES (12 registros)
INSERT INTO CLIENTE (nome, cpf, email, telefone, data_nascimento, data_cadastro) VALUES
('Ana Silva', '123.456.789-01', 'ana.silva@email.com', '(86) 91234-5678', '1990-03-15', '2026-05-01'),
('Bruno Costa', '234.567.890-12', 'bruno.costa@email.com', '(86) 92345-6789', '1985-07-22', '2026-05-01'),
('Carla Mendes', '345.678.901-23', 'carla.mendes@email.com', '(86) 93456-7890', '1992-11-08', '2026-05-02'),
('Daniel Oliveira', '456.789.012-34', 'daniel.oliveira@email.com', '(86) 94567-8901', '1988-05-30', '2026-05-02'),
('Elena Souza', '567.890.123-45', 'elena.souza@email.com', '(86) 95678-9012', '1995-09-12', '2026-05-03'),
('Felipe Rocha', '678.901.234-56', 'felipe.rocha@email.com', '(86) 96789-0123', '1982-01-18', '2026-05-03'),
('Gabriela Lima', '789.012.345-67', 'gabriela.lima@email.com', '(86) 97890-1234', '1998-04-25', '2026-05-04'),
('Henrique Alves', '890.123.456-78', 'henrique.alves@email.com', '(86) 98901-2345', '1991-08-07', '2026-05-04'),
('Isabela Ferreira', '901.234.567-89', 'isabela.ferreira@email.com', '(86) 99012-3456', '1993-12-03', '2026-05-05'),
('Joao Pereira', '012.345.678-90', 'joao.pereira@email.com', '(86) 90123-4567', '1987-06-20', '2026-05-05'),
('Guilherme Moraes', '111.222.333-44', 'guiozo.moraes@email.com', '(86) 91234-8765', '1996-02-14', '2026-05-06'),
('Rhuan Douglas', '222.333.444-55', 'rhuan.douglass@email.com', '(86) 92345-9876', '1989-10-28', '2026-05-06');

-- Insercao de VENDEDORES (10 registros)
INSERT INTO VENDEDOR (nome_loja, cnpj, email, telefone, data_cadastro, avaliacao_media) VALUES
('TechStore PI', '12.345.678/0001-90', 'contato@techstore.com', '(86) 3321-1001', '2026-01-15', 4.5),
('Moda Fashion', '23.456.789/0001-01', 'vendas@modafashion.com', '(86) 3321-1002', '2026-01-20', 4.2),
('Eletro Casa', '34.567.890/0001-12', 'suporte@eletrocasa.com', '(86) 3321-1003', '2026-02-01', 4.8),
('Livraria Central', '45.678.901/0001-23', 'atendimento@livrariacentral.com', '(86) 3321-1004', '2026-02-10', 4.0),
('Esportes Total', '56.789.012/0001-34', 'contato@esportestotal.com', '(86) 3321-1005', '2026-02-15', 4.3),
('Beleza Natural', '67.890.123/0001-45', 'vendas@belezanatural.com', '(86) 3321-1006', '2026-03-01', 4.6),
('Mundo Infantil', '78.901.234/0001-56', 'atendimento@mundoinfantil.com', '(86) 3321-1007', '2026-03-10', 4.1),
('Casa e Jardim', '89.012.345/0001-67', 'contato@casaejardim.com', '(86) 3321-1008', '2026-03-20', 4.4),
('Super Eletronicos', '90.123.456/0001-78', 'vendas@supereletronicos.com', '(86) 3321-1009', '2026-04-01', 4.7),
('Pet Shop Amigo', '01.234.567/0001-89', 'contato@petshopamigo.com', '(86) 3321-1010', '2026-04-10', 4.9);

-- Insercao de CATEGORIAS (10 registros)
INSERT INTO CATEGORIA (nome, descricao, id_categoria_pai) VALUES
('Eletronicos', 'Produtos eletronicos e tecnologia', NULL),
('Moda e Vestuario', 'Roupas, calcados e acessorios', NULL),
('Casa e Decoracao', 'Itens para casa e decoracao', NULL),
('Esportes e Lazer', 'Artigos esportivos e lazer', NULL),
('Livros e Papelaria', 'Livros, cadernos e materiais', NULL),
('Celulares', 'Smartphones e acessorios', 1),
('Notebooks', 'Computadores portateis', 1),
('Roupas Femininas', 'Vestuario feminino', 2),
('Roupas Masculinas', 'Vestuario masculino', 2),
('Moveis', 'Moveis para casa', 3);

-- Insercao de PRODUTOS (15 registros)
INSERT INTO PRODUTO (nome, descricao, preco, quantidade_estoque, id_vendedor, id_categoria, data_cadastro) VALUES
('iPhone 15 Pro', 'Smartphone Apple 128GB', 6999.99, 50, 1, 6, '2026-01-20'),
('Samsung Galaxy S24', 'Smartphone Samsung 256GB', 5499.99, 40, 1, 6, '2026-01-25'),
('MacBook Air M3', 'Notebook Apple 13 polegadas', 8999.99, 30, 1, 7, '2026-02-01'),
('Vestido Floral', 'Vestido longo estampado', 189.90, 100, 2, 8, '2026-02-05'),
('Camisa Social', 'Camisa social masculina azul', 129.90, 80, 2, 9, '2026-02-10'),
('Geladeira Frost Free', 'Geladeira 400L Inox', 3499.99, 20, 3, 3, '2026-02-15'),
('Livro Python Avancado', 'Guia completo de Python', 89.90, 200, 4, 5, '2026-02-20'),
('Bicicleta Mountain Bike', 'Bike aro 29 com 21 marchas', 1299.99, 25, 5, 4, '2026-03-01'),
('Kit Maquiagem', 'Kit completo de maquiagem', 199.90, 60, 6, 2, '2026-03-05'),
('Carrinho de Bebe', 'Carrinho compacto e seguro', 899.99, 35, 7, 3, '2026-03-10'),
('Sofa 3 Lugares', 'Sofa retratil e reclinavel', 2499.99, 15, 8, 10, '2026-03-15'),
('Smart TV 55 4K', 'Televisao LED 55 polegadas', 2799.99, 45, 9, 1, '2026-03-20'),
('Racao Premium Caes', 'Racao super premium 15kg', 249.90, 100, 10, 3, '2026-03-25'),
('Tenis Running', 'Tenis esportivo para corrida', 399.99, 70, 5, 4, '2026-04-01'),
('Monitor Gamer 27', 'Monitor 165Hz Full HD', 1499.99, 35, 9, 1, '2026-04-05');

-- Insercao de CARRINHOS (8 registros)
INSERT INTO CARRINHO (id_cliente, data_criacao, data_atualizacao) VALUES
(1, '2026-05-01', '2026-05-10'),
(2, '2026-05-02', '2026-05-11'),
(3, '2026-05-03', '2026-05-12'),
(4, '2026-05-04', '2026-05-13'),
(5, '2026-05-05', '2026-05-14'),
(6, '2026-05-06', '2026-05-15'),
(7, '2026-05-07', '2026-05-16'),
(8, '2026-05-08', '2026-05-17');

-- Insercao de ITENS_CARRINHO (12 registros)
INSERT INTO ITEM_CARRINHO (id_carrinho, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 1, 6999.99),
(1, 3, 1, 8999.99),
(2, 4, 2, 189.90),
(2, 5, 1, 129.90),
(3, 6, 1, 3499.99),
(3, 11, 1, 2499.99),
(4, 7, 3, 89.90),
(5, 8, 1, 1299.99),
(5, 14, 1, 399.99),
(6, 9, 2, 199.90),
(7, 12, 1, 2799.99),
(8, 13, 2, 249.90);

-- Insercao de PEDIDOS (12 registros)
INSERT INTO PEDIDO (id_cliente, data_pedido, status, valor_total, endereco_entrega, frete) VALUES
(1, '2026-05-10', 'entregue', 15999.98, 'Rua das Flores, 123 - Centro, Teresina-PI', 25.00),
(2, '2026-05-11', 'enviado', 509.70, 'Av. Frei Serafim, 456 - Centro, Teresina-PI', 15.00),
(3, '2026-05-12', 'pago', 5999.98, 'Rua Joao XXIII, 789 - Dirceu, Teresina-PI', 30.00),
(4, '2026-05-13', 'entregue', 269.70, 'Av. Marechal Castelo Branco, 321 - Centro, Teresina-PI', 12.00),
(5, '2026-05-14', 'pendente', 1699.98, 'Rua Teresina, 555 - Centro, Teresina-PI', 20.00),
(6, '2026-05-15', 'pago', 399.80, 'Av. Homero Castelo Branco, 777 - Joquei, Teresina-PI', 18.00),
(7, '2026-05-16', 'enviado', 2799.99, 'Rua das Margaridas, 888 - Santa Maria, Teresina-PI', 22.00),
(8, '2026-05-17', 'entregue', 499.80, 'Av. Joao XXIII, 999 - Dirceu, Teresina-PI', 10.00),
(9, '2026-05-18', 'cancelado', 6999.99, 'Rua das Palmeiras, 111 - Centro, Teresina-PI', 25.00),
(10, '2026-05-19', 'entregue', 129.90, 'Av. Frei Serafim, 222 - Centro, Teresina-PI', 15.00),
(11, '2026-05-20', 'pago', 5499.99, 'Rua do Sol, 333 - Fatima, Teresina-PI', 28.00),
(12, '2026-05-21', 'enviado', 8999.99, 'Av. Marechal Deodoro, 444 - Centro, Teresina-PI', 35.00);

-- Insercao de ITENS_PEDIDO (20 registros)
INSERT INTO ITEM_PEDIDO (id_pedido, id_produto, quantidade, preco_unitario, subtotal) VALUES
(1, 1, 1, 6999.99, 6999.99),
(1, 3, 1, 8999.99, 8999.99),
(2, 4, 2, 189.90, 379.80),
(2, 5, 1, 129.90, 129.90),
(3, 6, 1, 3499.99, 3499.99),
(3, 11, 1, 2499.99, 2499.99),
(4, 7, 3, 89.90, 269.70),
(5, 8, 1, 1299.99, 1299.99),
(5, 14, 1, 399.99, 399.99),
(6, 9, 2, 199.90, 399.80),
(7, 12, 1, 2799.99, 2799.99),
(8, 13, 2, 249.90, 499.80),
(9, 1, 1, 6999.99, 6999.99),
(10, 5, 1, 129.90, 129.90),
(11, 2, 1, 5499.99, 5499.99),
(12, 3, 1, 8999.99, 8999.99),
(1, 15, 1, 1499.99, 1499.99),
(3, 12, 1, 2799.99, 2799.99),
(5, 6, 1, 3499.99, 3499.99),
(7, 15, 1, 1499.99, 1499.99);

-- Insercao de PAGAMENTOS (12 registros)
INSERT INTO PAGAMENTO (id_pedido, metodo, status, valor, data_vencimento, data_pagamento) VALUES
(1, 'cartao_credito', 'aprovado', 15999.98, '2026-05-10', '2026-05-10'),
(2, 'pix', 'aprovado', 509.70, '2026-05-11', '2026-05-11'),
(3, 'boleto', 'aprovado', 5999.98, '2026-05-15', '2026-05-13'),
(4, 'cartao_debito', 'aprovado', 269.70, '2026-05-13', '2026-05-13'),
(5, 'cartao_credito', 'pendente', 1699.98, '2026-05-21', NULL),
(6, 'pix', 'aprovado', 399.80, '2026-05-15', '2026-05-15'),
(7, 'boleto', 'aprovado', 2799.99, '2026-05-19', '2026-05-17'),
(8, 'pix', 'aprovado', 499.80, '2026-05-17', '2026-05-17'),
(9, 'cartao_credito', 'cancelado', 6999.99, '2026-05-18', NULL),
(10, 'cartao_debito', 'aprovado', 129.90, '2026-05-19', '2026-05-19'),
(11, 'pix', 'aprovado', 5499.99, '2026-05-20', '2026-05-20'),
(12, 'boleto', 'pendente', 8999.99, '2026-05-26', NULL);

-- Insercao de AVALIACOES (15 registros)
INSERT INTO AVALIACAO (id_cliente, id_produto, id_vendedor, nota, comentario, data_avaliacao) VALUES
(1, 1, 1, 5, 'Produto excelente, chegou rapido!', '2026-05-15'),
(1, 3, 1, 5, 'Notebook incrivel, super leve!', '2026-05-16'),
(2, 4, 2, 4, 'Vestido lindo, mas um pouco grande', '2026-05-18'),
(3, 6, 3, 5, 'Geladeira perfeita, muito silenciosa', '2026-05-20'),
(4, 7, 4, 5, 'Livro muito completo, recomendo!', '2026-05-21'),
(5, 8, 5, 4, 'Bicicleta boa, mas precisa ajustar os freios', '2026-05-22'),
(6, 9, 6, 5, 'Kit maravilhoso, cores lindas!', '2026-05-23'),
(7, 12, 9, 4, 'TV boa, mas a imagem poderia ser melhor', '2026-05-24'),
(8, 13, 10, 5, 'Meu cachorro adorou a racao!', '2026-05-25'),
(9, 1, 1, 3, 'Produto bom, mas demorou a entregar', '2026-05-26'),
(10, 5, 2, 4, 'Camisa de boa qualidade', '2026-05-27'),
(11, 2, 1, 5, 'Galaxy S24 e top!', '2026-05-28'),
(12, 3, 1, 5, 'Melhor notebook que ja tive', '2026-05-29'),
(1, 12, 9, 4, 'Smart TV com otimo custo-beneficio', '2026-05-30'),
(3, 11, 8, 5, 'Sofa muito confortavel!', '2026-05-31');
