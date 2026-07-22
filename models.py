import re
import bcrypt


class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Usuario:
    def __init__(self, pessoa, login, senha):
        self.pessoa = pessoa
        self.login = login

        self.verificar_forca_senha(senha)

        self.senha_hash = bcrypt.hashpw(
            senha.encode("utf-8"),
            bcrypt.gensalt()
        )

    @staticmethod
    def verificar_forca_senha(senha):
        if len(senha) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")

        if not re.search(r"[a-z]", senha):
            raise ValueError("A senha deve conter letra minúscula.")

        if not re.search(r"[A-Z]", senha):
            raise ValueError("A senha deve conter letra maiúscula.")

        if not re.search(r"\d", senha):
            raise ValueError("A senha deve conter número.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            raise ValueError("A senha deve conter caractere especial.")

    def conferir_senha(self, senha_digitada):
        return bcrypt.checkpw(
            senha_digitada.encode("utf-8"),
            self.senha_hash
        )