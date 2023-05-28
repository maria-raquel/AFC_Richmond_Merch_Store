import mysql as ms

class Table_Produto:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produto (
                id INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(255) NOT NULL,
                preco FLOAT NOT NULL,
                estoque INT NOT NULL DEFAULT 0,
                categoria SET ('Vestuario', 'Outros'),
                local_de_fabricacao VARCHAR(255),
                disponibilidade BOOLEAN DEFAULT TRUE,

                PRIMARY KEY (id)
            )
        ''')

        self.cursor.execute('''
        SHOW COLUMNS FROM produto
        ''')
        colunas_info = self.cursor.fetchall()
        self.colunas = []
        for coluna in colunas_info:
            self.colunas.append(coluna[0])        
        
    def create(self, nome, preco, estoque, categoria, local_de_fabricacao, disponibilidade):
        try:
            self.cursor.execute(f'''
                INSERT INTO produto (nome, preco, estoque, categoria, local_de_fabricacao, disponibilidade)
                VALUES ('{nome}', '{preco}', '{estoque}', '{categoria}', '{local_de_fabricacao}', '{disponibilidade}');
            ''')
            return self.connection.commit()
        except:
            return 0
        
    def read_by_id(self, id):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Produto WHERE id = {id};
            ''')
            return self.cursor.fetchone()
        except:
            return None

    def read_by_name(self, name):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Produto WHERE nome LIKE '%{name}%';
            ''')
            return self.cursor.fetchall()
        except:
            return None
        
    def read_all_available(self):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Produto WHERE disponibilidade = 1;
            ''')
            return self.cursor.fetchall()
        except:
            return None
        
    def read_all(self):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Produto;
            ''')
            return self.cursor.fetchall()
        except:
            return None

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
            return self.connection.commit()
        except:
            return None
        
    def delete(self, id):
        try: 
            self.cursor.execute(f'''
            UPDATE Produto SET disponibilidade = 0 WHERE id = {id};
            ''')
            return self.connection.commit()
        except:
            return None