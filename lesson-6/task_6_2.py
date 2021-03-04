# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания. Спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Примечание:
# - Уверены ли вы, что максимальное кол-во запросов - уникально?
# Т.е. найденный спамер - только один? Или таких спамеров может быть несколько?
def sort_ip(some_gen):
    set_all_ip = set()
    dict_repeated = {}
    for el in some_gen:
        ip = el[0]
        if ip in dict_repeated:
            dict_repeated[ip] += 1
        elif ip in set_all_ip:
            dict_repeated[ip] = 2
        else:
            set_all_ip.add(ip)
    return find_spam(dict_repeated)


def find_spam(some_dict):
    list_spam = []
    max_spam_value = max(some_dict.values())
    for key, value in some_dict.items():
        if value == max_spam_value:
            list_spam.append((key, value))
    return list_spam


with open('nginx_logs.txt', encoding='utf-8') as f:
    def gen_data(file):
        for line in file:
            remote_addr, _, _, _, _, request_type, requested_resource, *other = line.replace('"', '').split()
            yield remote_addr, request_type, requested_resource

    request_data = gen_data(f)
    spam_ip = sort_ip(request_data)
    print(spam_ip)
