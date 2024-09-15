class Quarto:
    def __init__(self, numero_quarto, tipo, status, preco_diaria, caracteristicas, _id=None):
        self._id = _id  # ID único gerado automaticamente pelo MongoDB
        self.numero_quarto = numero_quarto
        self.tipo = tipo
        self.status = status
        self.preco_diaria = preco_diaria
        self.caracteristicas = caracteristicas  # Lista de características do quarto

    def to_dict(self):
        return {
            "_id": self._id,
            "numero_quarto": self.numero_quarto,
            "tipo": self.tipo,
            "status": self.status,
            "preco_diaria": self.preco_diaria,
            "caracteristicas": self.caracteristicas
        }
