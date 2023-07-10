from funcionario import Funcionario

class Diretor(Funcionario):
    def __init__(self, nome, salario, senha, tempo_de_casa):
        super().__init__(nome, salario, tempo_de_casa)
        self._senha = senha

    def autentica(self, senha):
        return self._senha == senha

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000
