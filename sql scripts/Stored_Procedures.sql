DELIMITER $$
CREATE PROCEDURE Confirmacao (IN id_da_compra INT)
BEGIN

UPDATE Pagamento
SET status_do_pagamento = "Confirmado"
WHERE id_compra = id_da_compra

UPDATE Compra 
SET status_da_compra = "Confirmada"
WHERE id = id_da_compra

END $$
DELIMITER ;