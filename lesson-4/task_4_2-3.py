from requests import get, utils
from decimal import Decimal
from datetime import datetime


def currency_rates(currency_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    date_resp = datetime.strptime((content[content.find('Date') + 6:
                                  content.find('Date') + 16]), '%d.%m.%Y').date()
    start_search = content.find('<Value>', content.find(currency_code.upper()))
    result = content[start_search+7:content.find('</Value>', start_search)]
    if result == content[6:-1]:
        return None
    else:
        return f"курс {currency_code.upper()} {Decimal(result.replace(',', '.'))} на дату {date_resp}"


print(f"Доллар: {currency_rates('USD')}")
print(f"Евро: {currency_rates('EUR')}")
print(currency_rates(input("Введите трехзначный код требуемой валюты: ")))
