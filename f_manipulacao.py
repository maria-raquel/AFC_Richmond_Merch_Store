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
Pagamento = pg.Pagamento(connection)

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
            if Cliente.create(*dados):
                fp.mensagem_sucesso()
            else:
                fp.mensagem_erro()
    else: 
        id_cliente = Cliente.return_id('0')
    
    dados = fi.dados_da_compra(id_cliente)

    if not Compra.create(*dados):
        fp.mensagem_erro()
    
    id_compra = Compra.return_id(*dados)

    produtos = fi.escolher_produtos(id_compra)

    for produto in produtos:
        if not Compra_Produto.create(*produto):
            fp.mensagem_erro()
    
    total = Compra_Produto.return_total_compra(id_compra)
    try:
        desconto = Cliente.return_desconto(id_cliente) * total
    except:
        fp.mensagem_erro()
        desconto = 0
    
    dados_pagamento = (id_compra, total, desconto, 'A definir', 'Pendente')
    if not Pagamento.create(*dados_pagamento):
        fp.mensagem_erro()

    # imprimir informações de pagamento

    forma_pagamento = fi.forma_de_pagamento(id_compra)

    if not Pagamento.update(id_compra, 'forma_de_pagamento', forma_pagamento):
        fp.mensagem_erro()

    # função de confirmação de pagamento

    # atualizar tabela pagamento
    # atualizar tabela compra