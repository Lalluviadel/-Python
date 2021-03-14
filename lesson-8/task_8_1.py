# Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает
# их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.

import re


def email_parse(email_address):
    match = re.findall(r"([\w'.+-]+)@([\w'.-]+\.[\w'.-]+)", email_address, re.ASCII)
    msg = f"wrong email: {email_address}"
    if not match:
        raise ValueError(msg)
    else:
        yield match[0][0], match[0][1]


# user_address = 'someone@geekbrainsru'
user_address = 'someone@@geekbrains.ru'
# user_address = 'some1-one@geek.brains.ru'

dict_userdata = {}
for item in email_parse(user_address):
    dict_userdata.update(username=item[0], domain=item[1])
print(dict_userdata)
