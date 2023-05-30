import mysql as ms

class Table_Vendedor:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Vendedor(
                id INT NOT NULL AUTO_INCREMENT,
                cpf VARCHAR(255) NOT NULL UNIQUE,
                nome VARCHAR(255) NOT NULL,
                situacao SET ('Ativo', 'De ferias', 'Afastado', 'Ex-colaborador') DEFAULT 'Ativo',

                PRIMARY KEY (id)
            );
        ''')
        self.connection.commit()

    def create(self, cpf, nome, situacao):
        try:
            self.cursor.execute(f'''
                INSERT INTO Vendedor (cpf, nome, situacao) 
                VALUES ('{cpf}', '{nome}', '{situacao}')
            ''')
            self.connection.commit()
            return 1
        except:
            return 0
    
    def read_by_id(self, id):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Vendedor WHERE id = {id};
            ''')
            return self.cursor.fetchone()
        except:
            return 0
    
    def read_by_cpf(self, cpf):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Vendedor WHERE cpf = '{cpf}';
            ''')
            return self.cursor.fetchone()
        except:
            return 0
    
    def read_by_name(self, name):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Vendedor WHERE nome LIKE '%{name}%';
            ''')
            return self.cursor.fetchall()
        except:
            return 0
        
    def read_all_active(self):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Vendedor WHERE situacao = 'Ativo';
            ''')
            return self.cursor.fetchall()
        except:
            return 0
        
    def read_all(self):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Vendedor;
            ''')
            return self.cursor.fetchall()
        except:
            return 0

    def update(self, id, coluna, valor):
        try:
            if type(valor) == str:
                self.cursor.execute(f'''
                UPDATE Vendedor SET {coluna} = "{valor}" WHERE id = {id};
                ''')
            else:
                self.cursor.execute(f'''
                UPDATE Vendedor SET {coluna} = {valor} WHERE id = {id};
                ''')
            self.connection.commit()
            return 1
        except:
            return 0

    def delete(self, id):
        try: 
            self.cursor.execute(f'''
            UPDATE Vendedor SET situacao = 'Ex-colaborador' WHERE id = {id};
            ''')
            self.connection.commit()
            return 1
        except:
            return 0