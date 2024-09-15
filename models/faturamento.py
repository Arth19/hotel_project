import uuid
from datetime import datetime

class Faturamento:
    def __init__(self, reserva_id, valor_total, metodo_pagamento, data_pagamento=None, faturamento_id=None):
        self.faturamento_id = faturamento_id if faturamento_id else str(uuid.uuid4())  # Gera UUID automaticamente
        self.reserva_id = reserva_id
        self.valor_total = valor_total
        self.metodo_pagamento = metodo_pagamento
        self.data_pagamento = data_pagamento if data_pagamento else datetime.now()  # Data atual se não for passada

    def to_dict(self):
        return {
            "faturamento_id": self.faturamento_id,
            "reserva_id": self.reserva_id,
            "valor_total": self.valor_total,
            "metodo_pagamento": self.metodo_pagamento,
            "data_pagamento": self.data_pagamento
        }
