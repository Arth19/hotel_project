class Funcionario:
    def __init__(self, nome, cargo, data_contratacao, salario, turno, contato, _id=None):
        self._id = _id  # ID único gerado automaticamente pelo MongoDB
        self.nome = nome
        self.cargo = cargo
        self.data_contratacao = data_contratacao
        self.salario = salario
        self.turno = turno
        self.contato = contato  # Contato deve ser um dicionário com 'email' e 'telefone'

    def to_dict(self):
        return {
            "_id": self._id,
            "nome": self.nome,
            "cargo": self.cargo,
            "data_contratacao": self.data_contratacao,
            "salario": self.salario,
            "turno": self.turno,
            "contato": self.contato
        }
