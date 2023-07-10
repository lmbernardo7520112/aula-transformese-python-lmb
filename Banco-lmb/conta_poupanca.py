from conta import Conta

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3

    def __str__(self):
        return f'Conta Poupança\nNúmero: {self.numero}\nTitular: {self.titular}\nSaldo: {self.saldo}'
