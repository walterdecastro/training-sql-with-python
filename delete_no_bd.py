from mysql_connector import mycursor, mydb # Devemos agora importar do arquivo my_connector.py o objeto mycursor e o mydb criado nele
import os # Importa o módulo os

clear = lambda: os.system('cls') # Através de uma função lambda criamos uma função clear() para limpar o terminal

# Dentro do contexto para treinarmos, vou apenas implementar a lógica para a tabela de usuários. Imaginemos que as tabelas destinos e registros sejam do escopo do adm do sistemas, portanto, só cabe a ele atualiza-los

print()
nome = input("Digite o seu nome: ")
clear()
print(f"Olá, {nome}")
print()
opt = input("Gostaria de deletar seu registro? S ou N: ").upper()
clear()
if opt == 'S':
    nome = input("Confirme o seu nome: ")
    mycursor.execute(f"DELETE FROM usuarios WHERE nome = '{nome}'")
    conf = input(f"{nome}, quer realmente fazer isto?: S ou N: ").upper()
    if conf == "S":
        mydb.commit()
    print("Registro apagado!")