import pickle

def display_cities_and_avg_temp(city_data):
    print("\nСписок городов и средней температуры:")
    for city, temps in city_data.items():
        avg_temp = sum(temps.values()) / len(temps)
        print(f"{city}: {avg_temp:.1f}°C")

def find_max_temp_year(city_data):
    print("\nГоды с максимальной средней температурой:")
    for city, temps in city_data.items():
        max_year = max(temps, key=temps.get)
        print(f"{city}: {max_year} ({temps[max_year]}°C)")

def find_cities_cold_in_2019(city_data):
    cold_2019_cities = [city for city, temps in city_data.items() if min(temps, key=temps.get) == "2019"]
    print("\nГорода, где 2019 был самым холодным годом:")
    print(", ".join(cold_2019_cities))

def find_cities_hot_in_2017(city_data):
    hot_2017_cities = [
        city
        for city, temps in city_data.items()
        if temps["2017"] - temps["2018"] > 1
    ]
    print("\nГорода, где температура 2017 года превосходила 2018 более чем на 1°С:")
    print(", ".join(hot_2017_cities))

def save_data_to_file(city_data, filename):
    with open(filename, "wb") as f:
        pickle.dump(city_data, f)
    print(f"\nДанные сохранены в файл {filename}.")

def load_data_from_file(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

city_data = {
    "Moscow": {"2017": 5.2, "2018": 6.0, "2019": 4.8, "2020": 5.9, "2021": 6.1, "2022": 5.7},
    "New York": {"2017": 12.3, "2018": 12.5, "2019": 11.9, "2020": 12.1, "2021": 12.8, "2022": 12.4},
    "Tokyo": {"2017": 16.8, "2018": 16.9, "2019": 16.7, "2020": 17.0, "2021": 17.2, "2022": 16.8},
    "Berlin": {"2017": 9.3, "2018": 9.8, "2019": 9.1, "2020": 9.5, "2021": 9.7, "2022": 9.4},
    "Paris": {"2017": 11.7, "2018": 12.0, "2019": 11.3, "2020": 11.8, "2021": 12.2, "2022": 11.9},
    "Sydney": {"2017": 18.5, "2018": 18.7, "2019": 18.3, "2020": 18.6, "2021": 18.9, "2022": 18.4},
    "Cairo": {"2017": 21.3, "2018": 21.5, "2019": 21.0, "2020": 21.4, "2021": 21.8, "2022": 21.6},
}

display_cities_and_avg_temp(city_data)
find_max_temp_year(city_data)
find_cities_cold_in_2019(city_data)
find_cities_hot_in_2017(city_data)
save_data_to_file(city_data, "data.pickle")

loaded_data = load_data_from_file("data.pickle")
print("\nДанные, прочитанные из файла data.pickle:")
print(loaded_data)





