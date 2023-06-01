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
    data = input("Data da compra, formato aaaa-mm-dd: ")
    return (id_cliente, id_vendedor, data, 'Aguardando confirmação')

# Retorna os dados dos produtos escolhidos em uma lista de tuplas
# Cada tupla está na ordem (id_compra, id_produdo, quantidade)
def escolher_produtos(id_compra):
    id = int(input("Id do 1° produto: "))
    qtd = int(input("Quantidade do 1° produto: "))

    produtos = [(id_compra, id, qtd)]

    escolha = input("Deseja incluir mais produtos? (s/n) ")
    i = 2

    while escolha != 'n':
        if escolha != 's': 
            escolha = input("Opção inválida! Digite s ou n: ")
        else:
            id = int(input(f"Id do {i}° produto: "))
            qtd = int(input(f"Quantidade do {i}° produto: "))
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