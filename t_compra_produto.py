class Table_Compra_Produto:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS Produto_Compra(
                id_compra INT NOT NULL,
                id_produto INT NOT NULL,
                quantidade INT NOT NULL,

                CONSTRAINT PK_Produto_Compra PRIMARY KEY (id_compra,id_produto),
                FOREIGN KEY (id_compra) REFERENCES Compra(id),
                FOREIGN KEY (id_produto) REFERENCES Produto(id)
            );
        ''')
        self.connection.commit()
    
    def create(self, id_compra, id_produto, quantidade):
        try:
            self.cursor.execute(f'''
                INSERT INTO Produto_Compra(id_compra, id_produto, quantidade)
                VALUES ({id_compra}, {id_produto}, {quantidade});
                ''')
            self.connection.commit()
            return 1
        except:
            return 0
    
    def read(self, id_compra, id_produto):
        try:
            self.cursor.execute(f'''
                SELECT Produto_Compra.id_compra, 
                Produto_Compra.id_produto,
                Produto.nome, Produto.preco,
                Produto_Compra.quantidade
                FROM Produto INNER JOIN Produto_Compra
                ON Produto.id = Produto_Compra.id_produto
                WHERE id_compra = {id_compra} 
                AND id_produto = {id_produto};
                ''')
            return self.cursor.fetchone()[0]
        except:
            return 0
        
    def read_all_from_compra(self, id_compra):
        try:
            self.cursor.execute(f'''
                SELECT Produto_Compra.id_compra, 
                Produto_Compra.id_produto,
                Produto.nome, Produto.preco,
                Produto_Compra.quantidade
                FROM Produto INNER JOIN Produto_Compra
                ON Produto.id = Produto_Compra.id_produto
                WHERE id_compra = {id_compra};
                ''')
            return self.cursor.fetchall()
        except:
            return 0
        
    def return_total_compra(self, id_compra):
        try:
            self.cursor.execute(f'''
                SELECT SUM(quantidade * preco) FROM Produto_Compra
                INNER JOIN Produto ON Produto_Compra.id_produto = Produto.id
                WHERE id_compra = {id_compra};
                ''')
            total = self.cursor.fetchone()[0]
            return round(total, 2)
        except:
            return 0