def StockPicker(arr):
    max_profit = -1  # Variável para armazenar o lucro máximo
    buy_index = 0  # Índice de compra inicial
    sell_index = 0  # Índice de venda inicial

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            profit = arr[j] - arr[i]  # Calcula o lucro potencial

            if profit > max_profit:
                max_profit = profit
                buy_index = i
                sell_index = j

    if max_profit > 0:
        return max_profit
    else:
        return -1


prices = [44, 30, 24, 32, 35, 30, 40, 38, 15]
print(StockPicker(prices))  # Saída: 16

prices = [10, 9, 8, 2]
print(StockPicker(prices))  # Saída: -1
