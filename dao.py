from conexao import conectar
from models import *
class pessoaDao:
    @classmethod
    def cadastrar(cls, pessoa : Pessoa):
        conexao = conectar()
        cursor = conexao.cursor()
        try:
            cursor.execute("""
                INSERT INTO dbo.Pessoa (nome,email)
                VALUES (?, ?)
            """, (
                pessoa.nome,
                pessoa.email
            ))

            conexao.commit()

        finally:
            cursor.close()
            conexao.close()
    @classmethod
    def apagar(cls, email : str):
        conexao = conectar()
        cursor =  conexao.cursor()
        try :
            cursor.execute(
                """
            DELETE FROM dbo.Pessoa where email = ? 
            """,
            (email,)
            )
            conexao.commit()
        except Exception as erro:
            conexao.rollback()
            print(f"Erro ao apagar pessoa: {erro}")

        finally:
            cursor.close()
    @classmethod
    def consultar(cls, pessoa : Pessoa):
        conexao = conectar()
        cursor = conexao.cursor()
        try:
            cursor.execute("""
                select id,email from dbo.Pessoa where email = ?
            """, (
                (pessoa.email,)
            ))
            resultado = cursor.fetchone()
            if resultado is None:
                print("Usuário não encontrado.")
                return
            id = resultado[0]
        finally:
            cursor.close()
            conexao.close()
        return True

class usuarioDao(pessoaDao):
    @classmethod
    def cadastrar(cls, usuario : Usuario):
        Usuario.verificar_forca_senha(usuario)
        conexao = conectar()
        cursor =  conexao.cursor()
        try:
            cursor.execute(
                """
                select id from dbo.Pessoa where email = '?'""",(usuario.pessoa.email,)
            )
            resultado = cursor.fetchone()

            cursor.execute("""
                INSERT INTO dbo.Usuario (pessoa_id, login, senha_hash)
                VALUES (?, ?, ?)
            """, (
                resultado[0],
                usuario.login,
                usuario.senha_hash.decode("utf-8")
            ))

            conexao.commit()

        finally:
            cursor.close()
            conexao.close()    
    @classmethod
    def apagar(cls, login : str):
        conexao = conectar()
        cursor =  conexao.cursor()
        try :
            cursor.execute(
                """
            DELETE FROM dbo.Usuario where login = ? 
            """,
            (login,)
            )
            conexao.commit()
        except Exception as erro:
            conexao.rollback()
            print(f"Erro ao apagar pessoa: {erro}")

        finally:
            cursor.close()
    @classmethod
    def consultar(cls,usuario : Usuario):
        conexao = conectar()
        cursor = conexao.cursor()
        try:
            cursor.execute(
                """
                select login,senha_hash from dbo.Usuario where login = ?
                """,(usuario.login,)
            )
            resultado = cursor.fetchone()
            if resultado is None:
                print("Usuário não encontrado.")
                return
            login,senha_hash = resultado
            if login == usuario.login and usuario.conferir_senha(senha_hash):
                print("LOGIN REALIZADO!")
            else:
                print("Senha incorreta.")
        finally:
                    cursor.close()
                    conexao.close()
"""
a = Pessoa('Felps','felps@')
b = Usuario(a,'felps','Felps.1234')

pessoaDao.cadastrar(a)
usuarioDao.cadastrar(b)
"""
