class Table_Produto:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Produto (
                id INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(255) NOT NULL,
                preco FLOAT NOT NULL,
                estoque INT NOT NULL DEFAULT 0,
                categoria SET ('Vestuário', 'Outros'),
                local_de_fabricacao VARCHAR(255),
                disponibilidade BOOLEAN DEFAULT TRUE,

                PRIMARY KEY (id)
            );
        ''')
        self.connection.commit()
        
    def create(self, nome, preco, estoque, categoria, local_de_fabricacao, disponibilidade):
        try:
            self.cursor.execute(f'''
                INSERT INTO Produto (nome, preco, estoque, categoria, local_de_fabricacao, disponibilidade)
                VALUES ('{nome}', {preco}, {estoque}, '{categoria}', '{local_de_fabricacao}', {disponibilidade});
            ''')
            self.connection.commit()
            return 1
        except:
            return 0

    def delete(self, id):
        try: 
            self.cursor.execute(f'''
            UPDATE Produto SET disponibilidade = 0 WHERE id = {id};
            ''')
            self.connection.commit()
            return 1
        except:
            return 0

    def read_all(self):
        try:
            self.cursor.execute(f'''
            SELECT id, nome, preco, estoque, categoria, local_de_fabricacao, 
            disponibilidade FROM Produto;
            ''')
            return self.cursor.fetchall()
        except:
            return 0

    def read_all_available(self):
        try:
            self.cursor.execute(f'''
            SELECT id, nome, preco, estoque, categoria, local_de_fabricacao, 
            disponibilidade FROM Produto WHERE disponibilidade = 1;
            ''')
            return self.cursor.fetchall()
        except:
            return 0

    def read_by_category(self, categoria):
        try:
            self.cursor.execute(f'''
            SELECT id, nome, preco, estoque, categoria, local_de_fabricacao, 
            disponibilidade FROM Produto WHERE categoria = '{categoria}';
            ''')
            return self.cursor.fetchall()
        except:
            return 0   

    def read_by_id(self, id):
        try:
            self.cursor.execute(f'''
            SELECT id, nome, preco, estoque, categoria, local_de_fabricacao, 
            disponibilidade FROM Produto WHERE id = {id};
            ''')
            return self.cursor.fetchone()
        except:
            return 0

    def read_by_local(self, local):
        try:
            self.cursor.execute(f'''
            SELECT id, nome, preco, estoque, categoria, local_de_fabricacao, 
            disponibilidade FROM Produto WHERE local_de_fabricacao = '{local}';
            ''')
            return self.cursor.fetchall()
        except:
            return 0

    def read_by_name(self, name):
        try:
            self.cursor.execute(f'''
            SELECT id, nome, preco, estoque, categoria, local_de_fabricacao, 
            disponibilidade FROM Produto WHERE nome LIKE '%{name}%';
            ''')
            return self.cursor.fetchall()
        except:
            return 0
       
    def read_by_price(self, min, max):
        if min != max:
            try:
                self.cursor.execute(f'''
                SELECT id, nome, preco, estoque, categoria, local_de_fabricacao, 
                disponibilidade FROM Produto WHERE preco > {min} AND preco < {max};
                ''')
                return self.cursor.fetchall()
            except:
                return 0
            
        if min == max:
            try:
                self.cursor.execute(f'''
                SELECT id, nome, preco, estoque, categoria, local_de_fabricacao, 
                disponibilidade FROM Produto WHERE CAST(preco AS DECIMAL(10,2)) = {min};
                ''')
                return self.cursor.fetchall()
            except:
                return 0
        
    def return_estoque(self, id):
        try:
            self.cursor.execute(f'''
            SELECT estoque FROM Produto WHERE id = {id};
            ''')
            return self.cursor.fetchone()[0]
        except:
            return 0

    def update(self, id, coluna, valor):
        try:
            if type(valor) == str:
                self.cursor.execute(f'''
                UPDATE Produto SET {coluna} = "{valor}" WHERE id = {id};
                '''
                )
            else:
                self.cursor.execute(f'''
                UPDATE Produto SET {coluna} = {valor} WHERE id = {id};
                '''
                )
            self.connection.commit()
            return 1
        except:
            return 0
               
    def validate_id(self, id):
        try:
            self.cursor.execute(f'''
            SELECT id FROM Produto WHERE id = {id};
            ''')
            return self.cursor.fetchone()[0]
        except:
            return 0