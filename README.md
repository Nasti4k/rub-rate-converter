# Rub rate converter

Консольный конвертер валют с актуальными курсами Центрального банка РФ.

## Возможности

- Загрузка курсов валют с API ЦБ РФ ([cbr-xml-daily.ru](https://www.cbr-xml-daily.ru/))
- Конвертация **рубль → валюта** и **валюта → рубль**
- Учёт номинала валюты (например, для JPY)
- Обработка ошибок сети и некорректного ввода

## Требования

- Python 3.10+
- [requests](https://pypi.org/project/requests/)

Для тестов:

- [pytest](https://pypi.org/project/pytest/)
- [responses](https://pypi.org/project/responses/)

## Установка

```bash
git clone https://github.com/Nasti4k/rub-rate-converter.git
cd rub-rate-converter

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install requests pytest responses
```

## Использование

```bash
python main.py
```

Пример сессии:

```
Доступные валюты: AUD, AZN, GBP, AMD, BYN, BGN, BRL, HUF, VND, HKD, GEL, DKK, AED, USD, EUR, EGP, INR, IDR, KZT, CAD, QAR, KGS, CNY, MDL, NZD, NOK, PLN, RON, XDR, SGD, TJS, THB, TRY, TMT, UZS, UAH, CZK, SEK, CHF, RSD, ZAR, KRW, JPY
Введите код валюты: USD
1: RUB -> USD
2: USD -> RUB
2
Сумма: 100
Результат: 8650.00
```

## Как это работает

1. `fetch_rates()` — запрашивает JSON с курсами и возвращает словарь валют.
2. Пользователь выбирает код валюты и направление конвертации.
3. `convert()` — пересчитывает сумму с учётом курса и номинала:
   - валюта → RUB: `amount * rate`
   - RUB → валюта: `amount / rate`

## Тесты

```bash
pytest
```

Покрытие:

| Файл | Что проверяет |
|------|----------------|
| `tests/test_convert.py` | Конвертация в обе стороны, нулевая сумма, round-trip |
| `tests/test_fetch_rates.py` | Успешный ответ API, ошибка сервера, таймаут |

## Структура проекта

```
currency-conversion/
├── main.py                 
├── conftest.py             
├── tests/
│   ├── test_convert.py
│   └── test_fetch_rates.py
└── README.md
```

## Лицензия

MIT
```