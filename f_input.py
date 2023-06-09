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

# Retorna True ou False
def apenas_disponiveis():
    print("Deseja ver apenas os disponíveis? (s/n)")
    escolha = input("Digite s ou n: ")
    while escolha not in ("s", "n"):
        escolha = input("Opção inválida! Digite novamente: ")

    if escolha == "s":
        return True
    return False

#Retorna v ou o
def categoria():
    print("Vestuário ou Outros?")
    categoria = input("Digite v ou o: ")
    while categoria not in ("v", "o"):
        categoria = input("Opção inválida! Digite novamente: ")
    return categoria   

# Retorna True ou False
def cliente_tem_cadastro():
    escolha = input("O cliente já possui cadastro? (s/n) ")
    while escolha != "s" and escolha != "n":
        escolha = input("Opção inválida! (s/n) ")
    if escolha == "s":
        return True
    else:
        return False

# Retorna True ou False
def cliente_vai_dar_dado():
    escolha = input("O cliente deseja informar dados? (s/n) ")
    while escolha != "s" and escolha != "n":
        escolha = input("Opção inválida! (s/n) ")
    if escolha == "s":
        return True
    else:
        return False

def confirmação_do_pagamento():
    print("Solicite o pagamento ao cliente")

    while True:
        escolha = input("O pagamento foi confirmado? (s/n) ")
        while escolha != "s" and escolha != "n":
            escolha = input("Opção inválida! Digite s ou n: ")

        if escolha == "s":
            return True
        else:
            escolha = input("Deseja tentar novamente? (s/n) ")
            if escolha == "n":
                return False

# Retorna True se o usuário deseja tentar novamente
# e False se o usuário deseja cancelar a operação
def cpf_nao_encontrado_tentar_novamente():
    print("Opa! Parece que esse cpf não está cadastrado no sistema.")
    print("Você deseja tentar novamente? (s/n) ")
   
    escolha = input("Digite s ou n: ")
    while escolha != 's' and escolha != 'n':
        escolha = input("Opção inválida! Digite s ou n: ")

    if escolha == 's':
        return True
    else:
        return False

# Retorna os dados do cliente em uma tupla
# Na ordem (cpf, nome, is_flamengo, assiste_one_piece, cidade_natal)
def dados_cliente():
    print("Informe os dados do cliente: ")
    nome = pedir_nome()
    cpf = pedir_cpf()

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
def dados_compra(id_cliente):
    print("Informe os dados da compra: ")

    id_invalido = True

    while id_invalido:
        print("Id do vendedor ")
        id_vendedor = pedir_id()

        if Vendedor.validate_id(id_vendedor):
            id_invalido = False
        
        else:
            print("Id inválido!")
            iai = int(input("Digite 1 para tentar novamente ou 0 para sair. "))
            if not iai:
                return

    data = date.today().strftime("%Y-%m-%d")

    return (id_cliente, id_vendedor, data, 'Aguardando confirmação')

# Retorna a data de uma compra, em string
def data():
    id_invalido = True
    print("Digite a data da compra")
    print("Formato: aaaa-mm-dd")
    print("Ou pode ser só ano (aaaa), só mês (-mm-), ano e mes (aaaa-mm)")
    data = input("Data da compra: ")
    while data == "":
        data = input("Data inválida! Digite novamente: ")
    return data

# Pede uma ação para encerrar a operação
def deu_ruim_sair_da_operacao():
    print("Encerrando a operação, averigue o que aconteceu.")
    sair = input("Aperte enter para sair: ")
    return

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

# Retorna (min, max), float
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

# Retorna a forma de pagamento escolhida, em string
def forma_de_pagamento(id_compra):
    formas = {'1': 'Dinheiro',
              '2': 'Cartão de crédito',
              '3': 'Cartão de débito',
              '4': 'Pix'}

    print("Opções de pagamento: ")
    for opcao in formas:
        print(f"{opcao}: {formas[opcao]}")

    escolha = input("Digite a opção escolhida: ")

    while escolha not in ('1','2','3','4'):
        escolha = input("Opção inválida, digite novamente: ")

    return formas[escolha]

# Retorna na ordem (nome, preco, estoque, categoria, local_de_fabricacao, disponibilidade)
def info_produto_novo():
    nome = pedir_nome()

    preco_invalido = True
    while preco_invalido:
        try:
            preco = float(input("Preço do produto: "))
        except ValueError:
            print("Preço inválido! Digite novamente.")
            continue

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
            continue
        
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

# Retorna na ordem (cpf, nome, status)
def info_vendedor_novo():
    nome = pedir_nome()
    cpf = pedir_cpf()
    return (cpf, nome, 'Ativo')

def local_de_fabricacao():
    local = input(f"Local de fabricação: ")
    while local == "":
        local = input(f"Local inválido! Digite novamente: ")
    return local

# Retorna str
def opcao_menu_cliente():
    print("Menu - Clientes: ")
    print("1 - Cadastrar novo cliente")
    print("2 - Buscar cliente")
    print("3 - Atualizar cliente")
    print("4 - Remover cliente")
    print("0 - Voltar")

    escolha = input("Digite: ")

    while escolha not in ('0','1','2','3','4'):
        escolha = input("Opção inválida! Digite novamente: ")

    return escolha

# Retorna str
def opcao_menu_cliente_busca():
    print("----------------------------------------")
    print("Menu - Clientes - Busca: ")
    print("1 - Por id")
    print("2 - Por nome")
    print("3 - Por CPF")
    print("4 - Todos")
    print("0 - Voltar")

    escolha = input("Digite: ")
    while escolha not in ('0','1','2','3','4','5','6'):
        escolha = input("Opção inválida! Digite novamente: ")

    return escolha

# Retorna str
def opcao_menu_compras():
    print("----------------------------------------")
    print("Menu - Compras: ")
    print("1 - Realizar nova compra")
    print("2 - Buscar compra")
    print("3 - Atualizar compra")
    print("4 - Cancelar compra")
    print("0 - Voltar")

    escolha = input("Digite: ")

    while escolha not in ('0','1','2','3','4'):
        escolha = input("Opção inválida! Digite novamente: ")
    
    return escolha

# Retorna str
def opcao_menu_compras_busca():
    print("----------------------------------------")
    print("Menu - Compras - Busca: ")
    print("1 - Por id")
    print("2 - Por cliente")
    print("3 - Por vendedor")
    print("4 - Por data")
    print("5 - Todas")
    print("0 - Voltar")
    
    escolha = input("Digite: ")

    while escolha not in ('0','1','2','3','4','5'):
        escolha = input("Opção inválida! Digite novamente: ")
    
    return escolha

# Retorna str
def opcao_menu_principal():
    print("----------------------------------------")
    print("Menu: ")
    print("1 - Compras")
    print("2 - Produtos")
    print("3 - Clientes")
    print("4 - Vendedores")
    print("5 - Relatórios")
    print("0 - Sair")

    escolha = input("Digite: ")

    while escolha not in ('0','1','2','3','4','5'):
        escolha = input("Opção inválida! Digite novamente: ")
    
    return escolha

# Retorna str
def opcao_menu_produto():
    print("----------------------------------------")
    print("Menu - Produtos: ")
    print("1 - Cadastrar novo produto")
    print("2 - Buscar produto")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("0 - Voltar")

    escolha = input("Digite: ")

    while escolha not in ('0','1','2','3','4'):
        escolha = input("Opção inválida! Digite novamente: ")
    
    return escolha

# Retorna str
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

    escolha = input("Digite: ")
    while escolha not in ('0','1','2','3','4','5','6'):
        escolha = input("Opção inválida! Digite novamente: ")

    return escolha

# Retorna str
def opcao_menu_vendedor():
    print("Menu - Vendedores: ")
    print("1 - Cadastrar novo vendedor")
    print("2 - Buscar vendedor")
    print("3 - Atualizar vendedor")
    print("0 - Voltar")

    escolha = input("Digite: ")
    
    while escolha not in ('0','1','2','3'):
        escolha = input("Opção inválida! Digite novamente: ")
        
    return escolha

# Retorna str
def opcao_menu_vendedor_busca():
    print("----------------------------------------")
    print("Menu - Vendedor - Busca: ")
    print("1 - Por id")
    print("2 - Por nome")
    print("3 - Todos")
    print("0 - Voltar")

    escolha = input("Digite: ")
    while escolha not in ('0','1','2','3'):
        escolha = input("Opção inválida! Digite novamente: ")

    return escolha

# Retorna string
def pedir_cpf():
    cpf = input("Informe o CPF: ")
    while cpf == "":
        cpf = input("CPF inválido! Digite novamente: ")
    return cpf

# Retorna id, int
def pedir_id():
    id_invalido = True

    while id_invalido:
        try:
            id = int(input("Digite o id: "))
            id_invalido = False
        except ValueError:
            print("Id inválido! Digite novamente. ")

    return id

# Retorna tupla de string
def pedir_mes_ano():
    mes = input("Digite o mês: ")
    while mes not in ("01","02","03","04","05","06","07","08","09","10","11","12"):
        mes = input("Mês inválido! Digite novamente: ")
    ano = input("Digite o ano: ")
    while ano not in ("2022", "2023"):
        ano = input("Ano inválido! Digite novamente: ")
    return (mes, ano)

# Retorna string
def pedir_nome():
    nome = input("Digite o nome: ")
    while nome == "":
        nome = input("Nome inválido! Digite novamente: ")
    return nome

# Retorna True ou False
def tem_certeza():
    print("Tem certeza que deseja realizar essa operação? (s/n)")
    escolha = input("Digite s ou n: ")
    while escolha not in ("s", "n"):
        escolha = input("Opção inválida! Digite novamente: ")

    if escolha == "s":
        return True
    return False

# Retorna coluna em string e o valor em seu devido tipo
def update_cliente():
    colunas = {'1': 'nome',
               '2': 'cpf',
               '3': 'is_flamengo',
               '4': 'assiste_one_piece',
               '5': 'cidade_natal'}
    for coluna in colunas:
        print(f"{coluna}: {colunas[coluna]}")
    
    c = input("Digite o número da coluna que deseja atualizar: ")
    while c not in ('1','2','3','4','5'):
        c = input("Opção inválida, digite novamente: ")

    if c == '1' or c == '2' or c == '5':
        valor = input("Digite o novo valor: ")
        while valor == "":
            valor = input("Valor inválido! Digite novamente: ")
        return colunas[c], valor

    if c == '3' or c == '4':
        valor = -1
        while valor not in (0,1):
            try:
                valor = int(input("Digite o novo valor: "))
            except ValueError:
                print("Valor inválido!")
        return colunas[c], valor

# Retorna coluna em string e o valor em seu devido tipo
def update_compra():
    print("Que tipo de informação deseja atualizar? ")
    tabela = input("Da compra (c) ou do pagamento (p)? ")

    while tabela not in ('c', 'p'):
        tabela = input("Opção inválida! Digite novamente: ")

    if tabela == 'c':
        colunas = {'1': 'id_vendedor',
                   '2': 'id_cliente',
                   '3': 'status_da_compra',
                   '4': 'data_da_compra'}
        
        for coluna in colunas:
            print(f"{coluna}: {colunas[coluna]}")

        c = input("Digite o número da coluna que deseja atualizar: ")
        while c not in ('1','2','3','4'):
            c = input("Opção inválida, digite novamente: ")

        if c == '1' or c == '2':
            while True:
                try:
                    valor = int(input("Digite o novo valor: "))
                    return tabela, colunas[c], valor
                except ValueError:
                    print("Valor inválido! Digite novament. ")
        
        if c == '3':
            print("Opções: Confirmada, Aguardando confirmação, Cancelada")
            valor = input("Digite o novo status: ")
            while valor not in ('Confirmada', 'Aguardando confirmação', 'Cancelada'):
                valor = input("Valor inválido! Digite novamente: ")
            return tabela, colunas[c], valor

        if c == '4':
            print("Digite no formato aaaa-mm-dd")
            valor = input("Digite a data: ")
            while valor == "":
                valor = input("Data inválida! Digite novamente: ")
            return tabela, colunas[c], valor
        
    if tabela == 'p':
        colunas = {'1': 'forma_de_pagamento',
                   '2': 'status_do_pagamento'}

        for coluna in colunas:
            print(f"{coluna}: {colunas[coluna]}")
        
        c = input("Digite o número da coluna que deseja atualizar: ")
        while c not in ('1','2'):
            c = input("Digite o número da coluna que deseja atualizar: ")

        if c == '1':
            print("Opções: Dinheiro, Cartão de Crédito, Cartão de Débito, Pix, A definir")
            valor = input("Digite o novo status: ")
            while valor not in ('Dinheiro', 'Cartão de Crédito', 'Cartão de Débito', 'Pix', 'A definir'):
               valor = input("Forma inválida! Digite novamente: ")
            return tabela, colunas[c], valor

        if c == '2':
            print("Opções: Confirmado, Pendente, Cancelado, Reembolsado")
            valor = input("Digite o novo status: ")
            while valor not in ('Confirmado', 'Pendente', 'Cancelado', 'Reembolsado'):
                valor = input("Status inválido! Digite novamente: ")
            return tabela, colunas[c], valor

# Retorna coluna em string e o valor em seu devido tipo
def update_produto():
    colunas = {'1': 'nome',
               '2': 'preco',
               '3': 'estoque',
               '4': 'categoria',
               '5': 'local_de_fabricacao'}
    for coluna in colunas:
        print(f"{coluna}: {colunas[coluna]}")
    
    c = input("Digite o número da coluna que deseja atualizar: ")
    while c not in ('1','2','3','4','5'):
        c = input("Digite o número da coluna que deseja atualizar: ")

    if c == '1' or c == '5':
        valor = input("Digite o novo valor: ")
        while valor == "":
            valor = input("Valor inválido! Digite novamente: ")
        return colunas[c], valor
    
    if c == '2':
        valor_invalido = True
        while valor_invalido:
            try:
                valor = float(input("Digite o novo valor: "))
                valor_invalido = False
            except ValueError:
                print("Valor inválido!")
            if valor <= 0:
                print("Valor inválido!")
        return colunas[c], valor

    if c == '3':
        valor_invalido = True
        while valor_invalido:
            try:
                valor = int(input("Digite o novo valor: "))
                valor_invalido = False
            except ValueError:
                print("Valor inválido!")
            if valor < 0:
                print("Valor inválido!")
        return colunas[c], valor
    
    if c == '4':
        valor = input("Digite v para Vestuário e o para Outros: ")
        while valor not in ('v', 'o'):
            valor = input("Valor inválido! Digite novamente: ")
        if valor == 'v':
            valor = 'Vestuário'
        else:
            valor = 'Outros'
        return colunas[c], valor

# Retorna coluna em string e o valor em seu devido tipo
def update_vendedor():
    colunas = {'1': 'nome',
               '2': 'cpf',
               '3': 'situacao'}
    for coluna in colunas:
        print(f"{coluna}: {colunas[coluna]}")

    c = input("Digite o número da coluna que deseja atualizar: ")
    while c not in ('1','2','3','4','5'):
        c = input("Digite o número da coluna que deseja atualizar: ")

    if c == '1' or c == '2':
        valor = input("Digite o novo valor: ")
        while valor == "":
            valor = input("Valor inválido! Digite novamente: ")
        return colunas[c], valor

    if c == '3':
        print("Opções: Ativo, De férias, Afastado, Ex-colaborador")
        valor = input("Digite o novo status: ")
        while valor not in ('Ativo', 'De férias', 'Afastado', 'Ex-colaborador'):
            valor = input("Valor inválido! Digite novamente: ")
        return colunas[c], valor