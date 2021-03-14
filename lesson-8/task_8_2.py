# Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока
# nginx_logs.txt для получения информации вида: (<remote_addr>, <request_datetime>,
# <request_type>, <requested_resource>, <response_code>, <response_size>)
import re

with open('nginx_logs.txt', encoding='UTF-8') as f:
    for raw in f:
        RE_DATA = re.compile(r"^([0-9.:a-f]{7,}).{6}([\d]{2}\/[A-Za-z]{3}\/[\d:\s+]{19}).{3}"
                             r"([A-Z]{3,}).([\/a-z_\d]+).{11}([\d]{3}).([\d]+)")
        parsed_raw = RE_DATA.findall(raw)[0]
        print(parsed_raw)
