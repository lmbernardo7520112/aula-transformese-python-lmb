from cliente import Cliente
from conta import Conta

def criar_conta(numero, cliente, saldo, limite):
    conta = Conta(numero, cliente, saldo, limite)
    return conta

def depositar(conta, valor):
    conta.depositar(valor)
    print(f"Depósito de R$ {valor} realizado com sucesso!")

def sacar(conta, valor):
    if conta.sacar(valor):
        print(f"Saque de R$ {valor} realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")

def extrato(conta):
    conta.extrato()
    print(conta.historico.transacoes)

# Criando um cliente
cliente = Cliente("João")

# Criando a conta
conta = criar_conta(123, cliente, 1000, 500)

# Testando as operações
depositar(conta, 500)
sacar(conta, 200)
extrato(conta)
