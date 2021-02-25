duration = int(input("Введите количество секунд: "))
while duration < 0:
    duration = int(input('Число неверно. Введите положительное число: '))
if duration == 0:
    print('0 сек')
    exit(0)

reduction = duration % 31536000 % 2629744 % 86400
list_time = [duration // 31536000, 'гг', duration % 31536000 // 2629744, 'мес', duration % 31536000 % 2629744 // 86400,
             'дн', reduction // 3600, 'час', reduction % 3600 // 60, 'мин', reduction % 3600 % 60, 'сек']

excess = 0
while isinstance(list_time[excess], str) or not list_time[excess] != 0:
    del list_time[excess]

print(*list_time)