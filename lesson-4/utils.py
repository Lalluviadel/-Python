from requests import get, utils
from decimal import Decimal
from datetime import datetime


def currency_rates(currency_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    start_search = content.find('<Value>', content.find(currency_code.upper()))
    result = content[start_search+7:content.find('</Value>', start_search)]
    nominal_get = content[content.find(currency_code.upper())+23:
                          content.find('</Nominal>', content.find(currency_code.upper()))]
    date_resp = datetime.strptime((content[content.find('Date') + 6:
                                           content.find('Date') + 16]), '%d.%m.%Y').date()
    if result == content[6:-1] or nominal_get == content[23:-1]:
        return None
    else:
        nominal_1_cur = Decimal(result.replace(',', '.')) / int(nominal_get)
        return f"курс {currency_code.upper()} {nominal_1_cur} на дату {date_resp}"


if __name__ == '__main__':
    print(f"Доллар: {currency_rates('USD')}")
    print(f"Евро: {currency_rates('eur')}")
    print(f"Молдавский лей: {currency_rates('mdl')}")
    print(f"Несуществующая валюта: {currency_rates('ывыа')}")
