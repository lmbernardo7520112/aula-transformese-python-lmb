from controle_bonificacao import ControleBonificacao
from diretor import Diretor
from funcionario import Funcionario
from gerente import Gerente

# Criando instâncias de Funcionario, Gerente e Diretor
funcionario1 = Funcionario("João", 5000, 2)
gerente1 = Gerente("Maria", 6000, "senha123", 3)
diretor1 = Diretor("Carlos", 8000, "senha456", 5)

# Imprimindo informações dos funcionários, gerente e diretor
print(funcionario1)
print(gerente1)
print(diretor1)

# Criando instância de ControleBonificacao
controle_bonificacao = ControleBonificacao()

# Registrando os funcionários, gerente e diretor no controle de bonificações
controle_bonificacao.registra(funcionario1)
controle_bonificacao.registra(gerente1)
controle_bonificacao.registra(diretor1)

# Obtendo o total de bonificações registradas
total_bonificacoes = controle_bonificacao.total

print(f"Total de bonificações: R$ {total_bonificacoes}")
