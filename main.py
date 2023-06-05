import connect_to_DB
import t_cliente as cl
import t_compra_produto as cp
import t_compra as cm
import t_produto as p
import t_vendedor as v
import t_pagamento as pg
import f_input as fi
import f_print as fp
import f_manipulacao as fm

connection = connect_to_DB.connect()

Cliente = cl.Table_Cliente(connection)
Vendedor = v.Table_Vendedor(connection)
Produto = p.Table_Produto(connection)
Compra = cm.Table_Compra(connection)
Compra_Produto = cp.Table_Compra_Produto(connection)
Pagamento = pg.Table_Pagamento(connection)

fm.nova_compra()