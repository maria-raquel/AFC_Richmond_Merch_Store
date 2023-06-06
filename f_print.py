# imprime um pagamento a partir de uma tupla
def info_pagamento(id_compra, total, desconto, total_pos_desconto, status_do_pagamento, forma_de_pagamento):
    print("----------------------------------------")
    print(f"Informações da compra {id_compra}:")
    print("Total: R$ %.2f" % total)

    if desconto:
        print("Desconto: R$ %.2f" % desconto)
        print("Total com desconto: R$ %.2f" % total_pos_desconto)

    # transforma set em string e remove as chaves e aspas
    status_do_pagamento = str(status_do_pagamento)[2:-2]
    forma_de_pagamento = str(forma_de_pagamento)[2:-2]

    print(f"Status do pagamento: {status_do_pagamento}; Forma de pagamento: {forma_de_pagamento}")
    print("----------------------------------------")

# imprime um produto a partir de uma tupla
def info_produto(id, nome, preco, estoque, categoria, local_de_fabricacao, disponibilidade):
    print("----------------------------------------")

    # transforma set em string e remove as chaves e aspas
    categoria = str(categoria)[2:-2]

    print(f"Produto {id}: {nome}")
    print("Preço: R$ %.2f" % preco)
    print(f"Quantidade em estoque: {estoque}")
    print(f"Categoria: {categoria}; Local de fabricação: {local_de_fabricacao}")
    if not disponibilidade:
        print("Este produto não está disponível no momento.")
    print("----------------------------------------")

# imprime várias compras a partir de uma lista de tuplas
def info_compras(compras):
    print("----------------------------------------")
    print("id | id do cliente | id do vendedor | data | total | status da compra")

    for id, id_cliente, id_vendedor, data, status_c, total, desconto, total_pd, forma, status_p in compras:
        # formata a data para dd/mm/aaaa
        data = data.strftime("%d/%m/%Y")
        status_c = str(status_c)[2:-2]
        print(f"{id} | {id_cliente} | {id_vendedor} | {data} | {total_pd} | {status_c}")
    print("----------------------------------------")

# imprime uma compra a partir de uma tupla
def info_compra(id, id_cliente, id_vendedor, data, status_c, 
                total, desconto, total_pos_desconto, status_do_pagamento, forma_de_pagamento):
    print("----------------------------------------")
    data = data.strftime("%d/%m/%Y")
    status_c = str(status_c)[2:-2]
    print(f"Compra {id}:")
    print(f"Id do cliente: {id_cliente}; Id do vendedor: {id_vendedor}")
    print(f"Data: {data}; Status da compra: {status_c}")
    print("Total: R$ %.2f" % total)

    if desconto:
        print("Desconto: R$ %.2f" % desconto)
        print("Total com desconto: R$ %.2f" % total_pos_desconto)

    # transforma set em string e remove as chaves e aspas
    status_do_pagamento = str(status_do_pagamento)[2:-2]
    forma_de_pagamento = str(forma_de_pagamento)[2:-2]

    print(f"Status do pagamento: {status_do_pagamento}; Forma de pagamento: {forma_de_pagamento}")

def info_compra_produtos(produtos):
    print("Produtos dessa compra: ")
    print("id | nome | preço | quantidade")
    for id_c, id_p, nome, preco, qtd in produtos:
        print(f"{id_p} | {nome} | {preco} | {qtd}")
    print("----------------------------------------")

def boas_vindas():
    print("----------------------------------------")
    print("--Bem vindo ao controle de estoque da---")
    print("----Loja oficial do A.F.C. Richmond-----")
    print("------------WE ARE RICHMOND-------------")
    print("----------------------------------------")

def mensagem_erro_id_invalido():
    print("----------------------------------------")
    print("Id inválido! Tente novamente. ")
    print("----------------------------------------")

def mensagem_erro_ao_cadastrar_cliente():
    print("----------------------------------------")
    print("Algo deu errado ao inserir o cliente!")
    print("----------------------------------------")

def mensagem_sucesso_ao_cadastrar_cliente():
    print("----------------------------------------")
    print("Cliente cadastrado com sucesso!")
    print("----------------------------------------")

def mensagem_erro_ao_cadastrar_compra():
    print("----------------------------------------")
    print("Algo deu errado ao cadastrar a compra!")
    print("----------------------------------------")

def mensagem_erro_ao_recuperar_id_compra():
    print("----------------------------------------")
    print("Erro ao recuperar o id da compra!")
    print("----------------------------------------")

def mensagem_erro_ao_adicionar_produto():
    print("----------------------------------------")
    print("Erro ao adicionar produto!")
    print("----------------------------------------")

def mensagem_erro_ao_calcular_total():
    print("----------------------------------------")
    print("Erro ao calcular o total da compra!")
    print("----------------------------------------")

def mensagem_erro_ao_cadastrar_pagamento():
    print("----------------------------------------")
    print("Erro ao cadastrar o pagamento da compra!")
    print("----------------------------------------")

def mensagem_erro_atualizar_status_compra():
    print("----------------------------------------")
    print("Erro ao atualizar o status da compra!")
    print("----------------------------------------")

def mensagem_erro_ao_recuperar_info():
    print("----------------------------------------")
    print("Erro ao recuperar informações!")
    print("----------------------------------------")

def mensagem_erro_reinicie():
    print("----------------------------------------")
    print("Eita, deu um ruim aqui que é melhor reiniciar o programa.")
    print("----------------------------------------")

def mensagem_sucesso():
    print("----------------------------------------")
    print("Operação realizada com sucesso!")
    print("----------------------------------------")

def mensagem_erro():
    print("----------------------------------------")
    print("Eita, algo errado!")
    print("----------------------------------------")

def mensagem_sucesso_compra_nova():
    print("----------------------------------------")
    print("Compra cadastrada com sucesso!")
    print("----------------------------------------")

def mensagem_1():
    print("----------------------------------------")
    print("-------------FÚTBALL IS LIFE------------")
    print("----------------------------------------")

def mensagem_2():
    print("----------------------------------------")
    print("-------------WE ARE RICHMOND------------")
    print("----------------------------------------")

def mensagem_3():
    print("----------------------------------------")
    print("------------------BELIEVE---------------")
    print("----------------------------------------")

def mensagem_4():
    print("----------------------------------------")
    print("-------------GO GREYHOUNDS--------------")
    print("----------------------------------------")

def mensagem_5():
    print("----------------------------------------")
    print("-------WE'RE RICHMOND TILL WE DIE-------")
    print("----------------------------------------")

def despedida():
    print("----------------------------------------")
    print("-----------Sistema encerrado------------")
    print("-------------até a próxima--------------")
    print("----------------------------------------")
    print("--╔══╗ ╔═══╗╔╗   ╔══╗╔═══╗╔╗  ╔╗╔═══╗---")
    print("--║╔╗║ ║╔══╝║║   ╚╣╠╝║╔══╝║╚╗╔╝║║╔══╝---")
    print("--║╚╝╚╗║╚══╗║║    ║║ ║╚══╗╚╗║║╔╝║╚══╗---")
    print("--║╔═╗║║╔══╝║║ ╔╗ ║║ ║╔══╝ ║╚╝║ ║╔══╝---")
    print("--║╚═╝║║╚══╗║╚═╝║╔╣╠╗║╚══╗ ╚╗╔╝ ║╚══╗---")
    print("--╚═══╝╚═══╝╚═══╝╚══╝╚═══╝  ╚╝  ╚═══╝---")
    print("----------------------------------------")

def menu_produto():
    print("Menu - Produtos: ")
    print("1 - Cadastrar novo produto")
    print("2 - Buscar produto cadastrado")
    print("3 - Atualizar produto cadastrado")
    print("4 - Remover produto cadastrado")
    print("0 - Voltar")

def submenu_produto_busca():
    print("Menu - Produtos - Busca: ")
    print("1 - Por id")
    print("2 - Por nome")
    print("3 - Todos disponíveis")
    print("4 - Todos")
    print("0 - Voltar")

def menu_cliente():
    print("Menu - Clientes: ")
    print("1 - Cadastrar novo cliente")
    print("2 - Buscar cliente cadastrado")
    print("3 - Atualizar cliente cadastrado")
    print("4 - Remover cliente cadastrado")
    print("0 - Voltar")

def submenu_cliente_busca():
    print("Menu - Clientes - Busca: ")
    print("1 - Por id")
    print("2 - Por nome")
    print("3 - Por CPF")
    print("4 - Todos")
    print("0 - Voltar")

def menu_vendedor():
    print("Menu - Vendedores: ")
    print("1 - Cadastrar novo vendedor")
    print("2 - Buscar vendedor cadastrado")
    print("3 - Atualizar vendedor cadastrado")
    print("0 - Voltar")

def submenu_vendedor_busca():
    print("Menu - Vendedores - Busca: ")
    print("1 - Por id")
    print("2 - Por nome")
    print("3 - Todos ativos")
    print("4 - Todos")
    print("0 - Voltar")

def menu_relatorios():
    print("Menu - Relatórios: ")
    print("1 - Relatório de compras")
    print("2 - Relatório de produtos")
    print("3 - Relatório de clientes")
    print("4 - Relatório de vendedores")