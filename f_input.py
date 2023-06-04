import connect_to_DB
import f_print as fp
import t_produto as pr

connection = connect_to_DB.connect()
Produto = pr.Table_Produto(connection)

# Pede uma ação para encerrar a operação
def deu_ruim_sair_da_operacao():
    print("Encerrando a operação, averigue o que aconteceu.")
    sair = input("Aperte enter para sair: ")
    return

# Retorna True ou False
def cliente_vai_dar_dado():
    escolha = input("O cliente deseja informar dados? (s/n) ")
    while escolha != "s" and escolha != "n":
        escolha = input("Opção inválida! (s/n) ")
    if escolha == "s":
        return True
    else:
        return False

# Retorna True ou False
def cliente_tem_cadastro():
    escolha = input("O cliente já possui cadastro? (s/n) ")
    while escolha != "s" and escolha != "n":
        escolha = input("Opção inválida! (s/n) ")
    if escolha == "s":
        return True
    else:
        return False

def cpf_cliente():
    cpf = input("Informe o CPF do cliente: ")
    return cpf

# Retorna True se o usuário deseja tentar novamente
# e False se o usuário deseja cancelar a operação
def cpf_nao_encontrado_tentar_novamente():
    print("Opa! Parece que esse cpf não está cadastrado no sistema.")
    print("Você deseja: ")
    print("1: Tentar digitar o cpf novamente? ")
    print("0: Cancelar a operação? ")
    escolha = int(input("Digite 1 ou 0: "))

    while escolha != 0 and escolha != 1:
        escolha = int(input("Opção inválida! Digite 1 ou 0: "))

    return escolha

# Retorna os dados do cliente em uma tupla
# Na ordem (cpf, nome, is_flamengo, assiste_one_piece, cidade_natal)
def dados_cliente():
    print("Informe os dados do cliente: ")
    nome = input("Nome: ")
    cpf = input("CPF: ")

    aux = input("É flamenguista? (s/n) ")
    while aux != "s" and aux != "n":
        aux = input("Opção inválida! (s/n) ")
    
    if aux == "s":
        is_flamengo = 1
    else:
        is_flamengo = 0
    
    aux = input("Assiste One Piece? (s/n) ")
    while aux != "s" and aux != "n":
        aux = input("Opção inválida! (s/n) ")
    
    if aux == "s":
        assiste_one_piece = 1
    else:
        assiste_one_piece = 0
    
    cidade_natal = input("Cidade natal: ")

    return (cpf, nome, is_flamengo, assiste_one_piece, cidade_natal)

# Retorna os dados da compra em uma tupla
# Na ordem: (id_cliente, id_vendedor, data, 'Aguardando confirmação')
def dados_da_compra(id_cliente):
    print("Informe os dados da compra: ")
    id_vendedor = int(input("ID do vendedor: "))

    # validar id do vendedor aqui

    data = input("Data da compra, formato aaaa-mm-dd: ")

    # validar data aqui

    return (id_cliente, id_vendedor, data, 'Aguardando confirmação')

# Retorna os dados dos produtos escolhidos em uma lista de tuplas
# Cada tupla está na ordem (id_compra, id_produdo, quantidade)

def escolher_produtos(id_compra):
    produtos = []
    escolha = 's'
    i = 1

    while escolha != 'n':
        if escolha != 's': 
            escolha = input("Opção inválida! Digite s ou n: ")
        else:
            id_invalido = True

            while id_invalido:
                try:
                    id = int(input(f"Id do {i}° produto: "))
                except ValueError:
                    print("Id inválido! Digite novamente. ")
                    continue

                if Produto.validate_id(id):
                    id_invalido = False
                
                else:
                    print("Id inválido! Digite novamente. ")

            dados_produto = Produto.read_by_id(id)
            if not dados_produto:
                fp.mensagem_erro_ao_recuperar_info_produto()
            
            fp.info_produto(*dados_produto)

            quantidade_invalida = True

            while quantidade_invalida:
                try:
                    qtd = int(input(f"Quantidade do {i}° produto: (0 para desistir dele) "))
                except ValueError:
                    print("Quantidade inválida! Digite novamente. ")
                    continue

                estoque = Produto.return_estoque(id)

                if qtd < 0:
                    print("Quantidade inválida! Digite novamente. ")
                elif qtd > estoque:
                    print("Eita! Quantidade indisponível em estoque!")
                    print(f"Há {estoque} unidades disponíveis.")
                else:
                    quantidade_invalida = False

            if qtd != 0:
                produtos.append((id_compra, id, qtd))
                i = i+1
                escolha = input("Deseja incluir mais produtos? (s/n) ")
    
    return produtos

# Retorna a forma de pagamento escolhida, em string
def forma_de_pagamento(id_compra):
    formas = {1: 'Dinheiro',
              2: 'Cartão de crédito',
              3: 'Cartão de débito',
              4: 'Boleto',
              5: 'Pix'}

    print("Opções de pagamento: ")
    for opcao in formas:
        print(f"{opcao}: {formas[opcao]}")

    try:
        escolha = int(input("Digite a opção escolhida: "))
    except ValueError:
        escolha = 0

    while escolha not in (1,2,3,4,5):
        escolha = int(input("Opção inválida, digite novamente: "))

    return formas[escolha]

def confirmação_do_pagamento():
    print("Solicite o pagamento ao cliente")

    pagamento = 1
    while pagamento:
        escolha = input("O pagamento foi confirmado? (s/n) ")
        while escolha != "s" and escolha != "n":
            escolha = input("Opção inválida! Digite s ou n: ")

        if escolha == "s":
            return True
        else:
            escolha = input("Deseja tentar novamente? (s/n) ")
            if escolha == "n":
                pagamento = 0
                return False