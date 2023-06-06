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
Vendedor = v.Table_Vendedor(connection)

def atualizar_compra():
    # pede o id da compra
    id_compra = fi.id_compra()
    if not Compra.validate_id(id_compra):
        fp.mensagem_erro_id_invalido()
        return
    
    # mostra as informações da compra
    compra = Compra.read(id_compra)
    fp.info_compra(*compra)
    produtos = Compra_Produto.read_all_from_compra(id_compra)
    fp.info_compra_produtos(produtos)

    # pede ao usuário o que ele quer atualizar
    tabela, coluna, valor = fi.update_compra()

    # chama o método para cada tabela
    deu_ruim = False
    if tabela == 'compra':
        if not Compra.update(id_compra, coluna, valor):
            deu_ruim = True
    elif tabela == 'pagamento':
        if not Pagamento.update(id_compra, coluna, valor):
            deu_ruim = True
    elif tabela == 'produtos':
        # nesse caso, 'coluna' será o id do produto e 'valor' será a quantidade
        if not Compra_Produto.update(id_compra, coluna, valor):
            deu_ruim = True
    
    # imprime mensage de sucesso ou erro
    if deu_ruim:
        fp.mensagem_erro()
        return
    else:
        fp.mensagem_sucesso()
        fp.mensagem_2()
        return

def buscar_compra():
    escolha = fi.opcao_menu_compras_busca()
    while escolha != 0:

        # Por id
        if escolha == 1:
            # Pede o id da compra, valida o id, 
            # puxa os dados pelo id, imprime
            id_compra = fi.id_compra()
            if not Compra.validate_id(id_compra):
                fp.mensagem_erro_id_invalido()
                return
            else:
                compra = Compra.read(id_compra)
                produtos = Compra_Produto.read_all_from_compra(id_compra)
                if not compra or not produtos:
                    fp.mensagem_erro_reinicie()
                    fi.deu_ruim_sair_da_operacao()
                    return
                fp.info_compra(*compra)
                fp.info_compra_produtos(produtos)

        # Por cliente
        elif escolha == 2:
            # Pede o cpf do cliente, pega o id pelo cpf
            # puxa os dados pelo id e imprime
            cpf = fi.cpf_cliente()
            id_cliente = Cliente.return_id(cpf)
            if not id_cliente:
                fp.mensagem_erro_id_invalido()
                return
            else:
                compras = Compra.read_all_from_cliente(id_cliente)
                if not compras:
                    fp.mensagem_erro_reinicie()
                    fi.deu_ruim_sair_da_operacao()
                    return
                fp.info_compras(compras)

        # Por vendedor
        elif escolha == 3:
            # Pede o id do vendedor, valida o id,
            # puxa os dados pelo id e imprime
            id_vendedor = fi.id_vendedor()
            if not Vendedor.validate_id(id_vendedor):
                fp.mensagem_erro_id_invalido()
                return
            else:
                compras = Compra.read_all_from_vendedor(id_vendedor)
                if not compras:
                    fp.mensagem_erro_reinicie()
                    fi.deu_ruim_sair_da_operacao()
                    return
                fp.info_compras(compras)

        # Por data
        elif escolha == 4:
            # Pede a data, não valida mas não tem problema pois é str
            # puxa os dados pela data e imprime
            data = fi.data()
            compras = Compra.read_all_from_data(data)
            if not compras:
                fp.mensagem_erro_reinicie()
                fi.deu_ruim_sair_da_operacao()
                return
            fp.info_compras(compras)

        # Todos
        elif escolha == 5:
            # Puxa todos e imprime, sem segredo
            compras = Compra.read_all()
            if not compras:
                fp.mensagem_erro_reinicie()
                fi.deu_ruim_sair_da_operacao()
                return
            fp.info_compras(compras)

        escolha = fi.opcao_menu_compras_busca()

def cadastrar_produto():
    pass

def cancelar_compra():
    # pede e valida o id
    id_compra = fi.id_compra()
    if not Compra.validate_id(id_compra):
        fp.mensagem_erro_id_invalido()
        return
    
    # mostra as informações da compra
    compra = Compra.read(id_compra)
    fp.info_compra(*compra)
    produtos = Compra_Produto.read_all_from_compra(id_compra)
    fp.info_compra_produtos(produtos)

    # determina se o pagamento será reembolsado ou cancelado
    reembolso = fi.vai_reembolsar_pagamento()

    # cancela ou ou reembolsa o pagamento, a compra e dá alta no estoque
    if not Pagamento.cancel_payment(id_compra):
        fp.mensagem_erro()
        return
    if reembolso:
        if not Pagamento.update(id_compra, 'status_do_pagamento', 'Reembolsado'):
            fp.mensagem_erro()
            return
    
    fp.mensagem_sucesso()
    fp.mensagem_3()

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
        return
    
    # Pegando o id da compra nova
    id_compra = Compra.return_id(*dados)
    if not id_compra:
        fp.mensagem_erro_ao_recuperar_id_compra()
        fi.deu_ruim_sair_da_operacao()
        return
    
    # Adicionando produtos à compra
    # Inserindo na tabela Compra_Produto
    produtos = fi.escolher_produtos(id_compra)
    for produto in produtos:
        if not Compra_Produto.create(*produto):
            fp.mensagem_erro_ao_adicionar_produto()
            fi.deu_ruim_sair_da_operacao()
            return
    
    # Calcula o total e o desconto a serem aplicados
    total = Compra_Produto.return_total_compra(id_compra)
    try:
        desconto = Cliente.return_desconto(id_cliente) * total
    except:
        fp.mensagem_erro_ao_calcular_total()
        fi.deu_ruim_sair_da_operacao()
        return
    
    # Inserindo na tabela Pagamento
    dados_pagamento = (id_compra, total, desconto, 'A definir', 'Pendente')
    if not Pagamento.create(*dados_pagamento):
        fp.mensagem_erro_ao_cadastrar_pagamento()
        fi.deu_ruim_sair_da_operacao()
        return

    # Mostrando as informações do pagamento 
    info_pagamento = Pagamento.read(id_compra)
    fp.info_pagamento(*info_pagamento)

    # Definindo a forma de pagamento e atualizando na tabela
    forma_pagamento = fi.forma_de_pagamento(id_compra)
    if not Pagamento.update(id_compra, 'forma_de_pagamento', forma_pagamento):
        fp.mensagem_erro_ao_cadastrar_pagamento()
        fi.deu_ruim_sair_da_operacao()
        return

    # Definindo o status do pagamento e atualizando na tabela
    if fi.confirmação_do_pagamento():
        if not Pagamento.confirm_payment(id_compra):
            fp.mensagem_erro_ao_cadastrar_pagamento()
            fi.deu_ruim_sair_da_operacao()
            return
    else:
        if not Pagamento.cancel_payment(id_compra):
            fp.mensagem_erro_ao_cadastrar_pagamento()
            fi.deu_ruim_sair_da_operacao()
            return
    
    fp.mensagem_sucesso_compra_nova()
    fp.mensagem_1()