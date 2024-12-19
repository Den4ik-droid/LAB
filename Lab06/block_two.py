# n = int(input("Введите количество элементов в цепи: "))

# total_resistance = 0

# for i in range(1, n + 1):
# resistance = float(input(f"Введите сопротивление элемента {i} (Ом): "))
# total_resistance += resistance

##print(f"Общее сопротивление цепи: {total_resistance} Ом")


N = int(input("Введите целое число N (> 0): "))


if N <= 0:
    print("Число должно быть больше 0.")
else:
    K = 0

    while (K + 1) ** 2 <= N:
        K += 1

    print(f"Наибольшее целое число K, квадрат которого не превосходит {N}: {K}")
