from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# db = Date Base
db = create_engine("sqlite:///meubanco.db") # Cria o banco de dados ou conecta com banco de dados existente

Session = sessionmaker(bind=db) # bind = Parâmetro que diz qual é o nome do banco de dados
session = Session()

# Base -> É a classe mãe. Todas as tabelas vão ser subclasses dela.
Base = declarative_base() # Permite usar os comandos python no lugar dos comandos sql

# Tabelas
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


class Livro(Base):
    __tablename__ = "livros"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id")) 
    # Dono está ligado a tabela usuário

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono



# Cria todas as tabelas criadas dentro do banco de dados dentro de db
Base.metadata.create_all(bind=db)

# CRUD: Create,Read,Update e Delete
# Criar-Ler dados-Atualizar-Deletar 

# Create-CRIAR

#usuario = Usuario(nome="Lucas2", email="in9300121outro@gmail.com", senha="123456")
#session.add(usuario) # Salvando temporariamente 
#session.commit() # Subindo a atualização

# Read-LER
# .all() -> Consulta todos os itens .first() -> Consulta o primeiro item
#lista_usuarios = session.query(Usuario).all() # Query = Consulta 
usuario_lucas = session.query(Usuario).filter_by(email="in9300121outro@gmail.com").first()
print(usuario_lucas)
print(usuario_lucas.nome)
print(usuario_lucas.email)

livro = Livro(titulo="Nome do Vento", qtde_paginas=1000, dono=usuario_lucas.id)
session.add(livro)
session.commit()

# Update - ATUALIZAR
usuario_lucas.nome = "Lucas Gabriel"
session.add(usuario_lucas)
session.commit()

# Delete - DELETAR
session.delete(usuario_lucas)
session.commit()