import requests
import json

# URL API
BASE_URL = "https://restcountries.com/v3.1"
ALL_COUNTRIES_ENDPOINT = f"{BASE_URL}/all"

# Получение данных о странах
response = requests.get(ALL_COUNTRIES_ENDPOINT)
response.raise_for_status()
all_countries = response.json()

# Фильтрация стран
filtered_countries = []
for country in all_countries:
    region = country.get("region", "")
    area = country.get("area", 0)
    currencies = country.get("currencies", {})
    population = country.get("population", 0)

    # Проверяем условия
    if (
        region == "Europe"
        and area > 150000
        and "EUR" not in currencies
        and population > 0
    ):
        filtered_countries.append(
            {
                "name": country.get("name", {}).get("common", "Unknown"),
                "capital": country.get("capital", ["Unknown"])[0],
                "area": area,
                "population": population,
                "currency": list(currencies.keys())[0] if currencies else "Unknown",
                "flag_url": country.get("flags", {}).get("png", ""),
            }
        )

# Вычисление плотности населения и добавление в данные
for country in filtered_countries:
    country["density"] = country["population"] / country["area"]

# Сортировка по плотности населения
sorted_countries = sorted(filtered_countries, key=lambda x: x["density"], reverse=True)

# Сохранение данных в файл results.json
with open("results.json", "w", encoding="utf-8") as file:
    json.dump(filtered_countries, file, ensure_ascii=False, indent=4)

# Вывод топ-3 стран по плотности населения
top_3_countries = sorted_countries[:3]
print("Топ-3 страны по плотности населения:")
for country in top_3_countries:
    print(country["name"])

# Сохранение флагов топ-3 стран
for country in top_3_countries:
    flag_url = country["flag_url"]
    if flag_url:
        flag_response = requests.get(flag_url)
        flag_response.raise_for_status()
        flag_filename = f"{country['name']}_flag.png"
        with open(flag_filename, "wb") as flag_file:
            flag_file.write(flag_response.content)
        print(f"Флаг сохранён: {flag_filename}")
