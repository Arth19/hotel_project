import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# String de conexão obtida do arquivo .env
MONGO_URI = os.getenv('MONGO_URI')

# Criar o cliente MongoDB
client = MongoClient(MONGO_URI)

# Selecionar o banco de dados
db = client['HOTEL']  # Nome do banco de dados

# Funções de CRUD para a coleção "hospedes"
def create_hospede(data):
    collection = db.hospedes
    collection.insert_one(data)
    print("Hóspede criado com sucesso!")

def get_hospedes():
    collection = db.hospedes
    return list(collection.find())

# Funções para outros CRUD (funcionários e quartos) seguem a mesma lógica
