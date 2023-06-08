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
                cidade_natal VARCHAR(255),

                PRIMARY KEY (id)
            );
        ''')
        self.connection.commit()
    
    def create(self, cpf, nome, is_flamengo, assiste_one_piece, cidade_natal):
        try:
            self.cursor.execute(f'''
                INSERT INTO Cliente (cpf, nome, is_flamengo, assiste_one_piece, cidade_natal) 
                VALUES ('{cpf}', '{nome}', {is_flamengo}, {assiste_one_piece}, '{cidade_natal}')
            ''')
            self.connection.commit()
            return 1
        except:
            return 0
    
    def delete(self, id):
        try:
            self.cursor.execute(f'''
            CALL Apagar_cliente({id});
            ''')
            self.connection.commit()
            return 1
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

    def read_by_cpf(self, cpf):
        try:
            self.cursor.execute(f'''
            SELECT * FROM Cliente WHERE cpf = '{cpf}';
            ''')
            return self.cursor.fetchone()
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
        
    def return_desconto(self, id):
        try:
            self.cursor.execute(f'''
            SELECT is_flamengo FROM Cliente WHERE id = {id};
            ''')
            fla = self.cursor.fetchone()[0]
        except:
            return None
        
        try:
            self.cursor.execute(f'''
            SELECT assiste_one_piece FROM Cliente WHERE id = {id};
            ''')
            op = self.cursor.fetchone()[0]
        except:
            return None
        
        try:
            self.cursor.execute(f'''
            SELECT cidade_natal FROM Cliente WHERE id = {id};
            ''')
            if self.cursor.fetchone()[0] == 'Sousa':
                de_sousa = 1
            else: 
                de_sousa = 0
        except:
            return None
        
        return (fla + op + de_sousa) * 10/100
        
    def return_id(self, cpf):
        try:
            self.cursor.execute(f'''
            SELECT id FROM Cliente WHERE cpf = '{cpf}';
            ''')
            return self.cursor.fetchone()[0]
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
               
    def validate_id(self, id):
        try:
            self.cursor.execute(f'''
            SELECT id FROM Cliente WHERE id = {id};
            ''')
            return self.cursor.fetchone()[0]
        except:
            return 0