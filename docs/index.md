# StockSimplify 📦

Um sistema de gerenciamento de estoque construído com Django e Django Rest Framework, utilizando Docker e PostgreSQL.

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
- PostgreSQL
- Docker

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
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── requirements.txt
└── requirements_dev.txt
```

---

## ▶️ Como rodar o projeto

### 🐋 Executando com Docker (recomendado)

O projeto está configurado para rodar com Docker.

---

### 1. Subir os containers

Na raiz do projeto:

```
docker-compose up --build
```

Isso irá:
- Criar o container do PostgreSQL
- Criar o container da aplicação Django
- Executar automaticamente as migrações
- Subir o servidor em `0.0.0.0:8000`

---

### 🌐 Acessos

Aplicação estará disponível em: `http://127.0.0.1:8000`

---

### 🗄️ Banco de dados

O container do banco está configurado com:
- **DB_NAME**: stockdb
- **DB_USER**: stockuser
- **DB_PASSWORD**: stockpassword
- **DB_HOST**: db
- **DB_PORT**: 5432

Os dados são persistidos no volume: `postgres_data`
Ou seja, mesmo que os containers sejam removidos, os dados continuam salvos.

---

### 👤 Criar Superusuário
Após subir os containers, caso queira criar um superusuário, execute:

```
docker exec -it [container_id] task create_user
```

---

### 📚 Documentação
Após subir os containers, caso queira subir a documentação, execute:

```
docker exec -it [container_id] task docs
```

A documentação estará disponívem em: `http://127.0.0.1:8001`

---

### 🛑 Parar os containers
```
docker compose down
```
Para remover também os volumes (⚠️ apaga os dados do banco):
```
docker compose down -v
```

---

### 💻 Executando sem Docker (opcional)

Caso queira rodar manualmente:

---

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
