import connect_to_DB
import t_cliente as cl
import t_compra_produto as cp
import t_compra as cm
import t_produto as p
import t_vendedor as v
import t_pagamento as pg
import f_input as fi
import f_print as fp
import f_relatorio as fr

connection = connect_to_DB.connect()
Cliente = cl.Table_Cliente(connection)
Compra = cm.Table_Compra(connection)
Compra_Produto = cp.Table_Compra_Produto(connection)
Pagamento = pg.Table_Pagamento(connection)
Vendedor = v.Table_Vendedor(connection)
Produto = p.Table_Produto(connection)

def apagar_cliente():
    id = fi.pedir_id()
    if not Cliente.validate_id(id):
        fp.mensagem_erro_id_invalido()
        return
    
    cliente = Cliente.read_by_id(id)
    fp.info_cliente(*cliente)

    if not fi.tem_certeza():
        return

    if not Cliente.delete(id):
        fp.mensagem_erro()
        return
    
    fp.mensagem_sucesso()
    fp.mensagem_2()

def atualizar_cliente():
    id = fi.pedir_id()
    if not Cliente.validate_id(id):
        fp.mensagem_erro_id_invalido()
        return
    
    cliente = Cliente.read_by_id(id)
    fp.info_cliente(*cliente)

    coluna, valor = fi.update_cliente()

    if not Cliente.update(id, coluna, valor):
        fp.mensagem_erro()
        return
    
    fp.mensagem_sucesso()
    fp.mensagem_2()

def atualizar_compra():
    # pede o id da compra
    id_compra = fi.pedir_id()
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
    if tabela == 'c':
        if not Compra.update(id_compra, coluna, valor):
            deu_ruim = True
    elif tabela == 'p':
        if not Pagamento.update(id_compra, coluna, valor):
            deu_ruim = True
    
    # imprime mensage de sucesso ou erro
    if deu_ruim:
        fp.mensagem_erro()
        return
    else:
        fp.mensagem_sucesso()
        fp.mensagem_2()
        return

def atualizar_produto():
    id = fi.pedir_id()
    if not Produto.validate_id(id):
        fp.mensagem_erro_id_invalido()
        return
    
    produto = Produto.read_by_id(id)
    fp.info_produto(*produto)

    coluna, valor = fi.update_produto()

    if not Produto.update(id, coluna, valor):
        fp.mensagem_erro()
        return
    
    fp.mensagem_sucesso()
    fp.mensagem_1()

def atualizar_vendedor():
    id = fi.pedir_id()
    if not Vendedor.validate_id(id):
        fp.mensagem_erro_id_invalido()
        return
    
    info = Vendedor.read_by_id(id)
    fp.info_vendedor(*info)

    coluna, valor = fi.update_vendedor()

    if not Vendedor.update(id, coluna, valor):
        fp.mensagem_erro()
        return
    
    fp.mensagem_sucesso()
    fp.mensagem_3()

def buscar_cliente():
    escolha = fi.opcao_menu_cliente_busca()
    while escolha != '0':

        # Por id
        if escolha == '1':
            id = fi.pedir_id()
            if not Cliente.validate_id(id):
                fp.mensagem_erro_id_invalido()
                return
            info = Cliente.read_by_id(id)
            if not info:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_cliente(*info)

        # Por nome
        elif escolha == '2':
            nome = fi.nome()
            clientes = Cliente.read_by_name(nome)
            if clientes == 0:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_clientes(clientes)

        # Por cpf
        elif escolha == '3':
            cpf = fi.pedir_cpf()
            info = Cliente.read_by_cpf(cpf)
            if not info:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_cliente(*info)

        # Todos
        elif escolha == '4':
            clientes = Cliente.read_all()
            if clientes == 0:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_clientes(clientes)
        
        escolha = fi.opcao_menu_cliente_busca()

def buscar_compra():
    escolha = fi.opcao_menu_compras_busca()
    while escolha != '0':

        # Por id
        if escolha == '1':
            id_compra = fi.pedir_id()
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
        elif escolha == '2':
            cpf = fi.pedir_cpf()
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
        elif escolha == '3':
            id_vendedor = fi.pedir_id()
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
        elif escolha == '4':
            data = fi.data()
            compras = Compra.read_all_from_data(data)
            if not compras:
                fp.mensagem_erro_reinicie()
                fi.deu_ruim_sair_da_operacao()
                return
            fp.info_compras(compras)

        # Todos
        elif escolha == '5':
            compras = Compra.read_all()
            if not compras:
                fp.mensagem_erro_reinicie()
                fi.deu_ruim_sair_da_operacao()
                return
            fp.info_compras(compras)

        escolha = fi.opcao_menu_compras_busca()

def buscar_produto():
    escolha = fi.opcao_menu_produto_busca()

    while escolha != '0':
        # Por id
        if escolha == '1':
            id = fi.pedir_id()
            if not Produto.validate_id(id):
                fp.mensagem_erro_id_invalido()
                return
            info = Produto.read_by_id(id)
            if not info:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_produto(*info)

        # Por nome
        elif escolha == '2':
            nome = fi.pedir_nome()
            info = Produto.read_by_name(nome)
            if info == 0:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_produtos(info)

        # Por categoria
        elif escolha == '3':
            categoria = fi.categoria()
            if categoria == 'v':
                produtos = Produto.read_by_category('Vestuário')
            elif categoria == 'o':
                produtos = Produto.read_by_category('Outros')
            if not produtos:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_produtos(produtos)

        # Por local de fabricação
        elif escolha == '4':
            local = fi.local_de_fabricacao()
            info = Produto.read_by_local(local)
            if not info:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_produtos(info)

        # Por faixa de preço
        elif escolha == '5':
            faixa = fi.faixa_de_preco()
            produtos = Produto.read_by_price(*faixa)
            if not produtos:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_produtos(produtos)

        # Todos
        elif escolha == '6':
            if fi.apenas_disponiveis():
                produtos = Produto.read_all()
            else:
                produtos = Produto.read_all_available()
                
            if not produtos:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_produtos(produtos)

        escolha = fi.opcao_menu_produto_busca()

def buscar_vendedor():
    escolha = fi.opcao_menu_vendedor_busca()

    while escolha != '0':
        # Por id
        if escolha == '1':
            id = fi.pedir_id()
            if not Vendedor.validate_id(id):
                fp.mensagem_erro_id_invalido()
                return
            info = Vendedor.read_by_id(id)
            if not info:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_vendedor(*info)

        # Por nome
        elif escolha == '2':
            nome = fi.pedir_nome()
            vendedores = Vendedor.read_by_name(nome)
            if vendedores == 0:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_vendedores(vendedores)

        # Todos
        elif escolha == '3':
            if fi.apenas_disponiveis():
                vendedores = Vendedor.read_all_active()
            else:
                vendedores = Vendedor.read_all()
            if not vendedores:
                fp.mensagem_erro_ao_recuperar_info()
                return
            fp.info_vendedores(vendedores)
        
        escolha = fi.opcao_menu_vendedor_busca()

def cadastrar_cliente():
    dados = fi.dados_cliente()
    if Cliente.create(*dados):
        fp.mensagem_sucesso()
        fp.mensagem_4()
    else:
        fp.mensagem_erro()

def cadastrar_produto():
    info = fi.info_produto_novo()
    if Produto.create(*info):
        fp.mensagem_sucesso()
        fp.mensagem_4()
    else:
        fp.mensagem_erro()

def cadastrar_vendedor():
    dados = fi.info_vendedor_novo()
    if Vendedor.create(*dados):
        fp.mensagem_sucesso()
        fp.mensagem_4()
    else:
        fp.mensagem_erro()

def cancelar_compra():
    # pede e valida o id
    id_compra = fi.pedir_id()
    if not Compra.validate_id(id_compra):
        fp.mensagem_erro_id_invalido()
        return
    
    # puxa as informações da compra
    compra = Compra.read(id_compra)
    produtos = Compra_Produto.read_all_from_compra(id_compra)
    status_do_pagamento = Pagamento.return_status_de_pagamento(id_compra)

    if not compra or not produtos or not status_do_pagamento:
        fp.mensagem_erro_ao_recuperar_info()
        return

    fp.info_compra(*compra)
    fp.info_compra_produtos(produtos)

    if not fi.tem_certeza():
        return

    # cancela o pagamento sem reembolsar ou retornar mercadoria
    if status_do_pagamento == "{'Pendente'}":
        if not Pagamento.cancel_payment(id_compra):
            fp.mensagem_erro_atualizar_status_compra()
            return

    # reembolsa o pagamento, a compra e dá alta no estoque
    elif status_do_pagamento == "{'Confirmado'}":
        if not Pagamento.refund_payment(id_compra):
            fp.mensagem_erro_atualizar_status_compra()
            return
    
    elif status_do_pagamento == "{'Cancelado'}" or status_do_pagamento == "{'Reembolsado'}":
        fp.mensagem_compra_já_cancelada()
        return
    
    fp.mensagem_sucesso()
    fp.mensagem_3()

def relatorio():
    id = fi.pedir_id()
    mes, ano = fi.pedir_mes_ano()

    if not Vendedor.validate_id(id):
        fp.mensagem_erro_id_invalido()
        return
    
    fr.relatorio_por_vendedor_por_mes(id, mes, ano)

def remover_produto():
    id = fi.pedir_id()
    if not Produto.validate_id(id):
        fp.mensagem_erro_id_invalido()
        return    

    produto = Produto.read_by_id(id)
    fp.info_produto(*produto)

    if not fi.tem_certeza():
        return
    
    if not Produto.delete(id):
        fp.mensagem_erro()
        return

def nova_compra():

    # Definindo o id do cliente
    # O cliente pode já ter cadastro, se cadastrar, ou não informar dados
    if fi.cliente_vai_dar_dado():
        if fi.cliente_tem_cadastro():
            cpf = fi.pedir_cpf()
            id_cliente = Cliente.return_id(cpf)

            # se o id retornado for 0, o cpf não está cadastrado
            # ou ocorreu um erro na consulta

            while id_cliente == 0:

                # tenta encontrar o cliente novamente, caso seja erro de digitação
                if fi.cpf_nao_encontrado_tentar_novamente():
                    cpf = fi.pedir_cpf()
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
                fp.mensagem_sucesso()
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
    dados = fi.dados_compra(id_cliente)

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
    if produtos == []:
        if not Pagamento.cancel_payment(id_compra):
            fp.mensagem_erro_ao_cancelar_compra()
            return
        fp.mensagem_compra_cancelada()
        return
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
            fp.mensagem_erro_ao_cancelar_compra()
            fi.deu_ruim_sair_da_operacao()
            return
    
    fp.mensagem_sucesso_compra_nova()
    fp.mensagem_1()