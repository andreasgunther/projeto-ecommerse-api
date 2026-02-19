# Projeto E-commerce API - Flask
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23d71f00.svg?style=for-the-badge&logo=sqlalchemy&logoColor=white)

Este projeto é uma API RESTful para um humilde sistema de e-commerce, desenvolvida como requisito do **Minicurso de Flask** da **Rocketseat**.

## 📂 Estrutura do Projeto

A organização segue o padrão **Application Factory**:

```text
ecommerce_api/
├── app/
│   ├── __init__.py 
│   ├── models.py  
│   └── routes.py
├── requirements.txt  
├── run.py              
└── seed.py    
```

## Aprendizados

**Métodos HTTP:** Implementação de métodos `GET`, `POST`, `PUT` e `DELETE`.

**Manipulação de Dados:** Recebimento e envio de dados via JSON e tratamento de códigos de status HTTP.

**Modularização:** Refatoração do código para separar a lógica de banco de dados `models.py` da lógica de rotas `routes.py`.

**Blueprints:** Uso de `Blueprints` do Flask para organizar rotas.

**Flask-Login:** Implementação de controle de sessão e proteção de rotas através do decorador `@login_required`.

Uso do **SQLAlchemy (ORM)** para realizar a comunicação entre Flask e SQLite.

**Postman:** Criação de coleções para testar as rotas.

**AWS Elastic Beanstalk:** Realização do `deploy` configurando o ambiente de produção na nuvem da Amazon.

## Como Executar o Projeto

1. Clonar o repositório

```sh
git clone https://github.com/andreasgunther/projeto-ecommerce-api
cd ecommerce-api
```

2. Criar o Ambiente Virtual

```sh
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependências

```sh
pip install -r requirements.txt
```

4. Popular o Banco de Dados

```sh
python3 seed.py
```

5. Iniciar a API

```sh
python3 run.py
```

## Recursos da API

Todas as requisições privadas exigem um cookie de sessão ativo (gerado após o login).

### Autenticação e Usuários
| Método | Endpoint | Descrição | Acesso |
| :--- | :--- | :--- | :--- |
| `POST` | `/login` | Autentica o usuário e inicia sessão | Público |
| `POST` | `/logout` | Encerra a sessão ativa | Privado |

### Catálogo de Produtos
| Método | Endpoint | Descrição | Acesso |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/products` | Lista todos os produtos cadastrados | Público |
| `GET` | `/api/products/<id>` | Detalhes de um produto específico | Público |
| `POST` | `/api/products/add` | Cadastra um novo produto | Privado |
| `PUT` | `/api/products/update/<id>` | Atualiza dados do produto | Privado |
| `DELETE` | `/api/products/delete/<id>` | Remove um produto do catálogo | Privado |

### Carrinho e Checkout
| Método | Endpoint | Descrição | Acesso |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/cart` | Visualiza itens no carrinho | Privado |
| `POST` | `/api/cart/add/<id>` | Adiciona produto ao carrinho | Privado |
| `DELETE` | `/api/cart/remove/<id>` | Remove item específico do carrinho | Privado |
| `POST` | `/api/cart/checkout` | Finaliza a compra e limpa o carrinho | Privado |

### Exemplo de Requisição (JSON)

Para adicionar um produto, envie um `POST` para `/api/products/add` com o seguinte corpo:

```json
{
    "name": "Teclado Mecanico",
    "price": 120.00,
    "description": "De Plastico"
}