import mysql as ms

class Table_Compra:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Compra(
                id INT NOT NULL AUTO_INCREMENT,
                id_cliente INT NOT NULL,
                id_vendedor INT NOT NULL,
                data_da_compra DATE NOT NULL,
                status_da_compra SET ('Confirmada', 'Aguardando confirmação', 'Cancelada'),

                PRIMARY KEY (id),
                FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
                FOREIGN KEY (id_vendedor) REFERENCES Vendedor(id)
            );
        ''')
        self.connection.commit()
    
    def create(self, id_cliente, id_vendedor, data_da_compra, status_da_compra):
        try:
            self.cursor.execute(f'''
                INSERT INTO Compra(id_cliente, id_vendedor, data_da_compra, status_da_compra)
                VALUES ({id_cliente}, {id_vendedor}, '{data_da_compra}', '{status_da_compra}');
                ''')
            self.connection.commit()
            return 1
        except:
            return 0
        
    def read(self, id):
        try:
            self.cursor.execute(f'''
                SELECT * FROM Compra WHERE id = {id};
                ''')
            return self.cursor.fetchone()
        except:
            return 0
        
    def read_all(self):
        try:
            self.cursor.execute('''
                SELECT * FROM Compra;
                ''')
            return self.cursor.fetchall()
        except:
            return 0

    def read_all_from_cliente(self, id_cliente):
        try:
            self.cursor.execute(f'''
                SELECT * FROM Compra WHERE id_cliente = {id_cliente};
                ''')
            return self.cursor.fetchall()
        except:
            return 0
        
    def read_all_from_vendedor(self, id_vendedor):
        try:
            self.cursor.execute(f'''
                SELECT * FROM Compra WHERE id_vendedor = {id_vendedor};
                ''')
            return self.cursor.fetchall()
        except:
            return 0
        
    def read_all_from_data(self, data_da_compra):
        try:
            self.cursor.execute(f'''
                SELECT * FROM Compra WHERE data_da_compra LIKE '%{data_da_compra}%';
                ''')
            return self.cursor.fetchall()
        except:
            return 0
        
    def return_id(self, id_cliente, id_vendedor, data_da_compra, status_da_compra):
        try:
            self.cursor.execute(f'''
                SELECT id FROM Compra WHERE id_cliente = {id_cliente} 
                    AND id_vendedor = {id_vendedor} 
                    AND data_da_compra = '{data_da_compra}' 
                    AND status_da_compra = '{status_da_compra}';
                ''')
            return self.cursor.fetchone()[0]
        except:
            return 0
                
    def update(self, id, coluna, valor):
        try:
            if type(valor) == str:
                self.cursor.execute(f'''
                    UPDATE Compra SET {coluna} = '{valor}' WHERE id = {id};
                    ''')
            else:
                    self.cursor.execute(f'''
                    UPDATE Compra SET {coluna} = {valor} WHERE id = {id};
                    ''')
            self.connection.commit()
            return 1
        except:
            return 0
        
    def delete(self, id):
        try:
            self.cursor.execute(f'''
            UPDATE Compra SET status_da_compra = 'Cancelada' WHERE id = {id};
            ''')
            self.connection.commit()
            return 1
        except:
            return 0
        
    def validate_id(self, id):
        try:
            self.cursor.execute(f'''
                SELECT id FROM Compra WHERE id = {id};
                ''')
            return self.cursor.fetchone()[0]
        except:
            return 0