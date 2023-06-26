# Criei um código para gerar combinações de jogos para mega-sena a partir de uma lista de números. Esta lista é comparada com outra cujos valores são os
# mais sorteados em uma série de anos conforme estudo obtido no link: https://www.kaggle.com/code/lidialucena/mega-sena/notebook

import random

def generate_combinations(number_list, combination_size):
    sorted_numbers = sorted(number_list)
    all_combinations = {}

    def backtrack(start, current_combination):
        if len(current_combination) == combination_size:
            all_combinations[len(all_combinations) + 1] = tuple(current_combination)
            return

        for i in range(start, len(sorted_numbers)):
            current_combination.append(sorted_numbers[i])
            backtrack(i + 1, current_combination)
            current_combination.pop()

    backtrack(0, [])
    return all_combinations

def calculate_number_of_combinations(n, r):
    if r > n:
        return 0

    numerator = 1
    denominator = 1

    for i in range(r):
        numerator *= n - i
        denominator *= i + 1

    return numerator // denominator

def count_sorted_numbers(combination, sorted_numbers):
    count = 0
    for num in combination:
        if num in sorted_numbers:
            count += 1
    return count

# Example usage
numbers = [46, 27, 19, 47, 51, 50, 31, 28, 17, 2, 48, 23]  # Your list of numbers
combination_size = 6  # Size of each combination

all_combinations = generate_combinations(numbers, combination_size)
sorted_numbers = [54, 4, 24, 51, 36, 33, 23, 53, 10, 5]

# Filter combinations that have the most sorted numbers
filtered_combinations = set()
max_sorted_count = 0

for combination in all_combinations.values():
    sorted_count = count_sorted_numbers(combination, sorted_numbers)
    if sorted_count > max_sorted_count:
        filtered_combinations = {tuple(combination)}
        max_sorted_count = sorted_count
    elif sorted_count == max_sorted_count:
        filtered_combinations.add(tuple(combination))

number_of_combinations = len(filtered_combinations)

# Randomly select three combinations with the highest probability of sorted numbers
selected_combinations = random.sample(sorted(filtered_combinations), min(3, number_of_combinations))

print("Number of combinations:", number_of_combinations)
print("Filtered combinations with most sorted numbers:", filtered_combinations)
print("Selected combinations:", selected_combinations)