import connect_to_DB
import t_cliente as cl
import t_compra_produto as cp
import t_compra as cm
import t_produto as p
import t_vendedor as v
import t_pagamento as pg
import f_input as fi
import f_print as fp

connection = connect_to_DB.connect()
Cliente = cl.Cliente(connection)
Compra = cm.Compra(connection)
Compra_Produto = cp.Compra_Produto(connection)

def nova_compra():
    if fi.cliente_vai_dar_dado():
        if fi.cliente_tem_cadastro():
            cpf = fi.cpf_cliente()
            id_cliente = Cliente.return_id(cpf)

            while id_cliente == 0:
                fp.mensagem_erro()
                cpf = fi.cpf_cliente()
                id_cliente = Cliente.return_id(cpf)
        else:
            dados = fi.dados_cliente()
            if Cliente.insert(*dados):
                fp.mensagem_sucesso()
            else:
                fp.mensagem_erro()
    else: 
        id_cliente = Cliente.return_id('0')
    
    dados = fi.dados_da_compra(id_cliente)

    if not Compra.insert(*dados):
        fp.mensagem_erro()
    
    id_compra = Compra.return_id(*dados)

    produtos = fi.produtos_da_compra(id_compra)

    for produto in produtos:
        if not Compra_Produto.insert(*produto):
            fp.mensagem_erro()
    
    # calcular total da compra
    # inserir na tabela pagamento
    # pedir informação de pagamento
    # atualizar tabela pagamento
    # atualizar tabela compra