# n = int(input("Введите длину массива n: "))

# if n <= 0:
#   print("Длина массива должна быть больше 0.")
# else:
# D = []
# print("Введите элементы массива:")
# for i in range(n):
# element = float(input(f"Элемент {i}: "))
# D.append(element)

# index_sum = 0
# for i in range(1, n, 2):
# index_sum += D[i]

# print("Массив D:", D)
# print("Сумма элементов с нечетными индексами:", index_sum)


D = []
print("Введите 8 элементов массива:")
for i in range(8):
    element = int(input(f"Элемент {i + 1}: "))
    D.append(element)

print("Исходный массив :      ", D)
for i in range(len(D)):
    if D[i] < 15:
        D[i] = D[i] * 2

print("Преобразованный массив:", D)
