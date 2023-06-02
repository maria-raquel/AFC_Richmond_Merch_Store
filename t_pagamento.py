class Table_Pagamento:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Pagamento(
                id_compra INT NOT NULL,
                total FLOAT NOT NULL,
                desconto_aplicado FLOAT DEFAULT 0,
                total_pos_desconto float GENERATED ALWAYS AS (total - desconto_aplicado),
                forma_de_pagamento SET ('Dinheiro', 'Cartão de Crédito', 
                                        'Cartão de Débito', 'Pix', 'Boleto', 'A definir'),
                status_do_pagamento SET ('Confirmado', 'Pendente', 'Cancelado', 'Reembolsado'),

                PRIMARY KEY (id_compra),
                FOREIGN KEY (id_compra) REFERENCES Compra(id)
            );
        ''')
        self.connection.commit()

    def create(self, id_compra, total, desconto_aplicado, forma_de_pagamento, status_do_pagamento):
        try:
            self.cursor.execute(f'''
                INSERT INTO Pagamento(id_compra, total, desconto_aplicado, forma_de_pagamento, status_do_pagamento)
                VALUES ({id_compra}, {total}, {desconto_aplicado}, '{forma_de_pagamento}', '{status_do_pagamento}');
                ''')
            self.connection.commit()
            return 1
        except:
            return 0
    
    def read(self, id_compra):
        try:
            self.cursor.execute(f'''
                SELECT * FROM Pagamento WHERE id_compra = {id_compra};
                ''')
            return self.cursor.fetchone()
        except:
            return 0
    
    def read_all(self):
        try:
            self.cursor.execute('''
                SELECT * FROM Pagamento;
                ''')
            return self.cursor.fetchall()
        except:
            return 0
    
    def read_all_confirmado(self):
        try:
            self.cursor.execute('''
                SELECT * FROM Pagamento WHERE status_do_pagamento = 'Confirmado';
                ''')
            return self.cursor.fetchall()
        except:
            return 0
    
    def update(self, id, coluna, valor):
        try:
            if type(valor) == str:
                self.cursor.execute(f'''
                    UPDATE Pagamento SET {coluna} = '{valor}' WHERE id_compra = {id};
                    ''')
            else:
                self.cursor.execute(f'''
                    UPDATE Pagamento SET {coluna} = {valor} WHERE id_compra = {id};
                    ''')
            self.connection.commit()
            return 1
        except:
            return 0
        
    def delete(self, id):
        try:
            self.cursor.execute(f'''
            UPDATE Compra SET status_do_pagamento = 'Cancelado' WHERE id_compra = {id};
            ''')
            self.connection.commit()
            return 1
        except:
            return 0