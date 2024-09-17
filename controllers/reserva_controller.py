from astra_api import create_reserva, get_reservas, update_reserva, delete_reserva
from datetime import datetime

class ReservaController:

    @staticmethod
    def validar_reserva(dados):
        if "hospede_id" not in dados or not dados["hospede_id"]:
            raise ValueError("ID do hóspede é obrigatório")
        
        if "quarto_id" not in dados or not dados["quarto_id"]:
            raise ValueError("ID do quarto é obrigatório")
        
        if "data_checkin" not in dados or not dados["data_checkin"]:
            raise ValueError("Data de check-in é obrigatória")
        
        if "data_checkout" not in dados or not dados["data_checkout"]:
            raise ValueError("Data de check-out é obrigatória")
        
        data_checkin = datetime.fromisoformat(dados["data_checkin"])
        data_checkout = datetime.fromisoformat(dados["data_checkout"])
        
        if data_checkout <= data_checkin:
            raise ValueError("A data de check-out deve ser posterior à data de check-in")
        
        if "status" not in dados or dados["status"] not in ["confirmada", "cancelada", "finalizada"]:
            raise ValueError("Status da reserva inválido")

    @staticmethod
    def criar_reserva(dados):
        ReservaController.validar_reserva(dados)
        create_reserva(dados)
        print("Reserva criada com sucesso!")

    @staticmethod
    def listar_reservas():
        return get_reservas()

    @staticmethod
    def atualizar_reserva(reserva_id, novos_dados):
        ReservaController.validar_reserva(novos_dados)
        update_reserva(reserva_id, novos_dados)
        print(f"Reserva {reserva_id} atualizada com sucesso!")

    @staticmethod
    def deletar_reserva(reserva_id):
        delete_reserva(reserva_id)
        print(f"Reserva {reserva_id} deletada com sucesso!")
