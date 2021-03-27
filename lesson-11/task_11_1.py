# Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год».

# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12).

# Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, date_str):
        tmp_data = self.get_elements(date_str)
        self.checkout(tmp_data)
        self.date_str = tmp_data

    @classmethod
    def get_elements(cls, date_str):
        try:
            result = [int(i) for i in date_str.split('-')]
            return result
        except (ValueError, AttributeError) as e:
            print(e, "Дата должна быть в виде строки формата «день-месяц-год», "
                  "\nгде день, месяц и год - положительные целые числа")
            exit(1)

    @staticmethod
    def checkout(list_num):
        msg = "Ошибочное значение дня, месяца или года"
        check_condition = [list_num[0] in range(1, 32), list_num[1] in range(1, 13),
                           list_num[2] > 0]
        if not all(check_condition):
            raise ValueError(msg)


if __name__ == "__main__":
    ''' Даты для испытаний
        a = Date('ff-12-2000')
        a = Date('144-12-2001')
        a = Date('-1-12-2000')
        a = Date('е1-12-2000')  
    '''

    a = Date('14-12-2001')
    print(a.date_str)
