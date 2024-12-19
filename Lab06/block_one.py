def convert_to_kilograms(unit, mass):
    if unit == 1:
        return mass  # килограммы
    elif unit == 2:
        return mass / 1_000_000  # миллиграммы
    elif unit == 3:
        return mass / 1_000  # граммы
    elif unit == 4:
        return mass * 1_000  # тонны
    elif unit == 5:
        return mass * 100  # центнеры
    else:
        raise ValueError(
            "Некорректный номер единицы измерения. Введите число от 1 до 5."
        )


# Основная программа
try:
    print("Выберите единицу измерения массы:")
    print("1 — килограмм\n2 — миллиграмм\n3 — грамм\n4 — тонна\n5 — центнер")
    unit = int(input("Введите номер единицы измерения (1-5): "))
    mass = float(input("Введите массу в выбранной единице измерения: "))

    mass_in_kg = convert_to_kilograms(unit, mass)
    print(f"Масса в килограммах: {mass_in_kg:.6f} кг")
except ValueError as e:
    print(f"Ошибка: {e}")
