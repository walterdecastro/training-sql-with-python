from mysql_connector import mycursor, mydb # Devemos agora importar do arquivo my_connector.py o objeto mycursor e o mydb criado nele
import os # Importa o módulo os

clear = lambda: os.system('cls') # Através de uma função lambda criamos uma função clear() para limpar o terminal

print("""
    U - Buscar usuários
    D - Buscar destinos
    R - Buscar reservas""")
print()
opt_menu = input("Digite uma opção: ").upper()

if opt_menu == 'U':
    mycursor.execute("SELECT * FROM usuarios")
    registros = mycursor.fetchall()
    clear()
    print()
    for usuarios in registros:
        print("ID: ", usuarios[0])
        print("Nome: ", usuarios[1])
        print("Email: ", usuarios[2])
        print("Cidade: ", usuarios[3])
        print("Data de Nascimento: ", usuarios[4])
    print()
if opt_menu == 'D':
    mycursor.execute("SELECT * FROM destinos")
    registros = mycursor.fetchall()
    clear()
    print()
    for destinos in registros:
        print("ID: ", destinos[0])
        print("Nome: ", destinos[1])
        print("Descrição: ", destinos[2])
    print()

if opt_menu == 'R':
    mycursor.execute("SELECT * FROM reservas")
    registros = mycursor.fetchall()
    clear()
    print()
    for reservas in registros:
        print("ID: ", reservas[0])
        print("Usuario: ", reservas[1])
        print("Destino: ", reservas[2])
        print("Data: ", reservas[3])
        print("Status ", reservas[4])
    print()