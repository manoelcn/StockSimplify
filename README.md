# StockSimplify 📦

Um sistema de gerenciamento de estoque construído com Django e Django Rest Framework.

---

## 📋 Descrição do Projeto
O StockSimplify é uma aplicação web com API REST para controle e gerenciamento de estoque.

O sistema permite realizar operações CRUD (Create, Read, Update, Delete) sobre:

- Produtos
- Categorias
- Marcas
- Fornecedores
- Entradas de estoque (Inflow)
- Saídas de estoque (Outflow)

Tecnologias usadas:

- Django
- Django Rest Framework
- Simple JWT
- Chart.js

---

## 📦 Estrutura do Projeto

```
StockSimplify/
├── app/
├── authentication/
├── brands/
├── categories/
├── docs/
├── inflows/
├── outflows/
├── products/
├── services/
├── suppliers/
├── .flake8
├── .gitignore
├── manage.py
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── requirements.txt
└── requirements_dev.txt
```

---

## ▶️ Como rodar o projeto

### 1. Criar e ativar o ambiente virtual

```
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

---

### 2. Instalar as dependências

```
pip install -r requirements.txt
```

Caso queira instalar dependências de desenvolvimento:

```
pip install -r requirements_dev.txt
```

---

### 3. Rodar as migrações do banco de dados

```
python manage.py makemigrations
python manage.py migrate
```

---

### 4. Criar um superusuário (opcional, mas recomendado)

```
task create_user
```

---

### 5. Rodar o servidor Django

```
task run
```

A aplicação estará disponível em: `http://127.0.0.1:8000`

---

## 📚 Documentação MkDocs

Para rodar a documentação local:

```
task docs
```

Acesse:

```
http://127.0.0.1:8001
```

---

## 👤 Autor

**Manoel Cândido**

[manoelcandidodev@gmail.com](mailto:manoelcandidodev@gmail.com)
