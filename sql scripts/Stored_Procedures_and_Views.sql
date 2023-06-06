CREATE VIEW Modificar_Estoque AS
SELECT Produto_Compra.id_compra AS id_compra,
Produto_Compra.id_produto AS id_produto,
Produto_Compra.quantidade AS quantidade,
Produto.estoque AS estoque
FROM Produto INNER JOIN Produto_Compra
ON Produto.id = Produto_Compra.id_produto;



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



DELIMITER $$
CREATE PROCEDURE Cancelar_compra (IN id_da_compra INT)
BEGIN

UPDATE Pagamento
SET status_do_pagamento = "Cancelado"
WHERE id_compra = id_da_compra;

UPDATE Compra 
SET status_da_compra = "Cancelada"
WHERE id = id_da_compra;

UPDATE modificar_estoque SET estoque = estoque + quantidade
WHERE id_compra = id_da_compra;

END $$
DELIMITER ;



DELIMITER $$
CREATE PROCEDURE Cancelar_compra_pendente (IN id_da_compra INT)
BEGIN

UPDATE Pagamento
SET status_do_pagamento = "Cancelado"
WHERE id_compra = id_da_compra;

UPDATE Compra 
SET status_da_compra = "Cancelada"
WHERE id = id_da_compra;

END $$
DELIMITER ;



CREATE VIEW compra_com_pagamento AS
SELECT Compra.id AS id, Compra.id_cliente AS id_cliente, Compra.id_vendedor As id_vendedor, 
Compra.data_da_compra AS data_da_compra, Compra.status_da_compra AS status_da_compra, 
Pagamento.total AS total, Pagamento.desconto_aplicado AS desconto_aplicado, 
Pagamento.total_pos_desconto AS total_pos_desconto, Pagamento.forma_de_pagamento AS forma_de_pagamento, 
Pagamento.status_do_pagamento AS status_do_pagamento 
FROM Compra INNER JOIN Pagamento ON Compra.id = Pagamento.id_compra