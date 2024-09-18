from astra_api import create_reserva, get_reserva_por_id, update_reserva, delete_reserva
from datetime import datetime

class ReservaController:

    @staticmethod
    def validar_reserva(dados):
        # Validação de nome e email do hóspede
        if "name" not in dados or not dados["name"]:
            raise ValueError("Nome do hóspede é obrigatório")
        
        if "email" not in dados or not dados["email"]:
            raise ValueError("Email do hóspede é obrigatório")

        # Validação da data de check-in e check-out
        if "arrival_date_day_of_month" not in dados or not dados["arrival_date_day_of_month"]:
            raise ValueError("Dia da chegada é obrigatório")
        
        if "arrival_date_month" not in dados or not dados["arrival_date_month"]:
            raise ValueError("Mês da chegada é obrigatório")
        
        if "arrival_date_year" not in dados or not dados["arrival_date_year"]:
            raise ValueError("Ano da chegada é obrigatório")
        
        if "stays_in_week_nights" not in dados or dados["stays_in_week_nights"] < 0:
            raise ValueError("Número de noites durante a semana deve ser informado")
        
        if "stays_in_weekend_nights" not in dados or dados["stays_in_weekend_nights"] < 0:
            raise ValueError("Número de noites no fim de semana deve ser informado")

        # Validação do status da reserva
        if "reservation_status" not in dados or dados["reservation_status"] not in ["confirmed", "canceled", "finalized"]:
            raise ValueError("Status da reserva inválido")

        # Validação do número de adultos e crianças
        if "adults" not in dados or dados["adults"] <= 0:
            raise ValueError("O número de adultos deve ser maior que zero")
        
        if "children" not in dados or dados["children"] < 0:
            raise ValueError("O número de crianças não pode ser negativo")
        
        if "babies" not in dados or dados["babies"] < 0:
            raise ValueError("O número de bebês não pode ser negativo")

        # Validar tipo de quarto reservado
        if "reserved_room_type" not in dados or not dados["reserved_room_type"]:
            raise ValueError("Tipo de quarto reservado é obrigatório")

    @staticmethod
    def criar_reserva(dados):
        # Valida os dados da reserva antes de criar
        ReservaController.validar_reserva(dados)
        create_reserva(dados)
        # print("Reserva criada com sucesso!")

    @staticmethod
    def listar_reservas(reserva_id):
        # Retorna todas as reservas
        return get_reserva_por_id(reserva_id)

    @staticmethod
    def atualizar_reserva(reserva_id, novos_dados):
        # Valida os novos dados da reserva antes de atualizar
        ReservaController.validar_reserva(novos_dados)
        update_reserva(reserva_id, novos_dados)
        print(f"Reserva {reserva_id} atualizada com sucesso!")

    @staticmethod
    def deletar_reserva(reserva_id):
        # Exclui uma reserva com base no ID
        delete_reserva(reserva_id)
        # print(f"Reserva {reserva_id} deletada com sucesso!")
