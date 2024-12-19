import requests
from bs4 import BeautifulSoup
import csv


BASE_URL = "https://worldathletics.org/records/toplists"
DISCIPLINES = {
    "SP": "shot-put",
    "DT": "discus-throw",
    "JT": "javelin-throw",
    "HT": "hammer-throw",
}
GENDERS = {"M": "men", "W": "women"}
YEARS = range(2001, 2025)


def scrape_page(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.select(".toplists-table tbody tr")
    if not rows:
        return None

    top_result = rows[0]
    columns = top_result.find_all("td")
    if len(columns) < 5:
        return None

    name = columns[1].text.strip()
    country = columns[2].find("span", class_="country-flag").text.strip()
    result = columns[3].text.strip()
    date = columns[4].text.strip()

    return {
        "name": name,
        "country": country,
        "result": result,
        "date": date,
    }


results = []
for year in YEARS:
    for gender, gender_name in GENDERS.items():
        for discipline_code, discipline_name in DISCIPLINES.items():
            url = f"{BASE_URL}/{discipline_name}/{gender_name}/{year}"
            print(f"Собираем данные с {url}")
            data = scrape_page(url)
            if data:
                results.append(
                    {
                        "year": year,
                        "gender": gender,
                        "discipline": discipline_name,
                        **data,
                    }
                )

with open("top_results.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["year", "gender", "discipline", "name", "country", "result", "date"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print("Сбор данных завершён. Результаты сохранены в top_results.csv.")
