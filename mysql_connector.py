import mysql.connector # Importando as classes (módulos) mysql e connector

# Cria um objeto de conexão com o BD(Banco de Dados), recebendo como parâmetros o host, o usuário, a senha e, após criada a database, podemos passar ela como argumento também
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass123",
    #database="db_dio_santander_bootcamp"
)


# Através do método cursor() da classe connector criamos um manipulador das nossa consultas(querys). Usaremos o objeto
mycursor = mydb.cursor()

# Através do do método execute() do connector podemos passar uma string como parâmetro com as querys que queremos solicitar ao SGBD. Comente o código após executado e descomente o parâmetro database="db_dio_santander_bootcamp" do objeto mydb
"""mycursor.execute(
    "CREATE DATABASE db_dio_santander_bootcamp"
)"""

# Ao executarmos o comando abaixo podemos listar todas as databases do nosso SGBD. Por padrão, o MySQL cria alguns databases para o proprio uso do sistema
"""mycursor.execute(
    "SHOW DATABASES"
)"""

# Usamos o loop para percorrer a lista retornada pelo cursor 
"""for x in mycursor:
    print(x)"""

#print(type(x)) # Cada item da lista retornada pelo cursor é uma tupla

   