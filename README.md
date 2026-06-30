# 📚SQLAlchemy

Este projeto foi desenvolvido com o objetivo de praticar os conceitos fundamentais de **persistência de dados em Python** utilizando **SQLAlchemy** como ORM e **SQLite** como banco de dados.

A aplicação demonstra como criar e manipular tabelas através de classes Python, realizando operações completas de **CRUD (Create, Read, Update e Delete)** sem escrever comandos SQL diretamente.

## 🚀 Tecnologias utilizadas

* Python 3
* SQLAlchemy
* SQLite

## 📂 Estrutura do projeto

```
📁 projeto
│── main.py
│── meubanco.db (criado automaticamente)
└── README.md
```

## 📖 Conceitos praticados

* Criação de banco de dados SQLite
* Configuração do SQLAlchemy
* Criação de modelos (Models)
* Mapeamento Objeto-Relacional (ORM)
* Criação automática de tabelas
* Sessões (`Session`)
* Relacionamentos utilizando `ForeignKey`
* Operações CRUD

## 🗄️ Modelos

### Usuário

| Campo | Tipo    |
| ----- | ------- |
| id    | Integer |
| nome  | String  |
| email | String  |
| senha | String  |
| ativo | Boolean |

### Livro

| Campo        | Tipo                     |
| ------------ | ------------------------ |
| id           | Integer                  |
| titulo       | String                   |
| qtde_paginas | Integer                  |
| dono         | ForeignKey → usuarios.id |

Cada livro pertence a um usuário através da chave estrangeira (`ForeignKey`).

## ⚙️ Funcionalidades

### ✔ Criar

* Criar usuários
* Criar livros associados a um usuário

### ✔ Ler

* Buscar todos os usuários
* Buscar um usuário específico
* Exibir informações cadastradas

### ✔ Atualizar

* Alterar dados de um usuário

### ✔ Deletar

* Remover usuários do banco de dados

## 💻 Exemplo

Criando um usuário:

```python
usuario = Usuario(
    nome="Lucas",
    email="lucas@email.com",
    senha="123456"
)

session.add(usuario)
session.commit()
```

Buscando um usuário:

```python
usuario = session.query(Usuario).filter_by(
    email="lucas@email.com"
).first()
```

Criando um livro:

```python
livro = Livro(
    titulo="Nome do Vento",
    qtde_paginas=1000,
    dono=usuario.id
)

session.add(livro)
session.commit()
```

Atualizando um usuário:

```python
usuario.nome = "Lucas Gabriel"

session.add(usuario)
session.commit()
```

Removendo um usuário:

```python
session.delete(usuario)
session.commit()
```

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Entre na pasta:

```bash
cd nome-do-repositorio
```

Instale a dependência:

```bash
pip install sqlalchemy
```

Execute o projeto:

```bash
python main.py
```

Na primeira execução será criado automaticamente o arquivo:

```
meubanco.db
```

## 🎯 Objetivo

Este projeto faz parte da minha jornada de estudos em **Python Backend**, com foco em:

* SQLAlchemy
* ORM
* SQLite
* Modelagem de dados
* Persistência de informações
* Desenvolvimento Backend

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos importantes como:

* Organização de modelos
* Sessões do SQLAlchemy
* Mapeamento objeto-relacional
* Chaves primárias
* Chaves estrangeiras
* Operações CRUD
* Persistência de dados em banco relacional

---

⭐ Este projeto faz parte da minha coleção de estudos em Python para fortalecer os fundamentos de desenvolvimento Backend.
