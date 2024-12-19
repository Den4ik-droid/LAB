def arithmetic_progression(a1, d, n):
    if n == 1:
        return a1
    else:
        return arithmetic_progression(a1, d, n - 1) + d


a1 = float(input("Введите первый член прогрессии (a1): "))
d = float(input("Введите разность прогрессии (d): "))
n = int(input("Введите номер члена прогрессии (n): "))

nth_term = arithmetic_progression(a1, d, n)

print(f"{n}-й член арифметической прогрессии: {nth_term}")
