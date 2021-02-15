"""
    Задача 2 обычной сложности, 1 вариант:
Создайте новый список и заполните его нужными значениями,включая элементы-кавычки.
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Вывести список и строку на экран. Обратите внимание на отсутствие "лишних" пробелов около кавычек.
"""
weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for member in weather_list:
    if member.isdigit():
        new_list.extend(['"', f'{int(member):02d}', '"'])
    elif member[1:].isdigit():
        new_list.extend(['"', f'{member[0]}{int(member[1:]):02d}', '"'])
    else:
        new_list.append(member)
print(new_list)
str_tmp = ' '.join(new_list)
str_new = ''
for inx, symbol in enumerate(str_tmp):
    if symbol == ' ' and (str_tmp[inx+1].isdigit() or str_tmp[inx+1] == '+' or str_tmp[inx+1] == '-'):
        str_new = str_new + ''
    elif symbol == ' ' and str_tmp[inx-1].isdigit():
        str_new = str_new + ''
    else:
        str_new = str_new + symbol
print(str_new)
