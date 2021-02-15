"""
    Задача 2 повышенной сложности:
Измените существующий список, и добавьте элементы-кавычки.
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Вывести список и строку на экран. Обратите внимание на отсутствие "лишних" пробелов около кавычек.
"""

weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(id(weather_list))  # для самопроверки, что список тот же

for inx, member in enumerate(weather_list):
    if member.isdigit():
        weather_list[inx] = f'{int(member):02d}'
        weather_list.insert(inx + 1, '"', )
    elif member[1:].isdigit():
        weather_list[inx] = f'{member[0]}{int(member[1:]):02d}'
        weather_list.insert(inx + 1, '"', )
print(id(weather_list))  # для самопроверки, что список тот же
weather_list.reverse()

for inx, member in enumerate(weather_list):
    if member.isdigit() or member[1:].isdigit():
        weather_list.insert(inx + 1, '"', )
weather_list.reverse()

print(id(weather_list))  # для самопроверки, что список тот же
print(weather_list)

str_tmp = ' '.join(weather_list)
str_new = ''
for inx, symbol in enumerate(str_tmp):
    if symbol == ' ' and (str_tmp[inx+1].isdigit() or str_tmp[inx+1] == '+' or str_tmp[inx+1] == '-'):
        str_new = str_new + ''
    elif symbol == ' ' and str_tmp[inx-1].isdigit():
        str_new = str_new + ''
    else:
        str_new = str_new + symbol
print(str_new)
