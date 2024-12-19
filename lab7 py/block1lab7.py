# Открытие исходного файла и запись результата в новый файл
input_file = "input.txt"
output_file = "output.txt"

try:
    with open(input_file, "r", encoding="utf-8") as infile, open(
        output_file, "w", encoding="utf-8"
    ) as outfile:
        for line in infile:
            # Перевод всех слов в строке в нижний регистр
            outfile.write(line.lower())
    print(f"Результат записан в файл {output_file}.")
except FileNotFoundError:
    print(f"Файл {input_file} не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
