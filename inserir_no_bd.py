from mysql_connector import mycursor, mydb # Devemos agora importar do arquivo my_connector.py o objeto mycursor e o mydb criado nele
import os # Importa o módulo os

clear = lambda: os.system('cls') # Através de uma função lambda criamos uma função clear() para limpar o terminal

# Em nossa implementação, criaremos um sisteminha simples para inserir os registros no nosso banco de dados. Para isso, criamos um loop com um verificação para encerra-lo quando o usuário assim desejar

opt = "S" # Variável de verificação do loop while

while opt == "S":
    clear() # Usamos a função lambda que criamos acima para, a cada usuário criado no bd, o console(terminal) seja limpo(cls ou clear)
    print("\n## Populando o Banco de Dados ##")
    print()
    # Inserimos os dados do usuário atráves da função input() do Python
    nome = input("Digite seu nome: ")
    email = input("Digite o seu e-mail: ")
    endereco = input("Digite o seu endereço: ")
    data_digitada = input("Digite a data de nascimento (dd mm aaaa): ")
    # Dado que o formato padrão do MySQL para data é "aaaa-mm-dd", podemos pedir ao usuário digitar a data no formato convencional (brasileiro) e depois fazemos uma tratativo nesse dado. Segue abaixo:
    data_formato_br = data_digitada.split(" ") # Primeiro, tiramos os espaços da string digitada
    data_formato_mysql = data_formato_br[::-1] # O método split() nos retorna uma lista ["dd", "mm", "aaaa"]. Invertemos a posição dos itens da lista e obtemos ["aaaa", "mm", "dd"]
    data_nascimento_com_traco = ""
    for data in data_formato_mysql: # Aqui, devemos recriar uma string para passar para o nosso bd, com o formato de data padrão(MySQL), para tanto faremos um loop pela lista retornado ao usarmos o slicing (linha 21) concatenado os itens e um traço '-'
        data_nascimento_com_traco += data + '-'
        data_nascimento = data_nascimento_com_traco[0:10] # Surge um novo problemas com a concatenação, um traço a mais é colocado ao final da string, fazemos um slicing e ignoramos o último traço.
# Ao final, temos a variável data_nascimento no seguinte padrão "aaaa-mm-dd"
    
    # Para o comando INSERT, devemos uma variável para query em si e os valore que serão inseridos. Para o nosso sistemas os valores serão atribuídos de forma dinâmica
    sql = "INSERT INTO usuarios (nome, email, endereco, data_nascimento) VALUES (%s, %s, %s, %s)" # Os valores das variáveis serão atribuídos aos operadores %s da variável val
    val = (f"{nome}", f"{email}", f"{endereco}", f"{data_nascimento}") # Usamos fstring para atribuição dinâmica
    mycursor.execute(sql, val)
    mydb.commit() # Executa a query de INSERT
    print()
    opt = input("Digite \'s\' para continuar... \n").upper() # Solicita ao usuário se o sistema deve continuar inserindo dados no bd

