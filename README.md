# Hotel Management System

Este projeto é uma aplicação para gerenciamento de um sistema hoteleiro, que permite a administração de reservas, hóspedes, quartos, faturamento e operações. A aplicação interage com dois bancos de dados: **MongoDB** (para gerenciar hóspedes, funcionários e quartos) e **Cassandra** (para gerenciar reservas, faturamento e operações).

## Funcionalidades

- Gerenciamento de hóspedes, funcionários e quartos (armazenados no MongoDB)
- CRUD completo para reservas, faturamento e operações (armazenados no Cassandra)
- Conexão segura com MongoDB Atlas e DataStax Astra (Cassandra)
  
## Requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- [Python 3.12.6+](https://www.python.org/downloads/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [DataStax Astra](https://www.datastax.com/)
- [Git](https://git-scm.com/)

## Configuração do Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/hotel_project.git
cd hotel_project
```

### 2. Crie e Ative o Ambiente Virtual

```bash
# No Linux/MacOS
python3 -m venv myenv
source myenv/bin/activate

# No Windows
python -m venv myenv
myenv\Scripts\activate
```

### 3. Instale as Dependências

Instale as dependências necessárias executando:

```bash
pip install -r requirements.txt
```

### 4. Configuração das Variáveis de Ambiente

Crie um arquivo **`.env`** na raiz do projeto e adicione as seguintes variáveis de ambiente, substituindo pelos seus próprios valores:

```bash
# MongoDB Atlas Connection
MONGO_URI=mongodb+srv://Cluster80112:<senha>@cluster80112.ooezbhi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster80112

# DataStax Astra Cassandra Connection
ASTRA_DB_ID=<id_do_db>
ASTRA_DB_REGION=eu-west-1
ASTRA_DB_APPLICATION_TOKEN=<token>
ASTRA_DB_KEYSPACE=hotel
ASTRA_SECURE_BUNDLE_PATH=./secure-connect-projeto.zip
```

### 5. Executando a Aplicação

Após configurar as variáveis de ambiente e instalar as dependências, você pode rodar o projeto.

#### Exemplo de como rodar uma operação para buscar hóspedes no MongoDB:

```bash
python app.py
```

A aplicação irá executar o script principal definido em **app.py**, que contém funções de teste para CRUD.

## Estrutura do Projeto

```bash
hotel_project/
├── app.py                   # Arquivo principal que orquestra a aplicação
├── astra_api.py              # Lida com a comunicação e CRUD para Cassandra
├── mongo_api.py              # Lida com a comunicação e CRUD para MongoDB
├── controllers/              # Controladores para lógica de negócios
│   ├── reserva_controller.py # Lógica para CRUD de reservas (Cassandra)
│   ├── hospede_controller.py # Lógica para CRUD de hóspedes (MongoDB)
│   ├── funcionario_controller.py # Lógica para CRUD de funcionários (MongoDB)
│   ├── operacao_controller.py # Lógica para CRUD de operacoes (MongoDB)
│   ├── faturamento_controller.py # Lógica para CRUD de faturamento (MongoDB)
│   └── quarto_controller.py  # Lógica para CRUD de quartos (MongoDB)
├── models/                   # Modelos de dados para Cassandra e MongoDB
│   ├── reserva.py            # Modelo de reservas (Cassandra)
│   ├── faturamento.py        # Modelo de faturamento (Cassandra)
│   ├── operacao.py           # Modelo de operações (Cassandra)
│   ├── hospede.py            # Modelo de hóspedes (MongoDB)
│   ├── funcionario.py        # Modelo de funcionários (MongoDB)
│   └── quarto.py             # Modelo de quartos (MongoDB)
├── myenv/                    # Ambiente virtual (não versionado)
├── requirements.txt          # Dependências do projeto
├── .env                      # Arquivo de variáveis de ambiente (não versionado)
└── README.md                 # Documentação do projeto
```

## Dependências

As dependências do projeto são gerenciadas no arquivo **`requirements.txt`**. Certifique-se de atualizar este arquivo sempre que adicionar novas bibliotecas.
