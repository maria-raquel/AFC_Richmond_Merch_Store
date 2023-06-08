-- View usada para facilitar a alta e baixa de estoque
-- Mostra a quantidade de um produto em uma compra e o estoque atual do produto
CREATE VIEW Modificar_Estoque AS
SELECT Produto_Compra.id_compra AS id_compra,
Produto_Compra.id_produto AS id_produto,
Produto_Compra.quantidade AS quantidade,
Produto.estoque AS estoque
FROM Produto INNER JOIN Produto_Compra
ON Produto.id = Produto_Compra.id_produto;


-- Chamado ao confirmar uma compra nova
DELIMITER $$
CREATE PROCEDURE Confirmar_compra (IN id_da_compra INT)
BEGIN

UPDATE Pagamento
SET status_do_pagamento = "Confirmado"
WHERE id_compra = id_da_compra;

UPDATE Compra 
SET status_da_compra = "Confirmada"
WHERE id = id_da_compra;

UPDATE modificar_estoque SET estoque = estoque - quantidade
WHERE id_compra = id_da_compra;

END $$
DELIMITER ;


-- Chamado ao cancelar um pagamento que não chegou a ser confirmado
-- Ou seja, não ocorreu baixa de mercadoria
DELIMITER $$
CREATE PROCEDURE Cancelar_compra (IN id_da_compra INT)
BEGIN

UPDATE Pagamento
SET status_do_pagamento = "Cancelado"
WHERE id_compra = id_da_compra;

UPDATE Compra 
SET status_da_compra = "Cancelada"
WHERE id = id_da_compra;

END $$
DELIMITER ;


-- Chamado ao cancelar um pagamento que estava confirmado
DELIMITER $$
CREATE PROCEDURE Reembolsar_compra (IN id_da_compra INT)
BEGIN

UPDATE Pagamento
SET status_do_pagamento = "Reembolsado"
WHERE id_compra = id_da_compra;

UPDATE Compra 
SET status_da_compra = "Cancelada"
WHERE id = id_da_compra;

UPDATE modificar_estoque SET estoque = estoque + quantidade
WHERE id_compra = id_da_compra;

END $$
DELIMITER ;


-- View usada para mostrar todas as informações de uma compra e seu pagamento
CREATE VIEW compra_com_pagamento AS
SELECT Compra.id AS id, Compra.id_cliente AS id_cliente, Compra.id_vendedor As id_vendedor, 
Compra.data_da_compra AS data_da_compra, Compra.status_da_compra AS status_da_compra, 
Pagamento.total AS total, Pagamento.desconto_aplicado AS desconto_aplicado, 
Pagamento.total_pos_desconto AS total_pos_desconto, Pagamento.forma_de_pagamento AS forma_de_pagamento, 
Pagamento.status_do_pagamento AS status_do_pagamento 
FROM Compra INNER JOIN Pagamento ON Compra.id = Pagamento.id_compra


-- Chamado para apagar um cliente do sistema
DELIMITER $$
CREATE PROCEDURE Apagar_cliente (IN id_a_apagar INT)
BEGIN

UPDATE Compra
SET id_cliente = (SELECT id FROM cliente WHERE cpf = '0')
WHERE id_cliente = id_a_apagar;

DELETE FROM Cliente WHERE id = id_a_apagar;

END $$
DELIMITER ;