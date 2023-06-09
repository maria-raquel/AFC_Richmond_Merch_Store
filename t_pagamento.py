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
                                        'Cartão de Débito', 'Pix', 'A definir'),
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
                SELECT id_compra, total, desconto_aplicado, total_pos_desconto,
                status_do_pagamento, forma_de_pagamento
                FROM Pagamento WHERE id_compra = {id_compra};
                ''')
            return self.cursor.fetchone()
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
               
    def confirm_payment(self, id):
        try:
            self.cursor.execute(f'''
            CALL Confirmar_compra({id});
            ''')
            self.connection.commit()
            return 1
        except:
            return 0
    
    def cancel_payment(self, id):
        try:
            self.cursor.execute(f'''
            CALL Cancelar_compra({id});
            ''')
            self.connection.commit()
            return 1
        except:
            return 0
        
    def refund_payment(self, id):
        try:
            self.cursor.execute(f'''
            CALL Reembolsar_compra({id});
            ''')
            self.connection.commit()
            return 1
        except:
            return 0
        
    def return_status_de_pagamento(self, id):
        try:
            self.cursor.execute(f'''
                SELECT status_do_pagamento FROM Pagamento WHERE id_compra = {id};
                ''')
            return str(self.cursor.fetchone()[0])
        except:
            return 0