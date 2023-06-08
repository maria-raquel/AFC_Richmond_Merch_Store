import connect_to_DB
import f_print as fp
import t_relatorio as r
import t_vendedor as v

connection = connect_to_DB.connect()
Vendedor = v.Table_Vendedor(connection)
Consulta = r.Consulta_Relatorio(connection)

def relatorio_por_vendedor_por_mes(id, mes, ano):
    meses = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
             '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
             '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
    
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
