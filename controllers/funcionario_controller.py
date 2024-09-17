# controllers/funcionario_controller.py
from mongo_api import create_funcionario, get_funcionarios, update_funcionario, delete_funcionario
import re

class FuncionarioController:

    @staticmethod
    def validar_funcionario(dados):
        if "nome" not in dados or not dados["nome"]:
            raise ValueError("Nome do funcionário é obrigatório")
        
        if "cargo" not in dados or not dados["cargo"]:
            raise ValueError("Cargo do funcionário é obrigatório")
        
        if "salario" not in dados or dados["salario"] <= 0:
            raise ValueError("Salário deve ser um valor positivo")
        
        contato = dados.get("contato", {})
        if "email" not in contato or not re.match(r"[^@]+@[^@]+\.[^@]+", contato["email"]):
            raise ValueError("Email inválido")
        
        if "telefone" not in contato or len(contato["telefone"]) < 8:
            raise ValueError("Telefone inválido")

    @staticmethod
    def criar_funcionario(dados):
        # Validar dados antes da criação
        FuncionarioController.validar_funcionario(dados)
        create_funcionario(dados)
        print("Funcionário criado com sucesso!")

    @staticmethod
    def listar_funcionarios():
        return get_funcionarios()

    @staticmethod
    def atualizar_funcionario(funcionario_id, novos_dados):
        # Validar os novos dados antes da atualização
        FuncionarioController.validar_funcionario(novos_dados)
        update_funcionario(funcionario_id, novos_dados)
        print(f"Funcionário {funcionario_id} atualizado com sucesso!")

    @staticmethod
    def deletar_funcionario(funcionario_id):
        delete_funcionario(funcionario_id)
        print(f"Funcionário {funcionario_id} deletado com sucesso!")
