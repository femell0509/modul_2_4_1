# Просты и сложные числа
numbers = []
for i in range(1, 16):
    numbers.append(i)
print('numbers = ', numbers)
prime = []  # Список с простыми числами
not_prime = []  # Список с составными числами
for i in numbers[1:]:
    is_prime = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            is_prime = False
    if is_prime == False:
        not_prime.append(i)
    else:
        prime.append(i)
print(f'{prime= }')
print(f'{not_prime= }')
