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
Cliente = cl.Table_Cliente(connection)
Compra = cm.Table_Compra(connection)
Compra_Produto = cp.Table_Compra_Produto(connection)
Pagamento = pg.Table_Pagamento(connection)

def nova_compra():

    # Definindo o id do cliente
    # O cliente pode já ter cadastro, se cadastrar, ou não informar dados
    if fi.cliente_vai_dar_dado():
        if fi.cliente_tem_cadastro():
            cpf = fi.cpf_cliente()
            id_cliente = Cliente.return_id(cpf)

            # se o id retornado for 0, o cpf não está cadastrado
            # ou ocorreu um erro na consulta

            while id_cliente == 0:

                # tenta encontrar o cliente novamente, caso seja erro de digitação
                if fi.cpf_nao_encontrado_tentar_novamente():
                    cpf = fi.cpf_cliente()
                    id_cliente = Cliente.return_id(cpf)

                # se não for erro de digitação, encerra a compra nova, para verificar o erro
                else: 
                    fi.deu_ruim_sair_da_operacao()
                    id_cliente = -1
                    return

        # cadastra o cliente        
        else:
            dados = fi.dados_cliente()
            if Cliente.create(*dados):
                fp.mensagem_sucesso_ao_cadastrar_cliente()
            else:
                fp.mensagem_erro_ao_cadastrar_cliente()
                fi.deu_ruim_sair_da_operacao()
                return
            
            cpf = dados[0]
            id_cliente = Cliente.return_id(cpf)

    # se o cliente não quer informar seus dados, é a entrada anônima do banco
    else: 
        id_cliente = Cliente.return_id('0')
    
    # Definindo os outros dados necessários para a compra    
    dados = fi.dados_da_compra(id_cliente)

    # Inserindo na tabela Compra
    if not Compra.create(*dados):
        fp.mensagem_erro_ao_cadastrar_compra()
        fi.deu_ruim_sair_da_operacao()
    
    # Pegando o id da compra nova
    id_compra = Compra.return_id(*dados)
    if not id_compra:
        fp.mensagem_erro_ao_recuperar_id_compra()
        fi.deu_ruim_sair_da_operacao()

    # Adicionando produtos à compra
    # Inserindo na tabela Compra_Produto
    produtos = fi.escolher_produtos(id_compra)
    for produto in produtos:
        if not Compra_Produto.create(*produto):
            fp.mensagem_erro_ao_adicionar_produto()
            fi.deu_ruim_sair_da_operacao()
    
    # Calcula o total e o desconto a serem aplicados
    total = Compra_Produto.return_total_compra(id_compra)
    try:
        desconto = Cliente.return_desconto(id_cliente) * total
    except:
        fp.mensagem_erro_ao_calcular_total()
        fi.deu_ruim_sair_da_operacao()
    
    # Inserindo na tabela Pagamento
    dados_pagamento = (id_compra, total, desconto, 'A definir', 'Pendente')
    if not Pagamento.create(*dados_pagamento):
        fp.mensagem_erro_ao_cadastrar_pagamento()
        fi.deu_ruim_sair_da_operacao()
    
    fp.info_pagamento(id_compra, total, desconto)

    # Definindo a forma de pagamento e atualizando na tabela
    forma_pagamento = fi.forma_de_pagamento(id_compra)
    if not Pagamento.update(id_compra, 'forma_de_pagamento', forma_pagamento):
        fp.mensagem_erro_ao_cadastrar_pagamento()
        fi.deu_ruim_sair_da_operacao()

    # Definindo o status do pagamento e atualizando na tabela
    if fi.confirmação_do_pagamento():
        if not Pagamento.update(id_compra, 'status_do_pagamento', 'Confirmado'):
            fp.mensagem_erro_ao_cadastrar_pagamento()
            fi.deu_ruim_sair_da_operacao()
    else:
        if not Pagamento.update(id_compra, 'status_do_pagamento', 'Cancelado'):
            fp.mensagem_erro_ao_cadastrar_pagamento()
            fi.deu_ruim_sair_da_operacao()