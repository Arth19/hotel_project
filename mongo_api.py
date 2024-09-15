import os
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
    print("Hóspede criado com sucesso!")

def get_hospedes():
    collection = db.hospedes
    return list(collection.find())

def update_hospede(hospede_id, novos_dados):
    collection = db.hospedes
    result = collection.update_one({"_id": ObjectId(hospede_id)}, {"$set": novos_dados})
    if result.matched_count > 0:
        print(f"Hóspede {hospede_id} atualizado com sucesso!")
    else:
        print(f"Hóspede {hospede_id} não encontrado.")

def delete_hospede(hospede_id):
    collection = db.hospedes
    result = collection.delete_one({"_id": ObjectId(hospede_id)})
    if result.deleted_count > 0:
        print(f"Hóspede {hospede_id} deletado com sucesso!")
    else:
        print(f"Hóspede {hospede_id} não encontrado.")

# Funções de CRUD para a coleção "funcionarios"
def create_funcionario(data):
    collection = db.funcionarios
    collection.insert_one(data)
    print("Funcionário criado com sucesso!")

def get_funcionarios():
    collection = db.funcionarios
    return list(collection.find())

def update_funcionario(funcionario_id, novos_dados):
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
    collection = db.quartos
    collection.insert_one(data)
    print("Quarto criado com sucesso!")

def get_quartos():
    collection = db.quartos
    return list(collection.find())

def update_quarto(quarto_id, novos_dados):
    collection = db.quartos
    result = collection.update_one({"_id": ObjectId(quarto_id)}, {"$set": novos_dados})
    if result.matched_count > 0:
        print(f"Quarto {quarto_id} atualizado com sucesso!")
    else:
        print(f"Quarto {quarto_id} não encontrado.")

def delete_quarto(quarto_id):
    collection = db.quartos
    result = collection.delete_one({"_id": ObjectId(quarto_id)})
    if result.deleted_count > 0:
        print(f"Quarto {quarto_id} deletado com sucesso!")
    else:
        print(f"Quarto {quarto_id} não encontrado.")
