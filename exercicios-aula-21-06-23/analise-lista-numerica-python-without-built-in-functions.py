lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

# Imprimir o maior elemento
maior_elemento = lista[0]
for num in lista:
    if num > maior_elemento:
        maior_elemento = num
print("Maior elemento:", maior_elemento)

# Imprimir o menor elemento
menor_elemento = lista[0]
for num in lista:
    if num < menor_elemento:
        menor_elemento = num
print("Menor elemento:", menor_elemento)

# Imprimir os números pares
numeros_pares = []
for num in lista:
    if num % 2 == 0:
        numeros_pares.append(num)
print("Números pares:", numeros_pares)

# Imprimir o número de ocorrências do primeiro elemento da lista
primeiro_elemento = lista[0]
ocorrencias_primeiro = 0
for num in lista:
    if num == primeiro_elemento:
        ocorrencias_primeiro += 1
print("Ocorrências do primeiro elemento:", ocorrencias_primeiro)

# Imprimir a média dos elementos
soma = 0
for num in lista:
    soma += num
media = soma / len(lista)
print("Média dos elementos:", media)

# Imprimir a soma dos elementos de valor negativo
soma_negativos = 0
for num in lista:
    if num < 0:
        soma_negativos += num
print("Soma dos elementos negativos:", soma_negativos)
