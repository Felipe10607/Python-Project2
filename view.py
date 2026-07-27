from models import *
from dao import *
from Controller import *



print('-----MENU------')
print('Entre no site')
email = input('digite o seu gmail: ')
a = Pessoa(None,email)
print('REALIZAR O LOGIN')
loginu = input("digite seu login: ")
senhau = input("insira a senha: ")
u = Usuario(a,loginu,senhau)
usuarioController.fazer_login(u)
"""
print('1. Criar o seu cadastro')
print('2. Criar o seu usuário')
print('3. Apagar cadastro')
print('4. Apagar usuário')
print('5. Consultar seus logins')
print('6. Sair')
while True:
    x =  int(input("Insira o valor :"))
    if x == 1:
        nome = input("Digite o seu nome :")
        email = input("Digite o seu email :")
        pessoaController.cadastra(nome,email)

    if x == 2:
        email2 = input("Digite seu email cadastrado :")
        login = input("Digite o seu login :")
        senha = input("Insira a senha :")
        usuarioController.cadastra_usuario(email2,login,senha)
    if x == 6:
        break
"""