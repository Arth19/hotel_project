from mongo_api import create_hospede, get_hospedes, update_hospede, delete_hospede
import re, uuid

class HospedeController:

    @staticmethod
    def validar_hospede(dados):
        if "nome" not in dados or not dados["nome"]:
            raise ValueError("Nome do hóspede é obrigatório")

        if "documento_identificacao" not in dados or len(dados["documento_identificacao"]) != 11:
            raise ValueError("Documento de identificação (CPF) inválido. Deve ter 11 dígitos.")
        
        # Validação do email diretamente no nível principal dos dados
        if "email" not in dados or not re.match(r"[^@]+@[^@]+\.[^@]+", dados["email"]):
            raise ValueError("Email inválido")


    @staticmethod
    def criar_hospede(dados):
        dados["uuid"] = str(uuid.uuid4())

        # Validar dados antes da criação
        HospedeController.validar_hospede(dados)
        create_hospede(dados)
        print("Hóspede criado com sucesso!")

    @staticmethod
    def listar_hospedes():
        return get_hospedes()

    @staticmethod
    def atualizar_hospede(hospede_id, novos_dados):
        # Validar os novos dados antes da atualização
        HospedeController.validar_hospede(novos_dados)
        update_hospede(hospede_id, novos_dados)
        print(f"Hóspede {hospede_id} atualizado com sucesso!")

    @staticmethod
    def deletar_hospede(hospede_id):
        delete_hospede(hospede_id)
        print(f"Hóspede {hospede_id} deletado com sucesso!")
