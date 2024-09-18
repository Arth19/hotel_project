import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

ASTRA_DB_ID = os.getenv('ASTRA_DB_ID')
ASTRA_DB_REGION = os.getenv('ASTRA_DB_REGION')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')

BASE_URL = f"https://{ASTRA_DB_ID}-{ASTRA_DB_REGION}.apps.astra.datastax.com/api/rest/v2/keyspaces/{ASTRA_DB_KEYSPACE}/"

HEADERS = {
    "X-Cassandra-Token": ASTRA_DB_APPLICATION_TOKEN,
    "Content-Type": "application/json"
}

# Funções CRUD para Reservas
# Criar uma nova reserva
def create_reserva(data):
    url = f"{BASE_URL}reservas"
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print("Reserva criada com sucesso!")
    else:
        print(f"Erro ao criar reserva: {response.status_code} - {response.text}")

def get_reserva_por_id(reserva_id):
    url = f'{BASE_URL}/reservas'
    
    # Adicionar um filtro 'where' para buscar pelo reserva_id
    params = {
        'where': f'{{"reserva_id": {{"$eq": "{reserva_id}"}}}}'
    }
    
    response = requests.get(url, headers=HEADERS, params=params)
    
    # Exibir a resposta completa da API para depuração
    print(f"Resposta da API: {response.json()}")
    
    if response.status_code == 200:
        reservas = response.json().get("data", [])
        if reservas:
            return reservas[0]  # Retorna a primeira reserva encontrada
        else:
            print("Nenhuma reserva encontrada.")
            return None
    else:
        print(f"Erro ao buscar reserva: {response.status_code} - {response.text}")
        return None

# Atualizar uma reserva existente
def update_reserva(reserva_id, novos_dados):
    url = f"{BASE_URL}reservas/{reserva_id}"
    response = requests.put(url, headers=HEADERS, json=novos_dados)
    if response.status_code == 200:
        print(f"Reserva {reserva_id} atualizada com sucesso!")
    else:
        print(f"Erro ao atualizar reserva: {response.status_code} - {response.text}")

# Deletar uma reserva
def delete_reserva(reserva_id):
    url = f"{BASE_URL}reservas/{reserva_id}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Reserva {reserva_id} deletada com sucesso!")
    else:
        print(f"Erro ao deletar reserva: {response.status_code} - {response.text}")

# Funções CRUD para Faturamento
# Criar um novo registro de faturamento
def create_faturamento(data):
    url = f"{BASE_URL}faturamento"
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print("Faturamento criado com sucesso!")
    else:
        print(f"Erro ao criar faturamento: {response.status_code} - {response.text}")

# Obter todos os registros de faturamento
def get_faturamentos():
    url = f"{BASE_URL}faturamento"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        print(f"Erro ao buscar faturamentos: {response.status_code} - {response.text}")
        return []

# Atualizar um registro de faturamento existente
def update_faturamento(faturamento_id, novos_dados):
    url = f"{BASE_URL}faturamento/{faturamento_id}"
    response = requests.put(url, headers=HEADERS, json=novos_dados)
    if response.status_code == 200:
        print(f"Faturamento {faturamento_id} atualizado com sucesso!")
    else:
        print(f"Erro ao atualizar faturamento: {response.status_code} - {response.text}")

# Deletar um registro de faturamento
def delete_faturamento(faturamento_id):
    url = f"{BASE_URL}faturamento/{faturamento_id}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Faturamento {faturamento_id} deletado com sucesso!")
    else:
        print(f"Erro ao deletar faturamento: {response.status_code} - {response.text}")

# Funções CRUD para Operações (Check-in, Check-out)

# Criar uma nova operação
def create_operacao(data):
    url = f"{BASE_URL}operacoes"
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print("Operação criada com sucesso!")
    else:
        print(f"Erro ao criar operação: {response.status_code} - {response.text}")

# Obter todas as operações
def get_operacoes():
    url = f"{BASE_URL}operacoes"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        print(f"Erro ao buscar operações: {response.status_code} - {response.text}")
        return []

# Atualizar uma operação existente
def update_operacao(operacao_id, novos_dados):
    url = f"{BASE_URL}operacoes/{operacao_id}"
    response = requests.put(url, headers=HEADERS, json=novos_dados)
    if response.status_code == 200:
        print(f"Operação {operacao_id} atualizada com sucesso!")
    else:
        print(f"Erro ao atualizar operação: {response.status_code} - {response.text}")

# Deletar uma operação
def delete_operacao(operacao_id):
    url = f"{BASE_URL}operacoes/{operacao_id}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Operação {operacao_id} deletada com sucesso!")
    else:
        print(f"Erro ao deletar operação: {response.status_code} - {response.text}")
