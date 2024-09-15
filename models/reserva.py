import uuid
from datetime import datetime

class Reserva:
    def __init__(self, hospede_id, quarto_id, data_checkin, data_checkout, status, reserva_id=None, data_reserva=None):
        self.reserva_id = reserva_id if reserva_id else str(uuid.uuid4())  # Gera UUID automaticamente se não for passado
        self.hospede_id = hospede_id
        self.quarto_id = quarto_id
        self.data_reserva = data_reserva if data_reserva else datetime.now()  # Data atual se não for passada
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status = status

    def to_dict(self):
        return {
            "reserva_id": self.reserva_id,
            "hospede_id": self.hospede_id,
            "quarto_id": self.quarto_id,
            "data_reserva": self.data_reserva,
            "data_checkin": self.data_checkin,
            "data_checkout": self.data_checkout,
            "status": self.status
        }
