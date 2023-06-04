CREATE SCHEMA AFC_Richmond_Merch_Store

CREATE TABLE Produto (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    preco FLOAT NOT NULL,
    estoque INT NOT NULL DEFAULT 0,
    categoria SET ('Vestuário', 'Outros'),
    local_de_fabricacao VARCHAR(255),
    disponibilidade BOOLEAN DEFAULT TRUE,

    PRIMARY KEY (id)
);

CREATE TABLE Cliente (
    id INT NOT NULL AUTO_INCREMENT,
    cpf VARCHAR(255) NOT NULL UNIQUE,
    nome VARCHAR(255) NOT NULL,
    is_flamengo BOOLEAN DEFAULT False,
    assiste_one_piece BOOLEAN DEFAULT False,
    cidade_natal VARCHAR(255),

    PRIMARY KEY (id)
);

INSERT INTO Cliente (cpf, nome, is_flamengo, assiste_one_piece, cidade_natal)
VALUES ('0', 'Sem cadastro', 0, 0, 'Nao informado');

CREATE TABLE Vendedor(
    id INT NOT NULL AUTO_INCREMENT,
    cpf VARCHAR(255) NOT NULL UNIQUE,
    nome VARCHAR(255) NOT NULL,
    situacao SET ('Ativo', 'De férias', 'Afastado', 'Ex-colaborador') DEFAULT 'Ativo',

    PRIMARY KEY (id)
);

CREATE TABLE Compra(
    id INT NOT NULL AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_vendedor INT NOT NULL,
    data_da_compra DATE NOT NULL,
    status_da_compra SET ('Confirmada', 'Aguardando confirmação', 'Cancelada'),

    PRIMARY KEY (id),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
    FOREIGN KEY (id_vendedor) REFERENCES Vendedor(id)
);

CREATE TABLE Produto_Compra(
    id_compra INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,

    CONSTRAINT PK_Produto_Compra PRIMARY KEY (id_compra,id_produto),
    FOREIGN KEY (id_compra) REFERENCES Compra(id),
    FOREIGN KEY (id_produto) REFERENCES Produto(id)
);

CREATE TABLE Pagamento(
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