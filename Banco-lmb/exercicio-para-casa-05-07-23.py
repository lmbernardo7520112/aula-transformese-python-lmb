from cliente import Cliente
from conta import Conta

# Criando 3 clientes
cliente1 = Cliente("João")
cliente2 = Cliente("Maria")
cliente3 = Cliente("Pedro")

# Criando 3 contas, uma para cada cliente
conta1 = Conta(123, cliente1, 1000, 500)
conta2 = Conta(456, cliente2, 2000, 1000)
conta3 = Conta(789, cliente3, 500, 200)

# Fazendo uma operação de depósito em cada conta
conta1.depositar(500)
conta2.depositar(1000)
conta3.depositar(200)

# Fazendo uma operação de saque em cada conta
conta1.sacar(300)
conta2.sacar(500)
conta3.sacar(100)

# Transferindo dinheiro entre duas contas quaisquer
conta1.transferir(conta3, 200)

# Tirando o extrato de cada conta
conta1.extrato()
conta2.extrato()
conta3.extrato()

# Imprimindo informações de uma conta específica
print("Informações da Conta 1:")
print("Titular:", conta1.titular)
print("Número:", conta1.numero)
print("Saldo:", conta1.saldo)
print("Identificador:", Conta.get_total_de_contas())
print("Histórico:", conta1.historico.transacoes)
