import uuid
from controllers.hospede_controller import HospedeController
from controllers.quarto_controller import QuartoController
from controllers.reserva_controller import ReservaController
from controllers.faturamento_controller import FaturamentoController
from controllers.operacao_controller import OperacaoController
from controllers.funcionario_controller import FuncionarioController
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Variável global para armazenar a reserva criada
reserva_criada = None

# Função de confirmação antes de prosseguir
def confirmar(mensagem):
    resposta = input(f"{mensagem} (s/n): ").lower()
    return resposta == 's'

# 1. Inserir um novo hóspede e criar uma reserva
def criar_reserva_com_hospede_novo():
    global reserva_criada
    novo_hospede = {
        "nome": "Pedro Henrique",
        "email": "pedro.henrique@example.com",  # Email diretamente aqui
        "documento_identificacao": "98765432100",
        "data_nascimento": "1995-08-17"
    }
    HospedeController.criar_hospede(novo_hospede)

    hospedes = HospedeController.listar_hospedes()
    novo_hospede = hospedes[-1]  # Pega o último hóspede criado

    quartos = QuartoController.listar_quartos()
    primeiro_quarto_numero = quartos[0]["numero_quarto"]

    # Ajustando os dados da reserva para corresponder à tabela no Cassandra
    nova_reserva = {
        "reserva_id": str(uuid.uuid4()),
        "name": novo_hospede["nome"],
        "email": novo_hospede["email"],
        "phone-number": "81999999999",
        "arrival_date_day_of_month": 20,
        "arrival_date_month": "September",
        "arrival_date_year": 2024,
        "reserved_room_type": "Suite Master",
        "stays_in_week_nights": 5,
        "stays_in_weekend_nights": 2,
        "adults": 2,
        "children": 0,
        "babies": 0,
        "country": "BR",
        "hotel": "City Hotel",
        "reservation_status": "confirmed"
    }

    ReservaController.criar_reserva(nova_reserva)
    reserva_criada = nova_reserva  # Armazena a reserva criada globalmente
    print(f"Reserva criada para o hóspede {novo_hospede['nome']} com sucesso!")


# 2. Buscar a reserva criada no passo 1
def buscar_reserva():
    if reserva_criada:
        reserva_id = reserva_criada["reserva_id"]
        reservas = ReservaController.listar_reservas(reserva_id)
        # reserva_encontrada = next((reserva for reserva in reservas if reserva["reserva_id"] == reserva_id), None)
        if reservas:
            print("Reserva encontrada:")
            print(reservas)
        else:
            print(f"Reserva {reserva_id} não encontrada.")
    else:
        print("Nenhuma reserva foi criada para buscar.")

# 3. Inserir registro de faturamento com a reserva criada
def criar_faturamento():
    if reserva_criada:
        faturamento = {
            "faturamento_id": str(uuid.uuid4()),
            "reserva_id": reserva_criada["reserva_id"],
            "valor_total": 1500.00,
            "metodo_pagamento": "cartao_credito",  # Método de pagamento válido
            "data_pagamento": "2024-09-20T14:00:00Z"  # Data do pagamento
        }
        FaturamentoController.criar_faturamento(faturamento)
        print("Faturamento registrado com sucesso!")
    else:
        print("Nenhuma reserva foi criada para vincular o faturamento.")

# 4. Criar uma operação (check-in) com a reserva criada
def criar_operacao():
    if reserva_criada:
        operacao = {
            "operacao_id": str(uuid.uuid4()),  # ID da operação
            "reserva_id": reserva_criada["reserva_id"],  # ID da reserva vinculada
            "tipo_operacao": "check-in",  # Tipo da operação, corrigido para "tipo_operacao"
            "data_operacao": "2024-09-20T14:00:00Z"  # Data da operação
        }
        OperacaoController.criar_operacao(operacao)
        print("Operação de check-in registrada com sucesso!")
    else:
        print("Nenhuma reserva foi criada para vincular a operação.")

# 5. Remover a reserva criada e verificar a remoção
def remover_reserva():
    if reserva_criada:
        reserva_id = reserva_criada["reserva_id"]
        ReservaController.deletar_reserva(reserva_id)
        print(f"Reserva {reserva_id} removida com sucesso!")
        
        # Verificar se a reserva foi removida
        reservas = ReservaController.listar_reservas(reserva_id)
        # reserva_encontrada = next((reserva for reserva in reservas if reserva["reserva_id"] == reserva_id), None)
        if reservas:
            print("Erro: A reserva ainda está presente!")
        else:
            print(f"Reserva {reserva_id} confirmada como removida.")
    else:
        print("Nenhuma reserva foi criada para remover.")

# 6. Inserir um novo funcionário
def inserir_funcionario():
    novo_funcionario = {
        "nome": "Ana Souza",
        "email": "ana.souza@example.com",  # Adicionando o email
        "cargo": "Recepcionista",
        "data_contratacao": "2024-09-15",
        "salario": 3000.00
    }
    FuncionarioController.criar_funcionario(novo_funcionario)
    print("Funcionário inserido com sucesso!")

# 7. Editar um quarto e mostrar antes e depois
def editar_quarto():
    quartos = QuartoController.listar_quartos()
    quarto_numero = quartos[0]["numero_quarto"]  # Seleciona o primeiro quarto pelo número

    # Mostrar o estado atual do quarto
    print("Estado atual do quarto:")
    print(quartos[0])

    # Incluindo o campo numero_quarto nos novos dados
    novos_dados = {
        "numero_quarto": quarto_numero,  # Incluindo o numero_quarto
        "tipo": "Suite Master",
        "preco_diaria": 550.00,  # Preço como float, não string
        "status": "disponível",
        "caracteristicas": ["ar-condicionado", "TV", "wi-fi", "banheira"]
    }

    QuartoController.atualizar_quarto(quarto_numero, novos_dados)
    print(f"Quarto {quarto_numero} atualizado com sucesso!")

    # Mostrar o estado atualizado do quarto
    quartos_atualizados = QuartoController.listar_quartos()
    quarto_atualizado = next((quarto for quarto in quartos_atualizados if quarto["numero_quarto"] == quarto_numero), None)
    print("Estado atualizado do quarto:")
    print(quarto_atualizado)

# Sequência de apresentação
if __name__ == "__main__":
    print(f"Keyspace configurado: {os.getenv('ASTRA_DB_KEYSPACE')}")

    if confirmar("Deseja criar uma nova reserva com hóspede novo?"):
        criar_reserva_com_hospede_novo()

    if confirmar("Deseja buscar a reserva criada?"):
        buscar_reserva()

    if confirmar("Deseja criar um novo faturamento?"):
        criar_faturamento()

    if confirmar("Deseja registrar uma nova operação de check-in?"):
        criar_operacao()

    if confirmar("Deseja remover a reserva criada e verificar a remoção?"):
        remover_reserva()

    if confirmar("Deseja inserir um novo funcionário?"):
        inserir_funcionario()

    if confirmar("Deseja editar um quarto e mostrar o antes e depois?"):
        editar_quarto()
