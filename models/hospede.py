import uuid  # Para gerar o UUID automaticamente

class Hospede:
    def __init__(self, nome, email, phone_number=None, documento_identificacao=None, data_nascimento=None, historico_reservas=None, _id=None, uuid=None):
        self._id = _id  # ID único gerado automaticamente pelo MongoDB, pode ser None para novos documentos
        self.uuid = uuid or str(uuid.uuid4())  # Gerar um UUID se não for fornecido
        self.nome = nome
        self.email = email  # Email obrigatório
        self.phone_number = phone_number  # Número de telefone opcional
        self.documento_identificacao = documento_identificacao
        self.data_nascimento = data_nascimento
        self.historico_reservas = historico_reservas or []  # Historico de reservas opcional

    def to_dict(self):
        return {
            "_id": self._id,
            "uuid": self.uuid,
            "nome": self.nome,
            "email": self.email,
            "phone-number": self.phone_number,  # Mantém o campo phone-number
            "documento_identificacao": self.documento_identificacao,
            "data_nascimento": self.data_nascimento,
            "historico_reservas": self.historico_reservas
        }
