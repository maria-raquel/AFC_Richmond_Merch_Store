import mysql as ms

class Table_Cliente:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cliente (
            id INT NOT NULL AUTO_INCREMENT,
            cpf VARCHAR(255) NOT NULL UNIQUE,
            nome VARCHAR(255) NOT NULL,
            is_flamengo BOOLEAN DEFAULT False,
            assiste_one_piece BOOLEAN DEFAULT False,
            data_nascimento DATE NOT NULL,
            sexo SET ('M' , 'F', 'NB'),
            cidade_natal VARCHAR(255),

            PRIMARY KEY (id)
        );
        ''')
        self.connection.commit()
    
    def create(self, cpf, nome, is_flamengo, assiste_one_piece, data_nascimento, sexo, cidade_natal):
        try:
            self.cursor.execute(f'''
                INSERT INTO Cliente (cpf, nome, is_flamengo, assiste_one_piece, data_nascimento, sexo, cidade_natal) 
                VALUES ('{cpf}', '{nome}', {is_flamengo}, {assiste_one_piece}, '{data_nascimento}', '{sexo}', '{cidade_natal}')
            '''
            )
            self.connection.commit()
            return 1
        except:
            return 0
    
    def read_by_id(self, id):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Cliente WHERE id = {id};
            ''')
            return self.cursor.fetchone()
        except:
            return 0
    
    def read_by_name(self, name):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Cliente WHERE nome LIKE '%{name}%';
            ''')
            return self.cursor.fetchall()
        except:
            return 0
        
    def read_by_cpf(self, cpf):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Cliente WHERE cpf = '{cpf}';
            ''')
            return self.cursor.fetchone()
        except:
            return 0
        
    def read_all(self):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Cliente;
            ''')
            return self.cursor.fetchall()
        except:
            return 0
    
    def update(self, id, coluna, valor):
        try:
            if type(valor) == str:
                self.cursor.execute(f'''
                UPDATE Cliente SET {coluna} = '{valor}' WHERE id = {id};
                ''')
            else:
                self.cursor.execute(f'''
                UPDATE Cliente SET {coluna} = {valor} WHERE id = {id};
                ''')
            self.connection.commit()
            return 1
        except:
            return 0
        
    def delete(self, id):
        try:
            self.cursor.execute(f'''
            DELETE FROM Cliente WHERE id = {id};
            ''')
            self.connection.commit()
            return 1
        except:
            return 0