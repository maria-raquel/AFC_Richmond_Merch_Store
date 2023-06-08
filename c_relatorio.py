class Consulta_Relatorio:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

        
    def n_de_vendas(self, id, ano, mes):
        try:
            self.cursor.execute(f'''
                SELECT COUNT(*)
                FROM Compra
                WHERE id_vendedor = {id}
                AND data_da_compra LIKE "{ano}-{mes}%"
            ''')
            return self.cursor.fetchone()[0]
        except:
            return None
        
    def valor_total_vendido(self, id, ano, mes):
        try:
            self.cursor.execute(f'''
                SELECT SUM(Pagamento.total_pos_desconto)
                FROM Compra INNER JOIN Pagamento
                ON Compra.id = Pagamento.id_compra
                WHERE id_vendedor = {id}
                AND data_da_compra LIKE "{ano}-{mes}%"
            ''')
            return self.cursor.fetchone()[0]
        except:
            return None
        
    def dia_maior_arrecadacao(self, id, ano, mes):
        try:
            self.cursor.execute(f'''
                SELECT Compra.data_da_compra, SUM(Pagamento.total_pos_desconto)
                FROM Compra INNER JOIN Pagamento
                ON Compra.id = Pagamento.id_compra
                WHERE id_vendedor = {id}
                AND data_da_compra LIKE "{ano}-{mes}%"
                GROUP BY Compra.data_da_compra
                ORDER BY SUM(Pagamento.total_pos_desconto) DESC
                LIMIT 1
            ''')
            return self.cursor.fetchone()
        except:
            return None
        
    def dia_maior_arrecadacao(self, id, ano, mes):
        try:
            self.cursor.execute(f'''
                SELECT Produto.id, Produto.nome, SUM(Produto_Compra.quantidade)
                FROM ((Compra INNER JOIN Produto_Compra
                ON Compra.id = Produto_Compra.id_compra)
                INNER JOIN Produto
                ON Produto.id = Produto_Compra.id_produto)
                WHERE id_vendedor = {id}
                AND data_da_compra LIKE "{ano}-{mes}%"
                GROUP BY Produto.id
                ORDER BY SUM(Produto_Compra.quantidade) DESC
                LIMIT 3
            ''')
            return self.cursor.fetchone()
        except:
            return None