from mongo_api import create_hospede, get_hospedes, update_hospede, delete_hospede
import re

class HospedeController:

    @staticmethod
    def validar_hospede(dados):
        if "nome" not in dados or not dados["nome"]:
            raise ValueError("Nome do hóspede é obrigatório")
        
        if "documento_identificacao" not in dados or len(dados["documento_identificacao"]) != 11:
            raise ValueError("Documento de identificação (CPF) inválido. Deve ter 11 dígitos.")
        
        contato = dados.get("contato", {})
        if "email" not in contato or not re.match(r"[^@]+@[^@]+\.[^@]+", contato["email"]):
            raise ValueError("Email inválido")
        
        if "telefone" not in contato or len(contato["telefone"]) < 8:
            raise ValueError("Telefone inválido")

    @staticmethod
    def criar_hospede(dados):
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
