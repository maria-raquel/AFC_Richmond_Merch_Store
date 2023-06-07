import connect_to_DB
import f_print as fp
import t_produto as pr
import t_compra as cm
import t_vendedor as v
from datetime import date

connection = connect_to_DB.connect()
Produto = pr.Table_Produto(connection)
Compra = cm.Table_Compra(connection)
Vendedor = v.Table_Vendedor(connection)

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

# Retorna o cpf do cliente em string
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

    id_invalido = True

    while id_invalido:
        try:
            id_vendedor = int(input("ID do vendedor: "))
        except ValueError:
            print("Id inválido! Digite novamente.")
            continue

        if Vendedor.validate_id(id_vendedor):
            id_invalido = False
        
        else:
            print("Id inválido!")
            iai = int(input("Digite 1 para tentar novamente ou 0 para sair. "))
            if not iai:
                return

    data = date.today().strftime("%Y-%m-%d")

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
                fp.mensagem_erro_ao_recuperar_info()
            
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
              4: 'Pix'}

    print("Opções de pagamento: ")
    for opcao in formas:
        print(f"{opcao}: {formas[opcao]}")

    try:
        escolha = int(input("Digite a opção escolhida: "))
    except ValueError:
        escolha = 0

    while escolha not in (1,2,3,4):
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
            
def opcao_menu_principal():
    print("----------------------------------------")
    print("Menu: ")
    print("1 - Compras")
    print("2 - Produtos")
    print("3 - Clientes")
    print("4 - Vendedores")
    print("5 - Relatórios")
    print("0 - Sair")
    

    escolha = int(input("Digite: "))

    while escolha not in (0,1,2,3,4,5):
        escolha = int(input("Opção inválida! Digite novamente: "))
    
    return escolha

def opcao_menu_compras():
    print("----------------------------------------")
    print("Menu - Compras: ")
    print("1 - Realizar nova compra")
    print("2 - Buscar compra já feita")
    print("3 - Atualizar compra já feita")
    print("4 - Cancelar compra já feita")
    print("0 - Voltar")

    escolha = int(input("Digite: "))

    while escolha not in (0,1,2,3,4):
        escolha = int(input("Opção inválida! Digite novamente: "))
    
    return escolha

def opcao_menu_compras_busca():
    print("----------------------------------------")
    print("Menu - Compras - Busca: ")
    print("1 - Por id")
    print("2 - Por cliente")
    print("3 - Por vendedor")
    print("4 - Por data")
    print("5 - Todas")
    print("0 - Voltar")
    
    escolha = int(input("Digite: "))

    while escolha not in (0,1,2,3,4,5):
        escolha = int(input("Opção inválida! Digite novamente: "))
    
    return escolha

def id_compra():
    id_invalido = True

    while id_invalido:
        try:
            id = int(input("Digite o id da compra: "))
            id_invalido = False
        except ValueError:
            print("Id inválido! Digite novamente. ")

    return id

def id_cliente():
    id_invalido = True

    while id_invalido:
        try:
            id = int(input("Digite o id do cliente: "))
            id_invalido = False
        except ValueError:
            print("Id inválido! Digite novamente. ")

    return id

def id_vendedor():
    id_invalido = True

    while id_invalido:
        try:
            id = int(input("Digite o id do vendedor: "))
            id_invalido = False
        except ValueError:
            print("Id inválido! Digite novamente. ")

    return id

def id_produto():
    id_invalido = True
    while id_invalido:
        try:
            id = int(input(f"Id do produto: "))
            id_invalido = False
        except ValueError:
            print("Id inválido! Digite novamente. ")


    return id

def nome_produto():
    nome = input(f"Nome do produto: ")
    return nome

def local_de_fabricacao():
    local = input(f"Local de fabricação: ")
    return local

def data():
    id_invalido = True
    print("Digite a data da compra")
    print("Formato: aaaa-mm-dd")
    print("Ou pode ser só ano (aaaa), só mês (-mm-), ano e mes (aaaa-mm)")
    data = input("Data da compra: ")
    return data

def update_compra():
    print("Que tipo de informação deseja atualizar? ")
    tabela = input("Da compra, do pagamento ou dos produtos? ")

    if tabela not in ('compra', 'pagamento', 'produtos'):
        tabela = input("Opção inválida! Digite novamente. ")
    
    if tabela == 'produtos':
        id = int(input("Digite o id do produto: "))
        qtd = int(input("Digite a nova quantidade: "))
        return tabela, id, qtd
    
    coluna = input("Digite o nome da coluna: ")
    valor = input("Digite o novo valor: ")

    return tabela, coluna, valor

def update_produto():
    colunas = {1: 'nome',
               2: 'preco',
               3: 'estoque',
               4: 'categoria',
               5: 'local_de_fabricacao'}
    for coluna in colunas:
        print(f"{coluna}: {colunas[coluna]}")
    
    c = -1
    while c not in (1,2,3,4,5):
        try:
            c = int(input("Digite o número da coluna que deseja atualizar: "))
        except ValueError:
            print("Opção inválida! Digite novamente: ")

    if c == 1 or c == 5:
        valor = input("Digite o novo valor: ")
        while valor == "":
            valor = input("Valor inválido! Digite novamente: ")
        return colunas[c], valor
    
    if c == 2:
        valor = -1
        while valor <= 0:
            try:
                valor = float(input("Digite o novo valor: "))
            except ValueError:
                print("Valor inválido!")
            if valor <= 0:
                print("Valor inválido!")
        return colunas[c], valor

    if c == 3:
        valor = -1
        while valor < 0:
            try:
                valor = int(input("Digite o novo valor: "))
            except ValueError:
                print("Valor inválido!")
            if valor < 0:
                print("Valor inválido!")
        return colunas[c], valor
    
    if c == 4:
        valor = ''
        while valor not in ('v', 'o'):
            valor = input("Digite v para Vestuário e o para Outros: ")
            if valor not in ('v', 'o'):
                print("Valor inválido!")
        if valor == 'v':
            valor = 'Vestuário'
        else:
            valor = 'Outros'
        return colunas[c], valor

def opcao_menu_produto():
    print("----------------------------------------")
    print("Menu - Produtos: ")
    print("1 - Cadastrar novo produto")
    print("2 - Buscar produto")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("0 - Voltar")

    escolha = int(input("Digite: "))

    while escolha not in (0,1,2,3,4):
        escolha = int(input("Opção inválida! Digite novamente: "))
    
    return escolha

def info_produto_novo():
    nome_invalido = True
    while nome_invalido:
        nome = input("Nome do produto: ")
        if nome == "":
            print("Nome inválido! Digite novamente.")
        else:
            nome_invalido = False

    preco_invalido = True
    while preco_invalido:
        try:
            preco = float(input("Preço do produto: "))
        except ValueError:
            print("Preço inválido! Digite novamente.")

        if preco <= 0:
            print("Preço inválido! Digite novamente.")
        else: 
            preco_invalido = False

    estoque_invalido = True
    while estoque_invalido:
        try:
            estoque = int(input("Quantidade em estoque: "))
        except ValueError:
            print("Quantidade inválida! Digite novamente.")
        
        if estoque < 0:
            print("Quantidade inválida! Digite novamente.")
        else:
            estoque_invalido = False
    
    categoria_invalida = True
    while categoria_invalida:
        categoria = input("Categoria do produto: ")
        if categoria not in ("Vestuário", "Outros"):
            print("Categoria inválida! Digite novamente.")
        else:
            categoria_invalida = False

    local_invalido = True
    while local_invalido:
        local_de_fabricacao = input("Local de fabricação do produto: ")
        if local_de_fabricacao == "":
            print("Local inválido! Digite novamente.")
        else:
            local_invalido = False

    disponibilidade_invalida = True
    while disponibilidade_invalida:
        disponibilidade = input("Ele já está disponível para vendas? (s/n): ")
        if disponibilidade not in ("s", "n"):
            print("Opção inválida! Digite novamente.")
        else:
            disponibilidade_invalida = False

    if disponibilidade == "s":
        d = 1
    else:
        d = 0

    return (nome, preco, estoque, categoria, local_de_fabricacao, d)

def opcao_menu_produto_busca():
    print("----------------------------------------")
    print("Menu - Produto - Busca: ")
    print("1 - Por id")
    print("2 - Por nome")
    print("3 - Por categoria")
    print("4 - Por local de fabricação")
    print("5 - Por faixa de preço")
    print("6 - Todos")
    print("0 - Voltar")

    try:
        escolha = int(input("Digite: "))
    except ValueError:
        print("Opção inválida! Digite novamente: ")

    while escolha not in (0,1,2,3,4,5,6):
        try:
            escolha = int(input("Opção inválida! Digite novamente: "))
        except ValueError:
            print("Opção inválida! Digite novamente: ")

    return escolha

def categoria():
    print("Vestuário ou Outros?")
    categoria = input("Digite v ou o: ")
    while categoria not in ("v", "o"):
        categoria = input("Opção inválida! Digite novamente: ")
    return categoria    

def faixa_de_preco():
    min_invalido = True
    while min_invalido:
        try:
            min = float(input("Digite o valor mínimo: "))
            min_invalido = False
        except ValueError:
            print("Valor inválido! Digite novamente: ")
    
    max_invalido = True
    while max_invalido:
        try:
            max = float(input("Digite o valor máximo: "))
            max_invalido = False
        except ValueError:
            print("Valor inválido! Digite novamente: ")
    
    return (min, max)

def apenas_disponiveis():
    print("Deseja ver apenas os disponíveis? (s/n)")
    escolha = input("Digite s ou n: ")
    while escolha not in ("s", "n"):
        escolha = input("Opção inválida! Digite novamente: ")

    if escolha == "s":
        return True
    return False

def tem_certeza():
    print("Tem certeza que deseja realizar essa operação? (s/n)")
    escolha = input("Digite s ou n: ")
    while escolha not in ("s", "n"):
        escolha = input("Opção inválida! Digite novamente: ")

    if escolha == "s":
        return True
    return False

def opcao_menu_cliente():
    print("Menu - Clientes: ")
    print("1 - Cadastrar novo cliente")
    print("2 - Buscar cliente cadastrado")
    print("3 - Atualizar cliente cadastrado")
    print("4 - Remover cliente cadastrado")
    print("0 - Voltar")

    try:
        escolha = int(input("Digite: "))
    except ValueError:
        print("Opção inválida! Digite novamente: ")

    while escolha not in (0,1,2,3,4):
        try:
            escolha = int(input("Opção inválida! Digite novamente: "))
        except ValueError:
            print("Opção inválida! Digite novamente: ")

    return escolha