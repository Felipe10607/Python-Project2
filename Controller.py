from models import *
from dao import *

class pessoaController:
    @staticmethod
    def cadastra(nome,email):
        pessoa = Pessoa(nome,email)
        pessoaDao.cadastrar(pessoa)


class usuarioController:
    @staticmethod
    def cadastra_usuario(email,login,senha):
        pessoa = Pessoa(None,email)
        usuario = Usuario(pessoa,login,senha)
        usuarioDao.cadastrar(usuario)
    @staticmethod
    def fazer_login(login,senha):
        usuario = Usuario(login,senha)
        usuarioDao.consultar(usuario)