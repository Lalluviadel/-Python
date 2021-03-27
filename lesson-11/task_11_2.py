# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    a = input('Введите число: ')
    b = input('Введите второе число: ')
    try:
        a, b = float(a), float(b)
        if b == 0:
            raise MyException("Делить на ноль нельзя, если это не высшая математика!")
    except MyException as e:
        print(e)
    except ValueError as e:
        print(e, "Введено не число")
    else:
        c = a / b
        print(f"Результат деления: {c}")
        exit()
