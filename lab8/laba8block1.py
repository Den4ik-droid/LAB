import requests
import json


BASE_URL = "https://restcountries.com/v3.1"
ALL_COUNTRIES_ENDPOINT = f"{BASE_URL}/all"

response = requests.get(ALL_COUNTRIES_ENDPOINT)
response.raise_for_status()
all_countries = response.json()


filtered_countries = []
for country in all_countries:
    region = country.get("region", "")
    area = country.get("area", 0)
    currencies = country.get("currencies", {})
    population = country.get("population", 0)

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


for country in filtered_countries:
    country["density"] = country["population"] / country["area"]


sorted_countries = sorted(filtered_countries, key=lambda x: x["density"], reverse=True)


with open("results.json", "w", encoding="utf-8") as file:
    json.dump(filtered_countries, file, ensure_ascii=False, indent=4)


top_3_countries = sorted_countries[:3]
print("Топ-3 страны по плотности населения:")
for country in top_3_countries:
    print(country["name"])


for country in top_3_countries:
    flag_url = country["flag_url"]
    if flag_url:
        flag_response = requests.get(flag_url)
        flag_response.raise_for_status()
        flag_filename = f"{country['name']}_flag.png"
        with open(flag_filename, "wb") as flag_file:
            flag_file.write(flag_response.content)
        print(f"Флаг сохранён: {flag_filename}")
