class Funcionario:
    def __init__(self, nome, salario, tempo_de_casa):
        self._nome = nome
        self._salario = salario
        self._tempo_de_casa = tempo_de_casa

    def get_bonificacao(self):
        return self._salario * 0.10

    def __str__(self):
        return f'Funcionário\nNome: {self._nome}\nSalário: {self._salario}\nTempo de Casa: {self._tempo_de_casa}'
