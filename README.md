# Descrição
StockSimplify é um projeto fullstack desenvolvido em Python com o framework Django. Ele é um sistema de gestão de estoque projetado para facilitar o controle de inventário.

StockSimplify oferece um conjunto abrangente de funcionalidades, incluindo operações CRUD (Create, Read, Update, Delete) para marcas, 
categorias, entradas e saídas de produtos, produtos e fornecedores.

Além disso, o StockSimplify conta com uma tela de dashboard para facilitar a visualização de métricas importantes, proporcionando uma visão clara e concisa do estado do estoque.

**Este projeto ainda está em desenvolvimento** e, portanto, receberá atualizações futuras para aprimorar e expandir suas funcionalidades.

## Instalação

Siga os passos abaixo para clonar e executar o projeto no seu computador:

1. **Clone o repositório**
   
   ``` git clone https://github.com/seu-usuario/StockSimplify.git ```

2. **Crie um ambiente virtual**
   
   ``` python -m venv venv ```

3. **Ative o ambiente virtual**
   
   - Windows: ``` venv\Scripts\activate ```
   - Linux/MacOs: ``` source venv/bin/activate ```

4. **Instale as dependências**
   
   ``` pip install -r requirements.txt ```

5. **Realize as migrações do banco de dados**
    
   ``` python manage.py migrate ```

6. **Crie um superusuário**
   
   ``` python manage.py createsuperuser ```

7. **Inicie o servidor de desenvolvimento**
    
   ``` python manage.py runserver ```

8. **Acesse o projeto no seu navegador**
    
   Abra o navegador e digite **http://127.0.0.1:8000** para ver o projeto em execução.
