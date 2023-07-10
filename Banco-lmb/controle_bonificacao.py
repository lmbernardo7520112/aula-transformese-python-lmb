class ControleBonificacao:
    def __init__(self):
        self.total_bonificacao = 0

    def registra(self, funcionario):
        self.total_bonificacao += funcionario.get_bonificacao()

    @property
    def total(self):
        return self.total_bonificacao
