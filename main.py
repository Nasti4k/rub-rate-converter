import requests

API_URL = "https://www.cbr-xml-daily.ru/daily_json.js"

def fetch_rates(url: str = API_URL, timeout: int = 10) -> dict:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()["Valute"]

def convert(amount: float, rate: float, to_rub: bool) -> float:
    return amount * rate if to_rub else amount / rate

def main():
    try:
        rates = fetch_rates()
    except requests.RequestException as e:
        print(f"Не удалось получить курс: {e}")
        return

    print("Доступные валюты:", ", ".join(rates))
    code = input("Введите код валюты: ").strip().upper()

    if code not in rates:
        print("Такой валюты нет")
        return

    rate = rates[code]["Value"] / rates[code]["Nominal"]
    direction = input(f"1: RUB -> {code}\n2: {code} -> RUB\n")

    try:
        amount = float(input("Сумма: "))
    except ValueError:
        print("Нужно число")
        return

    to_rub = direction == "2"
    result = convert(amount, rate, to_rub)
    print(f"Результат: {result:.2f}")

if __name__ == "__main__":
    main()