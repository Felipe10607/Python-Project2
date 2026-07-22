from conexao import conectar
from models import *
class pessoaDao:
    @classmethod
    def cadastrar(cls, pessoa : Pessoa):
        conexao = conectar()
        cursor = conexao.cursor()
        try:
            cursor.execute("""
                INSERT INTO Usuario (pessoa_id, login, senha_hash)
                VALUES (?, ?, ?)
            """, (
                pessoa.pessoa_id,
                pessoa.login,
                pessoa.senha_hash.decode("utf-8")
            ))

            conexao.commit()

        finally:
            cursor.close()
            conexao.close()
    @classmethod
    def apagar(cls, pessoa : Pessoa):
        conexao = conectar()
        cursor =  conexao.cursor()
        try :
            cursor.execute(
                """
            DELETE FROM dbo.Pessoa where email = ? 
            """,
            (pessoa.email)
            )
            conexao.commit()
        except Exception as erro:
            conexao.rollback()
            print(f"Erro ao apagar pessoa: {erro}")

        finally:
            cursor.close()

class UsuarioDao(pessoaDao):
    @classmethod
    def cadastrar(cls, usuario : Usuario):
        conexao = conectar()
        cursor =  conexao.cursor()
        try:
            cursor.execute(
                """
                select id from dbo.Pessoa where email = ?                
""",(Pessoa.email)
            )


            cursor.execute("""
                INSERT INTO Usuario (pessoa_id, login, senha_hash)
                VALUES (?, ?, ?)
            """, (
                usuario.pessoa_id,
                usuario.login,
                usuario.senha_hash.decode("utf-8")
            ))

            conexao.commit()

        finally:
            cursor.close()
            conexao.close()    
    @classmethod
    def apagar(cls, usuario : Usuario):
        conexao = conectar()
        cursor =  conexao.cursor()
        try :
            cursor.execute(
                """
            DELETE FROM dbo.Pessoa where email = ? 
            """,
            (pessoa.email)
            )
            conexao.commit()
        except Exception as erro:
            conexao.rollback()
            print(f"Erro ao apagar pessoa: {erro}")

        finally:
            cursor.close()
