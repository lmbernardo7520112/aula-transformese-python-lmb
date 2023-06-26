lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

# Imprimir o maior elemento
maior_elemento = max(lista)
print("Maior elemento:", maior_elemento)

# Imprimir o menor elemento
menor_elemento = min(lista)
print("Menor elemento:", menor_elemento)

# Imprimir os números pares
numeros_pares = [num for num in lista if num % 2 == 0]
print("Números pares:", numeros_pares)

# Imprimir o número de ocorrências do primeiro elemento da lista
primeiro_elemento = lista[0]
ocorrencias_primeiro = lista.count(primeiro_elemento)
print("Ocorrências do primeiro elemento:", ocorrencias_primeiro)

# Imprimir a média dos elementos
media = sum(lista) / len(lista)
print("Média dos elementos:", media)

# Imprimir a soma dos elementos de valor negativo
soma_negativos = sum(num for num in lista if num < 0)
print("Soma dos elementos negativos:", soma_negativos)