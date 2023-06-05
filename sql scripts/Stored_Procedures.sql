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