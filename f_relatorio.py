import connect_to_DB
import f_print as fp
import t_cliente as cl
import t_compra as cm
import t_compra_produto as cp
import t_relatorio as r
import t_vendedor as v
from PIL import Image, ImageDraw, ImageFont

connection = connect_to_DB.connect()
Vendedor = v.Table_Vendedor(connection)
Consulta = r.Consulta_Relatorio(connection)
Compra = cm.Table_Compra(connection)
Compra_Produto = cp.Table_Compra_Produto(connection)
Cliente = cl.Table_Cliente(connection)

meses = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
             '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
             '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}

def consultas(id, mes, ano):
    vendedor = Vendedor.read_by_id(id)
    info1 = Consulta.n_de_vendas(id, ano, mes)
    info2 = Consulta.valor_total_vendido(id, ano, mes)
    info3 = Consulta.dia_maior_arrecadacao(id, ano, mes)
    info4 = Consulta.top_produtos(id, ano, mes)
    info5 = Consulta.top_clientes(id, ano, mes)
    
    deu_ruim = False
    if not vendedor:
        deu_ruim = True
    if info1 == None or info2 == None or info3 == None or info4 == None or info5 == None:
        deu_ruim = True
    if deu_ruim:
        fp.mensagem_erro_ao_recuperar_info()
        return
    
    return vendedor, mes, ano, info1, info2, info3, info4, info5

def relatorio_terminal(vendedor, mes, ano, info1, info2, info3, info4, info5):    
    print("~~~~~~~~~~~ Relátorio Mensal ~~~~~~~~~~~")
    print(f"{meses[mes]} de {ano}")
    fp.info_vendedor(*vendedor)
    print(f"Total de vendas realizadas: {info1}")
    print("Total arrecadado: R$ %.2f" % info2)
    media = info2/info1 if info1 else 0
    print("Média de arrecadação por venda: R$ %.2f" % media)
    data = info3[0].strftime("%d/%m/%Y")
    print(f"Dia de maior arrecadação: {data}, R$ %.2f" % info3[1])
    print("----------------------------------------")
    print("Top 3 produtos mais vendidos:")
    print("ID | Nome | Quantidade")
    for produto in info4:
        print(f"{produto[0]} | {produto[1]} | {produto[2]}")
    print("----------------------------------------")
    print("Top 3 clientes deste vendedor:")
    print("ID | Nome | Compras feitas")
    for cliente in info5:
        print(f"{cliente[0]} | {cliente[1]} | {cliente[2]}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def relatorio_png(vendedor, mes, ano, info1, info2, info3, info4, info5):
    id, cpf, nome, situacao = vendedor
    situacao = str(situacao)[2:-2]

    # Carrega a imagem base
    image = Image.open("relatorio_files/relatorio_branco.png")
    draw = ImageDraw.Draw(image)

    # Define propriedades do texto
    font = ImageFont.truetype("relatorio_files/Gupter-Regular.ttf", 80)
    text_color = (0, 0, 0)

    # Define posição inicial do texto
    x = 100
    y = 600
    line_height = 90

        # Imprime as informações

    draw.text((x, y), f"Vendedor {id}:", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), f"Nome: {nome}; CPF: {cpf}; Situação: {situacao}", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), "----------------------------------------", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), f"{meses[mes]} de {ano}", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), f"Total de vendas realizadas: {info1}", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), f"Total arrecadado: R$ %.2f" % info2, font=font, fill=text_color)
    y += line_height

    media = info2/info1 if info1 else 0
    draw.text((x, y), f"Média de arrecadação por venda: R$ %.2f" % media, font=font, fill=text_color)
    y += line_height

    data = info3[0].strftime("%d/%m/%Y")
    draw.text((x, y), f"Dia de maior arrecadação: {data}, R$ %.2f" % info3[1], font=font, fill=text_color)
    y += line_height

    draw.text((x, y), "----------------------------------------", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), "Top 3 produtos mais vendidos:", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), "ID | Nome | Quantidade", font=font, fill=text_color)
    y += line_height

    for produto in info4:
        draw.text((x, y), f"{produto[0]} | {produto[1]} | {produto[2]}", font=font, fill=text_color)
        y += line_height

    draw.text((x, y), "----------------------------------------", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), "Top 3 clientes deste vendedor:", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), "ID | Nome | Compras feitas", font=font, fill=text_color)
    y += line_height

    for cliente in info5:
        draw.text((x, y), f"{cliente[0]} | {cliente[1]} | {cliente[2]}", font=font, fill=text_color)
        y += line_height

    # Salva a imagem
    image.save("relatorio_files/relatorio.png")

def recibo(id_compra):
    compra = Compra.read(id_compra)
    id_cliente = Compra.return_id_cliente(id_compra)
    cliente = Cliente.read_by_id(id_cliente)
    produtos = Compra_Produto.return_produtos_precos(id_compra)

    if not compra or not cliente or not produtos:
        return

    id, id_cliente, id_vendedor, data, status_c, total, desconto, total_pos_desconto, forma_de_pagamento, status_do_pagamento = compra
    id_cliente, cpf, nome, is_flamengo, assiste_one_piece, cidade_natal = cliente

    # Carrega a imagem base
    image = Image.open("relatorio_files/recibo_branco.png")
    draw = ImageDraw.Draw(image)

    # Define propriedades do texto
    font = ImageFont.truetype("relatorio_files/Gupter-Regular.ttf", 80)
    text_color = (0, 0, 0)

    # Define posição inicial do texto
    x = 100
    y = 600
    line_height = 90

    draw.text((x, y), f"Compra {id}:", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), f"Nome do cliente: {nome}; CPF: {cpf}", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), f"Id do vendedor: {id_vendedor}", font=font, fill=text_color)
    y += line_height

    status_c = str(status_c)[2:-2]

    draw.text((x, y), f"Data: {data}; Status da compra: {status_c}", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), f"Total: R$ %.2f" % total, font=font, fill=text_color)
    y += line_height

    if desconto:
        draw.text((x, y), "Desconto: R$ %.2f" % desconto, font=font, fill=text_color)
        y += line_height

        draw.text((x, y), "Total com desconto: R$ %.2f" % total_pos_desconto, font=font, fill=text_color)
        y += line_height

    status_do_pagamento = str(status_do_pagamento)[2:-2]
    forma_de_pagamento = str(forma_de_pagamento)[2:-2]

    draw.text((x, y), f"Status do pagamento: {status_do_pagamento}", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), f"Forma de pagamento: {forma_de_pagamento}", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), "----------------------------------------", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), "Produtos comprados:", font=font, fill=text_color)
    y += line_height

    draw.text((x, y), "Id | Produto | Quantidade | Preço", font=font, fill=text_color)
    y += line_height

    for produto in produtos:
        id_produto, quantidade, nome, preco = produto
        draw.text((x, y), f"{id_produto} | {nome} | {quantidade} | R$ %.2f" % preco, font=font, fill=text_color)
        y += line_height
    
    # Salva a imagem
    image.save("relatorio_files/recibo.png")