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
        total FLOAT NOT NULL,
        desconto_aplicado FLOAT DEFAULT 0,
        total_pos_desconto float GENERATED ALWAYS AS (compra.total - compra.desconto_aplicado),
        forma_de_pagamento SET ('Dinheiro', 'Cartao de Credito', 
                                'Cartao de Debito', 'Pix', 'Boleto', 'Fiado'),
        status_do_pagamento SET ('Confirmado', 'Pendente', 'Cancelado'),

        PRIMARY KEY (id),
        FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
        FOREIGN KEY (id_vendedor) REFERENCES Vendedor(id)
        );
        ''')
        self.connection.commit()
    
    def create(self, id_cliente, id_vendedor, data_da_compra, total, 
               desconto_aplicado, forma_de_pagamento, status_do_pagamento):
        try:
            self.cursor.execute(f'''
                INSERT INTO Compra(id_cliente, id_vendedor, data_da_compra, total, 
                desconto_aplicado, forma_de_pagamento, status_do_pagamento)
                VALUES ({id_cliente}, {id_vendedor}, '{data_da_compra}', {total}, 
                {desconto_aplicado}, '{forma_de_pagamento}', '{status_do_pagamento}');
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
        
    def read_all_pagamentos_pendentes(self):
        try:
            self.cursor.execute('''
                SELECT * FROM Compra WHERE status_do_pagamento = 'Pendente';
                ''')
            return self.cursor.fetchall()
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
            UPDATE Compra SET status_do_pagamento = 'Cancelado' WHERE id = {id};
            ''')
            self.connection.commit()
            return 1
        except:
            return 0