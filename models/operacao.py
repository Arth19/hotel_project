import uuid
from datetime import datetime

class Operacao:
    def __init__(self, reserva_id, tipo_operacao, data_operacao=None, operacao_id=None):
        self.operacao_id = operacao_id if operacao_id else str(uuid.uuid4())  # Gera UUID automaticamente
        self.reserva_id = reserva_id
        self.tipo_operacao = tipo_operacao
        self.data_operacao = data_operacao if data_operacao else datetime.now()  # Data atual se não for passada

    def to_dict(self):
        return {
            "operacao_id": self.operacao_id,
            "reserva_id": self.reserva_id,
            "tipo_operacao": self.tipo_operacao,
            "data_operacao": self.data_operacao
        }
