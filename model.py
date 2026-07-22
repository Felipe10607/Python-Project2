import re
import bcrypt
class Pessoa:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
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
            raise ValueError("A senha deve conter letras minúsculas.")

        if not re.search(r"[A-Z]", senha):
            raise ValueError("A senha deve conter letras maiúsculas.")

        if not re.search(r"\d", senha):
            raise ValueError("A senha deve conter números.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            raise ValueError("A senha deve conter caracteres especiais.")

        return True
    def conferir_senha(self, senha_digitada):
        return bcrypt.checkpw(
            senha_digitada.encode("utf-8"),
            self.senha_hash
        )
class Usuario(Pessoa):
    def __init__(self,email, senha):
        super.__init__(email, senha)


try:
    pessoa = Pessoa(
        "Felipe",
        "felipe@email.com",
        "Senha@123"
    )

    print("Cadastro realizado!")
    print(pessoa.senha_hash)
    print(pessoa.conferir_senha("Senha@123"))

except ValueError as erro:
    print(f"Erro: {erro}")