INSERT INTO Produto (nome, preco, estoque, categoria, local_de_fabricacao, disponibilidade) VALUES 
('Camiseta Oficial 5 McAdoo Principal', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 6 Kent Principal', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 9 Tartt Principal', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 10 Zava Principal', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 12 Hughes Principal', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 14 Rojas Principal', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 24 Obisanya Principal', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 81 Zoreaux Principal', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 5 McAdoo Secundária', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 6 Kent Secundária', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 9 Tartt Secundária', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 10 Zava Secundária', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 12 Hughes Secundária', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 14 Rojas Secundária', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 24 Obisanya Secundária', 69.99, 60, 'Vestuário', 'Londres', 1),
('Camiseta Oficial 81 Zoreaux Secundária', 69.99, 60, 'Vestuário', 'Londres', 1),
('Cachecol BELIEVE', 19.99, 60, 'Vestuário', 'Londres', 1),
('Cachecol Football is Life', 19.99, 60, 'Vestuário', 'Londres', 1),
('Ursinho Mascote', 5.99, 60, 'Outros', 'Mari', 1);

INSERT INTO Cliente (cpf, nome, is_flamengo, assiste_one_piece, cidade_natal) VALUES
('47586947582', 'Mae', 1, 0, 'Londres'),
('12345678910', 'Baz', 0, 1, 'São Paulo'),
('98765432101', 'Jeremy', 1, 1, 'Rio de Janeiro'),
('45678912302', 'Paul', 0, 0, 'Belo Horizonte'),
('13579246803', 'Jade', 1, 0, 'Salvador'),
('24681357904', 'Barbara', 0, 1, 'Recife'),
('98765432105', 'Shand', 1, 1, 'Fortaleza'),
('25836914706', 'Jack', 0, 0, 'Porto Alegre'),
('36925814707', 'Carla Fernandes', 1, 0, 'Brasília'),
('65498732108', 'Fernando Silva', 0, 1, 'Curitiba'),
('78965412309', 'Juliana Almeida', 1, 1, 'Manaus'),
('98765432110', 'Rafaela Rodrigues', 0, 0, 'Belém'),
('15975385211', 'Marcos Santos', 1, 0, 'Natal'),
('75315985212', 'Camila Oliveira', 0, 1, 'Vitória'),
('85236974123', 'Gabriel Pereira', 1, 1, 'Maceió'),
('65478932124', 'Isabela Costa', 0, 0, 'Goiania'),
('75395145625', 'Lucas Mendes', 1, 0, 'Porto Velho'),
('85274196326', 'Sandra Fernandes', 0, 1, 'Teresina'),
('96385274127', 'Rodrigo Silva', 1, 1, 'Florianópolis'),
('78945612328', 'Patricia Almeida', 0, 0, 'Cuiabá');

INSERT INTO Vendedor (cpf, nome, situacao) VALUES
('71829346582', 'Antonio Carvalho',  'Ativo')
('00011122233', 'Maria Souza', 'Ativo')
('12398745600', 'Phoebe Kent', 'De férias');

-- Mes de Maio de 2023
INSERT INTO compra (id_cliente, id_vendedor, data_da_compra, status_da_compra) VALUES 
(32, 10, '2023-05-01', 'Confirmada'),
(33, 11, '2023-05-02', 'Confirmada'),
(35, 10, '2023-05-04', 'Confirmada'),
(36, 11, '2023-05-05', 'Confirmada'),
(38, 10, '2023-05-07', 'Confirmada'),
(40, 12, '2023-05-09', 'Confirmada'),
(41, 10, '2023-05-10', 'Confirmada'),
(44, 10, '2023-05-13', 'Confirmada'),
(46, 12, '2023-05-15', 'Confirmada'),
(47, 10, '2023-05-16', 'Confirmada'),
(49, 12, '2023-05-18', 'Confirmada'),
(50, 10, '2023-05-19', 'Confirmada'),
(52, 12, '2023-05-21', 'Confirmada'),
(32, 10, '2023-05-22', 'Confirmada'),
(33, 11, '2023-05-23', 'Confirmada'),
(35, 10, '2023-05-25', 'Confirmada'),
(36, 11, '2023-05-26', 'Confirmada'),
(38, 10, '2023-05-28', 'Confirmada'),
(40, 12, '2023-05-30', 'Confirmada');

INSERT INTO Produto_Compra (id_compra, id_produto, quantidade) VALUES
(53, 29, 2),
(54, 30, 5),
(55, 31, 1),
(56, 32, 3),
(57, 33, 4),
(58, 34, 2),
(59, 35, 1),
(60, 36, 3),
(61, 37, 2),
(62, 38, 5),
(63, 39, 1),
(64, 40, 4),
(65, 41, 2),
(66, 42, 3),
(67, 43, 1),
(68, 44, 5),
(69, 45, 2),
(70, 46, 3),
(71, 47, 1);

INSERT INTO Pagamento (id_compra, total, desconto_aplicado, forma_de_pagamento, status_do_pagamento) VALUES
(53, 0, 0, 'Pix', 'Confirmado'),
(54, 0, 0, 'Cartão de Crédito', 'Confirmado'),
(55, 0, 0, 'Dinheiro', 'Confirmado'),
(56, 0, 0, 'Cartão de Débito', 'Confirmado'),
(57, 0, 0, 'Pix', 'Confirmado'),
(58, 0, 0, 'Cartão de Crédito', 'Confirmado'),
(59, 0, 0, 'Dinheiro', 'Confirmado'),
(60, 0, 0, 'Cartão de Débito', 'Confirmado'),
(61, 0, 0, 'Pix', 'Confirmado'),
(62, 0, 0, 'Cartão de Crédito', 'Confirmado'),
(63, 0, 0, 'Dinheiro', 'Confirmado'),
(64, 0, 0, 'Cartão de Débito', 'Confirmado'),
(65, 0, 0, 'Pix', 'Confirmado'),
(66, 0, 0, 'Cartão de Crédito', 'Confirmado'),
(67, 0, 0, 'Dinheiro', 'Confirmado'),
(68, 0, 0, 'Cartão de Débito', 'Confirmado'),
(69, 0, 0, 'Pix', 'Confirmado'),
(70, 0, 0, 'Cartão de Crédito', 'Confirmado'),
(71, 0, 0, 'Dinheiro', 'Confirmado');

-- COMANDOS PARA CALCULAR TOTAL E DESCONTO DESSAS COMPRAS

UPDATE ((pagamento INNER JOIN produto_compra ON pagamento.id_compra = produto_compra.id_compra) 
                   INNER JOIN produto ON produto_compra.id_produto = produto.id)
SET pagamento.total = produto_compra.quantidade * produto.preco 
WHERE pagamento.id_compra < 100

UPDATE ((pagamento INNER JOIN compra ON pagamento.id_compra = compra.id)
				   INNER JOIN cliente ON compra.id_cliente = cliente.id) 
SET pagamento.desconto_aplicado = total * 10/100
WHERE cliente.is_flamengo = 1 OR cliente.cidade_natal = 'Sousa' OR cliente.assiste_one_piece = 1



UPDATE ((pagamento INNER JOIN compra ON pagamento.id_compra = compra.id)
				   INNER JOIN cliente ON compra.id_cliente = cliente.id) 
SET pagamento.desconto_aplicado = total * 20/100
WHERE (cliente.is_flamengo = 1 AND cliente.cidade_natal = 'Sousa') 
   OR (cliente.assiste_one_piece = 1 AND cliente.cidade_natal = 'Sousa')
   OR (cliente.is_flamengo = 1 AND cliente.assiste_one_piece = 1)


UPDATE ((pagamento INNER JOIN compra ON pagamento.id_compra = compra.id)
				   INNER JOIN cliente ON compra.id_cliente = cliente.id) 
SET pagamento.desconto_aplicado = total * 30/100
WHERE cliente.is_flamengo = 1 AND cliente.cidade_natal = 'Sousa' AND cliente.assiste_one_piece = 1