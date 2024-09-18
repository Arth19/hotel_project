import os
import uuid
from pymongo import MongoClient, UpdateOne
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# String de conexão obtida do arquivo .env
MONGO_URI = os.getenv('MONGO_URI')

# Criar o cliente MongoDB com ServerApi
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Selecionar o banco de dados
db = client['HOTEL']

# Função para adicionar UUID em todos os documentos de uma coleção usando bulk_write
def adicionar_uuid_a_todos_bulk(colecao):
    collection = db[colecao]
    documentos_sem_uuid = collection.find({"uuid": {"$exists": False}})  # Filtrar documentos que ainda não têm UUID

    # Lista para armazenar as operações de atualização
    operacoes = []

    for documento in documentos_sem_uuid:
        novo_uuid = str(uuid.uuid4())  # Gerar um UUID
        operacoes.append(UpdateOne({"_id": documento["_id"]}, {"$set": {"uuid": novo_uuid}}))

    # Executar operações em lote (bulk)
    if operacoes:
        result = collection.bulk_write(operacoes)
        print(f"Adicionado UUID para {result.modified_count} documentos na coleção {colecao}")

# Atualizar todas as coleções em paralelo
def atualizar_todas_as_colecoes_com_uuid():
    colecoes = ["hospedes", "funcionarios", "quartos"]

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(adicionar_uuid_a_todos_bulk, colecoes)

# Executar o script para atualizar todas as coleções
if __name__ == "__main__":
    atualizar_todas_as_colecoes_com_uuid()
