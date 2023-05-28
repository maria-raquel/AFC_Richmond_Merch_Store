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
            sexo SET ('M' , 'F', 'NB'),
            situacao SET ('ativo', 'de ferias', 'afastado', 'ex-colaborador') DEFAULT 'ativo',

            PRIMARY KEY (id)
            )
        ''')
        self.cursor.commit()

    def create(self, cpf, nome, sexo, situacao):
        try:
            self.cursor.execute(f'''
                INSERT INTO Vendedor (cpf, nome, sexo, situacao) 
                VALUES ({cpf}, {nome}, {sexo}, {situacao})
            '''
            )
            return self.connection.commit()
        except:
            return None
    
    def read_by_id(self, id):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Vendedor WHERE id = {id};
            ''')
            return self.cursor.fetchone()
        except:
            return None
    
    def read_by_name(self, name):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Vendedor WHERE nome LIKE '%{name}%';
            ''')
            return self.cursor.fetchall()
        except:
            return None
        
    def read_all_active(self):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Vendedor WHERE situacao = 'ativo';
            ''')
            return self.cursor.fetchall()
        except:
            return None
        
    def read_all(self):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Vendedor;
            ''')
            return self.cursor.fetchall()
        except:
            return None

    def update(self, id, coluna, valor):
        try:
            if type(valor) == str:
                self.cursor.execute(f'''
                UPDATE Vendedor SET {coluna} = "{valor}" WHERE id = {id};
                '''
                )
            else:
                self.cursor.execute(f'''
                UPDATE Vendedor SET {coluna} = {valor} WHERE id = {id};
                '''
                )
            return self.connection.commit()
        except:
            return None

    def delete(self, id):
        try: 
            self.cursor.execute(f'''
            UPDATE Vendedor SET situacao = 'ex-colaborador' WHERE id = {id};
            ''')
            return self.connection.commit()
        except:
            return None