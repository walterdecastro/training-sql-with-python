from mysql_connector import mycursor # Para organizar nosso código, vamos criar um arquivo para cada query ou grupo de querys. Para isso devemos importar do arquivo my_connector.py o objeto mycursor criado nele


# Cria as tabelas no bd usando o objeto mycursor. Após executado, comente esse trecho de código
"""mycursor.execute("CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário', email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail do usuário', endereco VARCHAR(50) COMMENT 'Endereço do usuário', data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário')")

mycursor.execute("CREATE TABLE destinos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255) NOT NULL COMMENT 'Nome do destino', descricao VARCHAR(255) NOT NULL COMMENT 'Descricao do destino')")

mycursor.execute("CREATE TABLE reservas (id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Identificar único para a tabela reservas', id_usuario INT COMMENT 'Referência ao ID do usuario que fez a reserva', id_destino INT COMMENT 'Referência ao ID do destino da reserva', data DATE COMMENT 'Data da reserva', status VARCHAR(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confirmada, pedente, cancelada, etc)')")"""

# Verifica quais as tabelas que existem no db selecionado
mycursor.execute("SHOW TABLES")

for table in mycursor:
    print(table)