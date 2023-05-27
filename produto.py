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
        
    # lembrar de colocar alguns parametros opcionais
    #colocar try except 
    def create(self, nome, preco, estoque, categoria, local_de_fabricacao, disponibilidade):
        self.cursor.execute(f'''
            INSERT INTO produto (nome, preco, estoque, categoria, local_de_fabricacao, disponibilidade)
            VALUES ('{nome}', '{preco}', '{estoque}', '{categoria}', '{local_de_fabricacao}', '{disponibilidade}');
        ''')
        self.connection.commit()
        print("insert foi")

    # try catch
    def read(self, id):
        self.cursor.execute(f'''
        SELECT * FROM Produto WHERE id = {id};
        ''')
        return self.cursor.fetchone()

    # fazer read por nome

    def update(self, id, coluna, valor):
        print(f'''
        UPDATE Produto
        SET {coluna} = {valor} WHERE id = {id};
        '''
        )
        #print("update foi")