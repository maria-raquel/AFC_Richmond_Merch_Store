def info_pagamento(id_compra, total, desconto):
    print("----------------------------------------")
    print(f"Informações da compra {id_compra}:")
    print("Total: R$ %.2f" % total)
    if desconto:
        print("Mas pera! Esse cliente tem direito a um desconto de R$ %.2f" % desconto)
        print("Total com desconto: R$ %.2f" % (total - desconto))
        print(":)")
    print("----------------------------------------")

def info_produto(id, nome, preco, estoque, categoria, local_de_fabricacao, disponibilidade):
    print("----------------------------------------")

    # transforma categoria em string e remove as chaves e aspas
    categoria = str(categoria)[2:-2]

    print(f"Produto {id}: {nome}")
    print("Preço: R$ %.2f" % preco)
    print(f"Quantidade em estoque: {estoque}")
    print(f"Categoria: {categoria}, Local de fabricação: {local_de_fabricacao}")
    if not disponibilidade:
        print("Este produto não está disponível no momento")
    print("----------------------------------------")
    
def boas_vindas():
    print("----------------------------------------")
    print("--Bem vindo ao controle de estoque da---")
    print("----Loja oficial do A.F.C. Richmond-----")
    print("------------WE ARE RICHMOND-------------")
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

def mensagem_erro_ao_recuperar_info_produto():
    print("----------------------------------------")
    print("Erro ao recuperar informações do produto!")
    print("----------------------------------------")

def mensagem_sucesso():
    print("----------------------------------------")
    print("Operação realizada com sucesso!")
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

def menu_principal():
    print("Menu: ")
    print("1 - Compras")
    print("2 - Produtos")
    print("3 - Clientes")
    print("4 - Vendedores")
    print("5 - Relatórios")
    print("0 - Sair")

def menu_compra():
    print("Menu - Compras: ")
    print("1 - Realizar nova compra")
    print("2 - Buscar compra já feita")
    print("3 - Atualizar compra já feita")
    print("4 - Cancelar compra já feita")
    print("0 - Voltar")

def submenu_compra_busca():
    print("Menu - Compras - Busca: ")
    print("1 - Por id")
    print("2 - Por cliente")
    print("3 - Por vendedor")
    print("4 - Por data")
    print("5 - Com pagamento pendente")
    print("6 - Todas")
    print("0 - Voltar")

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