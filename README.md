## Visão Geral da EMBRAPA API - Vitivinicultura

### Descrição

Este projeto permite realizar um Web Scrapping no site sobre "Dados da Vitivinicultura" da Embrapa. http://vitibrasil.cnpuv.embrapa.br/

Existem duas formas neste projeto para obtenção dos dados do site da Embrapa:

   - A primeira é a leitura e gravação dos dados disponibilizados através do arquivo CSV em cada página do site.
   - A segunda é a leitura dos dados do site e a disponibilização direta na API.

A API permite realizar consultas, fornecendo dados relevantes através de endpoints RESTful. 

A API utiliza autenticação JWT para segurança.

Neste projeto encontra-se um arquivo Docker configurado que permite a execução em diversos ambientes de infraestrutura capazes de suportar essa tecnologia.

### Base URL
```
https://127.0.0.0:8000
```

## Estrutura do Projeto:
    
    
    ├── app/
    │   ├── __init__.py
    │   ├── data_processing/
    │   │   ├── __init__.py
    │   │   ├── comercializacao_processing.py
    │   │   ├── exportacao_processing.py
    │   │   ├── importacao_processing.py
    │   │   ├── processamento_processing.py
    │   │   ├── producao_processing.py
    │   │   └── database_update.py
    │   │
    │   ├── sql_app/
    │   │   ├── __init__.py
    │   │   ├── database_manager.py
    │   │   ├── database.py
    │   │   ├── dependencies.py
    │   │   ├── embrapa.db
    │   │   └── models.py 
    │   │
    │   ├── scraper/
    │   │   ├── __init__.py
    │   │   ├── models.py.py
    │   │   └─── scraper.py
    │   │   
    │   │
    │   ├──__init__.py 
    │   ├── main.py
    │   └── config.py
    │    
    ├── Docker/
    │   ├── Dockerfile
    │   ├── docker-compose.yml
    │   ├── initialize.py    
    │   ├── requirements.txt       
    │   └── .dockerignore
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_main.py
    │   └── test_scraper.py
    │
    ├──VENV/
    │
    ├── .env
    │
    ├── README.md
    └── .gitignore


## Autenticação
Esta API usa JWT (JSON Web Tokens) para autenticação. Para acessar os endpoints protegidos, é necessário incluir um token JWT válido no cabeçalho das requisições.

### Obter Token JWT
**Endpoint:** `/token`

**Método:** `POST`

**Parâmetros de Requisição:**
- username
- password

**Corpo da Requisição:**
```json
{
   username: teste
   password: teste
}
```

**Resposta de Sucesso:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTcxNjg2MjY3MX0.tt0SBG4TcNUdJVrxTjcHWxZ-qaTdIat77lZebNyOejc",
  "token_type": "bearer"
}
```

**Exemplo de Requisição:**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=teste&password=teste&scope=&client_id=&client_secret='
```

## Endpoints

### 1. Token

**Endpoint:** `/token`

**Método:** `Post`

**Parâmetros:**
- `username`: (string) 
- `password`: (string) 

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTcxNjg2MjY3MX0.tt0SBG4TcNUdJVrxTjcHWxZ-qaTdIat77lZebNyOejc",
   "token_type": "bearer"
}
```

**Exemplo de Requisição:**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=teste&password=teste&scope=&client_id=&client_secret='
```

### 2. Production

**Endpoint:** `/production`

**Método:** `GET`

**Parâmetros:**
  - `year` (integer, required): The year of the production data.
  - `token` (string, required): The authentication token.

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
  "year": 2023,
  "data": [
    {
      "Produto": "VINHO DE MESA",
      "Quantidade (L.)": "169.762.429"
    }, 
  ]
}
```

**Exemplo de Requisição:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/production/?year=2023&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTcxNjg2MTg4NX0.49GS0PEVDKhnKb_d-tQNKBwTgHfdSpX8FZZ9EzTAC0Q' \
  -H 'accept: application/json'
```
 
### 3. Processing Data Route

**Endpoint:** `/processing`

**Método:** `GET`

**Parâmetros:**
   - `category` (string, required): The category of processing data.
   - `year` (integer, optional): The year of the processing data.
   - `token` (string, optional): The authentication token.

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
  "category": "viniferas",
  "year": 2023,
  "data": [
    {
      "Cultivar": "TINTAS",
      "Quantidade (Kg)": "-"
    },
  ]
}
```

**Exemplo de Requisição:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/processing/?category=viniferas&year=2023&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTcxNjg2NDk5Mn0.NVYlJU35qlIIiyfPZybj7RiYT4DChAa-vDDHRC9HzgE' \
  -H 'accept: application/json'
```

### 4. Commercialization Data Route

**Endpoint:** `/commercialization`

**Método:** `GET`

**Parâmetros:**
   - `year` (integer, required): The year of the commercialization data.
   - `token` (string, required): The authentication token.

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
  "year": 2023,
  "data": [
    {
      "Produto": "VINHO DE MESA",
      "Quantidade (L.)": "187.016.848"
    },
  ]
}
```

**Exemplo de Requisição:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/commercialization/?year=2023&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTcxNjg2NDk5Mn0.NVYlJU35qlIIiyfPZybj7RiYT4DChAa-vDDHRC9HzgE' \
  -H 'accept: application/json'
```

### 5. Import Data Route

**Endpoint:** `/import`

**Método:** `GET`

**Parâmetros:**
    - `category` (string, required): The category of import data.
    - `year` (integer, optional): The year of the import data.
    - `token` (string, optional): The authentication token.

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
  "year": 2023,
  "data": [
    {
      "Países": "Africa do Sul",
      "Quantidade (Kg)": "522.733",
      "Valor (US$)": "1.732.850"
    },
  ]
}
```

**Exemplo de Requisição:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/import/?category=vinhos_mesa&year=2023&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9' \
  -H 'accept: application/json'
```

### 6. Export Data Route

**Endpoint:** `/export`

**Método:** `GET`

**Parâmetros:**
   - `category` (string, required): The category of export data.
   - `year` (integer, optional): The year of the export data.
   - `token` (string, optional): The authentication token.

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
  "year": 2023,
  "data": [
    {
      "Países": "Afeganistão",
      "Quantidade (Kg)": "-",
      "Valor (US$)": "-"
    },
  ]
}
```

**Exemplo de Requisição:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/export/?category=vinhos_mesa&year=2023&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTcxNjg2NDk5Mn0.NVYlJU35qlIIiyfPZybj7RiYT4DChAa-vDDHRC9HzgE' \
  -H 'accept: application/json'
```

### 7. Read Production
**Endpoint:** `/bd/production/{year}`

**Método:** `GET`

**Parâmetros:**
   - `year` (integer, required): The year of the production data.
   - `token` (string, optional): The authentication token.

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
  "year": 2023,
  "data": [
    {
      "Produto": "VINHO DE MESA",
      "Quantidade (L.)": 169762429
    },
  ]
}
```

**Exemplo de Requisição:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/bd/production/2023?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTcxNjg2NDk5Mn0.NVYlJU35qlIIiyfPZybj7RiYT4DChAa-vDDHRC9HzgE' \
  -H 'accept: application/json'
```

### 8. Read Processing Data
**Endpoint:** `/bd/processing/{category}/{year}`

**Método:** `GET`

**Parâmetros:**
   - `category` (string, required): The category of processing data.
   - `year` (integer, required): The year of the processing data.
   - `token` (string, optional): The authentication token.

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
  "category": "viniferas",
  "year": 2023,
  "data": [
    {
      "Cultivar": "TINTAS",
      "Quantidade (Kg)": "2023"
    },
  ]
}
```

**Exemplo de Requisição:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/bd/processing/viniferas/2023?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9' \
  -H 'accept: application/json'
```

### 9. Read Commercialization Data
**Endpoint:** `/bd/commercialization/{year}`

**Método:** `GET`

**Parâmetros:**
   - `year` (integer, required): The year of the commercialization data.
   - `token` (string, optional): The authentication token.

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
  "year": 2023,
  "data": [
    {
      "Produto": "VINHO DE MESA",
      "Quantidade (L.)": 187016848
    },
  ]
}
```

**Exemplo de Requisição:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/bd/commercialization/2023?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTcxNjg2NDk5Mn0.NVYlJU35qlIIiyfPZybj7RiYT4DChAa-vDDHRC9HzgE' \
  -H 'accept: application/json'
```

### 10. Read Importation Data
**Endpoint:** `/bd/importation/{category}/{year}`

**Método:** `GET`

**Parâmetros:**
   - `category` (string, required): The category of import data.
   - `year` (integer, required): The year of the import data.
   - `token` (string, optional): The authentication token.

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
  "category": "vinhos_mesa",
  "year": 2023,
  "data": [
    {
      "Países": "Africa do Sul",
      "Quantidade (Kg)": 522733,
      "Valor (US$)": 1732850
    },
  ]
}
```

**Exemplo de Requisição:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/bd/importation/vinhos_mesa/2023?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTcxNjg2NDk5Mn0.NVYlJU35qlIIiyfPZybj7RiYT4DChAa-vDDHRC9HzgE' \
  -H 'accept: application/json'
```

### 11. Read Exportation Data
**Endpoint:** `/bd/exportation/{category}/{year}`

**Método:** `GET`

**Parâmetros:**
   - `category` (string, required): The category of export data.
   - `year` (integer, required): The year of the export data.
   - `token` (string, optional): The authentication token.

**Cabeçalhos de Requisição:**
- `Authorization`: (string) Bearer token

**Resposta de Sucesso:**
```json
{
  "category": "vinhos_mesa",
  "year": 2023,
  "data": [
    {
      "Países": "Afeganistão",
      "Quantidade (Kg)": 0,
      "Valor (US$)": 0
    },
  ]
}
```

**Exemplo de Requisição:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/bd/exportation/vinhos_mesa/2023?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTcxNjg2NDk5Mn0.NVYlJU35qlIIiyfPZybj7RiYT4DChAa-vDDHRC9HzgE' \
  -H 'accept: application/json'
```


## Schemas

A API utiliza alguns schemas para suas respostas, tais como: `ProductionData`, `ProcessingData`, `CommercializationData`, `ImportData`, `ExportData`.



## Mensagens de Erro

### Erro de Autenticação
**Código:** `401 Unauthorized`

**Resposta:**
```json
{
    "message": "Credenciais incorretas."
}
```
```json
{
    "message": "Invalid token."
}
```

### Erro de Parâmetros
**Código:** `400 Bad Request`

**Resposta:**
```json
{
    "message": "400 Bad Request."
}
```

### Erro Interno do Servidor
**Código:** `500 Internal Server Error`

**Resposta:**

- Production Data
```json
{
    "message": "Falha ao buscar dados de produção: ..."
}
```
- Production DB
```json
{
    "message": "Falha ao buscar dados de produção para o ano ..."
}
```

- Processing Data
```json
{
    "message": "Falha ao buscar dados de processamento: ..."
}
```
- Processing DB
```json
{
    "message": "Falha ao buscar dados de processamento para {category}, ano {year}: ..."
}
```

- Comercialization Data
```json
{
    "message": "Falha ao buscar dados de comercialização: ..."
}
```
- Comercialization DB
```json
{
    "message": "Falha ao buscar dados de comercialização para o ano {year}:  ..."
}
```

- Import Data
```json
{
    "message": "Falha ao buscar dados de importação: ..."
}
```
- Import DB
```json
{
    "message": "Falha ao buscar dados de importação para {category}, ano {year}:  ..."
}
```

- Export Data
```json
{
    "message": "Falha ao buscar dados de exportação: ..."
}
```
- Export DB
```json
{
    "message": "Falha ao buscar dados de exportação para {category}, ano {year}:  ..."
}
```

--

Todos os erros apresentados durante a execução da API podem ser consultados no arquivo de LOG na pasta raiz do projeto chamado: "error.log".

--


## Plano de Deploy 

<img src="/use_case/scrapping_api_c3_arquitetura_deploy.png">
 

## Testes
- Os testes são realizados para garantir que a API e os scrapers funcionem corretamente. Eles utilizam o FastAPI TestClient e Pytest para realizar testes de integração.

### Objetivo dos Testes de Integração
-O principal objetivo é verificar se os diferentes componentes da sua API (rotas, controladores, modelos, banco de dados, etc.)     funcionam corretamente em conjunto, simulando requisições HTTP reais.
### Estrutura dos Testes
-Os arquivos de testes estão localizados no diretório tests/.
    .
    tests/
    ├── __init__.py
    ├── test_main.py
    └── test_scraper.py
### Testes com FastAPI: TestClient e Pytest
```
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_production_data():
    response = client.get("/production/?year=2021")
    assert response.status_code == 200  # Verifica se o status da resposta é 200
    assert response.json()['year'] == 2021  # Verifica se o ano na resposta é correto
```

### Exemplo de Teste de rota Scraping em test_scraper.py:
```
from app.scraper.scraper import (
    scrape_production,
    scrape_processing,
    scrape_commercialization,
    scrape_import,
    scrape_export,
)

def test_scrape_production():
    # Supondo que você espera que a função retorne uma lista de dicionários para o ano 2021
    result = scrape_production(2021)
    assert type(result) == list  # Verifica se o resultado é uma lista
    assert len(result) > 0  # Verifica se a lista não está vazia
    assert 'Produto' in result[0]  # Verifica se a chave esperada está no dicionário
```
### Exemplo de Teste de Integração para Banco de Dados em test_db.py:
```
from app.sql_app.database import get_db
from app.sql_app.models import Production
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_database_connection():
    # Código de teste para verificar a conexão com o banco de dados
```

### Executando os Testes

Para rodar os testes, use o seguinte comando: python -m pytest — cov=./ — cov-report html

 

## 📝 Licença
Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE.md para mais detalhes

## 📫 Integrantes

1. Igor Bruno
2. Luiz Carlos - @luizcs-code
3. Vinicius Gomes
4. Elzo Santos - @elzosantos

### Agradecimentos
Prof. Rodrigo Viannini

