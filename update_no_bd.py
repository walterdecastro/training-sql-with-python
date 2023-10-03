from mysql_connector import mycursor, mydb # Devemos agora importar do arquivo my_connector.py o objeto mycursor e o mydb criado nele
import os # Importa o módulo os

clear = lambda: os.system('cls') # Através de uma função lambda criamos uma função clear() para limpar o terminal

# Dentro do contexto para treinarmos, vou apenas implementar a lógica para a tabela de usuários. Imaginemos que as tabelas destinos e registros sejam do escopo do adm do sistemas, portanto, só cabe a ele atualiza-los

print()
print("### Editar usuário ###")
print()
print("""
    N - Editar nome
    E - Editar Endereço""")
print()
opt_edit = input("Digite uma opção: ").upper()

if(opt_edit == 'N'):
    clear()
    # Solicita o nome atual e o novo nome para ser atualizado
    nome_atual = input("Digite o seu nome atual: ")
    nome_novo = input("Digite o novo nome: ")

    # Faz a alteração passando os atributos através de fstring
    mycursor.execute(f"UPDATE usuarios SET nome = '{nome_novo}' WHERE nome = '{nome_atual}'")
    conf = input("Confirma a alteração? S ou N ").upper() # Confirma a alteração
    if conf == 'S':
        mydb.commit()# Executa a alteração

elif (opt_edit == 'E'):
    clear()
    endereco_atual = input("Digite o seu endereço atual: ")
    endereco_novo = input("Digite o seu novo endereço: ")

    mycursor.execute(f"UPDATE usuarios SET endereco = '{endereco_novo}' WHERE endereco = '{endereco_atual}'")
    conf = input("Confirma a alteração? S ou N ").upper()
    if conf == 'S':
        mydb.commit()