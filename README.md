#  Python-Project2 — Sistema de Login e Controle de Usuários

Sistema de cadastro, login e gerenciamento de usuários desenvolvido em **Python**, aplicando o padrão de arquitetura **MVC** (Model-View-Controller) com camada de persistência em **SQL Server** e senhas protegidas por **criptografia (bcrypt)**.

Projeto criado com foco em fixar conceitos de **Programação Orientada a Objetos (POO)**, separação de responsabilidades em camadas e boas práticas de segurança no armazenamento de credenciais.

##  Sobre o projeto

A proposta do projeto foi construir, do zero, um sistema de login e controle de usuários de nível inicial, indo além do CRUD básico ao introduzir:

- **Arquitetura MVC**, separando modelo de dados, regras de negócio e interface;
- **Persistência real em banco relacional** (SQL Server), via `pyodbc`;
- **Criptografia de senhas com bcrypt** (hash + salt), em vez de texto puro;
- **Validação de força de senha** antes do cadastro.

##  Funcionalidades

- Cadastro de pessoa (nome e e-mail);
- Cadastro de usuário vinculado a uma pessoa (login e senha);
- Login com verificação de credenciais via hash bcrypt;
- Exclusão de cadastro de pessoa;
- Exclusão de usuário;
- Listagem dos logins associados a um e-mail cadastrado;
- Validação de força da senha (mínimo de 8 caracteres, letra maiúscula, minúscula, número e caractere especial).

##  Arquitetura (MVC)

O projeto separa as responsabilidades em camadas, adicionando uma camada de acesso a dados (DAO) para isolar o SQL do restante da aplicação:

```
view.py         → View        (menu interativo via terminal / entrada e saída do usuário)
Controller.py   → Controller  (pessoaController e usuarioController: orquestram as regras de negócio)
models.py       → Model       (classes Pessoa e Usuario, com geração de hash e validação de senha)
dao.py          → DAO         (pessoaDao e usuarioDao: executam as queries SQL)
conexao.py      → Config      (abre a conexão com o SQL Server via pyodbc)
```

Fluxo típico de uma ação (ex.: cadastrar usuário):

```
view.py → usuarioController.cadastra_usuario() → usuarioDao.cadastrar() → SQL Server
```

##  Estrutura do banco de dados

O sistema utiliza duas tabelas relacionadas no banco `SistemaLogin`:

**dbo.Pessoa**
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id    | PK   | Identificador da pessoa |
| nome  | varchar | Nome da pessoa |
| email | varchar | E-mail (utilizado para localizar o cadastro) |

**dbo.Usuario**
| Campo      | Tipo | Descrição |
|------------|------|-----------|
| id         | PK   | Identificador do usuário |
| pessoa_id  | FK   | Referência à tabela Pessoa |
| login      | varchar | Login de acesso |
| senha_hash | varchar | Hash bcrypt da senha (nunca a senha em texto puro) |

## Segurança

- As senhas nunca são armazenadas em texto puro: são transformadas em hash com **bcrypt** (`bcrypt.hashpw` + `gensalt`) antes de irem para o banco;
- A verificação de login usa `bcrypt.checkpw`, comparando o hash salvo com a senha informada;
- Antes do cadastro, a senha passa por uma validação de força (`verificar_forca_senha`), garantindo tamanho mínimo e uso de maiúsculas, minúsculas, números e símbolos.

##  Tecnologias utilizadas

- **Python 3**
- **SQL Server** (Microsoft)
- **pyodbc** — conexão com o banco de dados
- **bcrypt** — hash e verificação de senhas
- **re (regex)** — validação de força da senha
- Programação Orientada a Objetos (POO)

##  Estrutura de arquivos

```
Python-Project2/
├── conexao.py       # Configuração e abertura da conexão com o SQL Server
├── models.py        # Classes Pessoa e Usuario (Model)
├── dao.py           # pessoaDao e usuarioDao (acesso ao banco de dados)
├── Controller.py    # pessoaController e usuarioController (regras de negócio)
├── view.py          # Menu interativo via terminal (View)
├── proposta.txt      # Proposta inicial do projeto
└── README.md
```

##  Como executar

### Pré-requisitos
- Python 3 instalado
- SQL Server instalado e rodando localmente
- ODBC Driver 18 for SQL Server instalado

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/Felipe10607/Python-Project2.git
cd Python-Project2
```

2. Instale as dependências:
```bash
pip install pyodbc bcrypt
```

3. Crie o banco de dados `SistemaLogin` no SQL Server com as tabelas `Pessoa` e `Usuario` (conforme estrutura acima).

4. Ajuste a string de conexão em `conexao.py` com o nome do seu servidor SQL Server:
```python
"SERVER=SEU_SERVIDOR;"
"DATABASE=SistemaLogin;"
```

5. Execute o sistema:
```bash
python view.py
```

6. Siga o menu interativo no terminal para se cadastrar, criar um login e testar as funcionalidades.

##  Melhorias futuras

- [ ] Tratamento de exceções mais robusto (conexão, entradas inválidas);
- [ ] Uso de variáveis de ambiente para a string de conexão (evitar dados sensíveis no código);
- [ ] Testes automatizados (unitários e de integração);

##  Autor

Desenvolvido por [Felipe10607](https://github.com/Felipe10607) como projeto de estudo, aplicando conceitos de POO, arquitetura MVC, integração com banco de dados relacional e criptografia de senhas.
