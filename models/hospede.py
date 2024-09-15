class Hospede:
    def __init__(self, nome, documento_identificacao, data_nascimento, historico_reservas, contato, _id=None):
        self._id = _id  # ID único gerado automaticamente pelo MongoDB, pode ser None para novos documentos
        self.nome = nome
        self.documento_identificacao = documento_identificacao
        self.data_nascimento = data_nascimento
        self.historico_reservas = historico_reservas  # Deve ser uma lista de IDs de reservas
        self.contato = contato  # Contato deve ser um dicionário com 'email' e 'telefone'

    def to_dict(self):
        return {
            "_id": self._id,
            "nome": self.nome,
            "documento_identificacao": self.documento_identificacao,
            "data_nascimento": self.data_nascimento,
            "historico_reservas": self.historico_reservas,
            "contato": self.contato
        }
