import requests
import json
import sys


def poluchit_data():
    try:
        otvet = requests.get("https://api.frankfurter.dev/v1/latest?base=USD")
    except requests.exceptions.RequestException:
        print("Нет связи с сервером")
        return None
    if otvet.status_code!= 200:
        print("Код ошибки: ", otvet.status_code)
        return None
    return otvet.json()

def sohranit(dannye):
    with open("kursy.json", "w", encoding="utf-8" ) as f: 
        json.dump(dannye, f, ensure_ascii=False, indent=2)
    print("Базовая валюта:", dannye["base"])
    print("Дата:", dannye["date"])
    print("Курс евро на дату:", dannye["rates"]["EUR"])

def main():
    dannye = poluchit_data()
    if dannye is None:
        sys.exit(1)
    sohranit(dannye)

if __name__ == "__main__":
    main()
