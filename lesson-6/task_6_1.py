# Не используя библиотеки для парсинга, распарсить
# (получить определённые данные) файл логов web-сервера nginx_logs.txt
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание:
# - код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# - Вы не знате заранее насколько идентичен шаблон строк файла. Попробуйте оценить это.

with open('nginx_logs1.txt', encoding='utf-8') as f:
    def gen_data(file):
        for line in file:
            remote_addr, _, _, _, _, request_type, requested_resource, *other = line.replace('"', '').split()
            yield remote_addr, request_type, requested_resource

    result = []
    for el in gen_data(f):
        result.append(el)
    print(result)
