import os
import uuid  # Import necessário para gerar UUID
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId  # Para lidar com IDs do MongoDB

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
    # print("Hóspede criado com sucesso!")

def get_hospedes():
    collection = db.hospedes
    return list(collection.find())

def update_hospede(email, novos_dados):
    collection = db.hospedes
    result = collection.update_one({"email": email}, {"$set": novos_dados})  # Buscar pelo campo email
    if result.matched_count > 0:
        print(f"Hóspede com email {email} atualizado com sucesso!")
    else:
        print(f"Hóspede com email {email} não encontrado.")

def delete_hospede(email):
    collection = db.hospedes
    result = collection.delete_one({"email": email})
    if result.deleted_count > 0:
        print(f"Hóspede com email {email} deletado com sucesso!")
    else:
        print(f"Hóspede com email {email} não encontrado.")

# Funções de CRUD para a coleção "funcionarios"
def create_funcionario(data):
    data['uuid'] = str(uuid.uuid4())  # Gerar e adicionar UUID ao funcionário
    collection = db.funcionarios
    collection.insert_one(data)
    # print("Funcionário criado com sucesso!")

def get_funcionarios():
    collection = db.funcionarios
    return list(collection.find())

def update_funcionario(funcionario_id, novos_dados):
    novos_dados['uuid'] = str(uuid.uuid4())  # Gerar e adicionar novo UUID ao funcionário atualizado
    collection = db.funcionarios
    result = collection.update_one({"_id": ObjectId(funcionario_id)}, {"$set": novos_dados})
    if result.matched_count > 0:
        print(f"Funcionário {funcionario_id} atualizado com sucesso!")
    else:
        print(f"Funcionário {funcionario_id} não encontrado.")

def delete_funcionario(funcionario_id):
    collection = db.funcionarios
    result = collection.delete_one({"_id": ObjectId(funcionario_id)})
    if result.deleted_count > 0:
        print(f"Funcionário {funcionario_id} deletado com sucesso!")
    else:
        print(f"Funcionário {funcionario_id} não encontrado.")

# Funções de CRUD para a coleção "quartos"
def create_quarto(data):
    data['uuid'] = str(uuid.uuid4())  # Gerar e adicionar UUID ao quarto
    collection = db.quartos
    collection.insert_one(data)
    # print("Quarto criado com sucesso!")

def get_quartos():
    collection = db.quartos
    return list(collection.find())

def update_quarto(numero_quarto, novos_dados):
    novos_dados['uuid'] = str(uuid.uuid4())  # Gerar e adicionar novo UUID ao quarto atualizado
    collection = db.quartos
    result = collection.update_one({"numero_quarto": numero_quarto}, {"$set": novos_dados})
    if result.matched_count > 0:
        print(f"Quarto com número {numero_quarto} atualizado com sucesso!")
    else:
        print(f"Quarto com número {numero_quarto} não encontrado.")

def delete_quarto(numero_quarto):
    collection = db.quartos
    result = collection.delete_one({"numero_quarto": numero_quarto})
    if result.deleted_count > 0:
        print(f"Quarto com número {numero_quarto} deletado com sucesso!")
    else:
        print(f"Quarto com número {numero_quarto} não encontrado.")
