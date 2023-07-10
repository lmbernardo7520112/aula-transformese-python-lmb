def calculadora(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = dividir(num1, num2)
    return (soma, subtracao, multiplicacao, divisao)

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero"

resultado_calculadora = calculadora(10, 5)
print("Resultado da Calculadora:", resultado_calculadora)
