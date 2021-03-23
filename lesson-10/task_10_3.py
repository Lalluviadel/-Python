# Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка».

# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).

# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__floordiv____truediv__()).
# Эти методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.
#
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если
# разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
#
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
#
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
# и количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.

class Cell:

    def __init__(self, num_section):
        self.num_section = num_section
        self.checkout()

    def checkout(self):
        msg = 'Количество ячеек клетки должно быть целым числом больше нуля'
        if isinstance(self.num_section, int) and self.num_section > 0:
            return
        raise TypeError(msg)

    def __add__(self, other):
        result = self.num_section + other.num_section
        return Cell(result)

    def __sub__(self, other):
        msg_1 = "Количество ячеек в 1 клетке меньше количества ячеек во 2"
        msg_2 = "Количества ячеек в клетках равны; создать клетку с 0 ячеек невозможно"
        result = self.num_section - other.num_section
        if result > 0:
            return Cell(result)
        elif result == 0:
            raise ValueError(msg_2)
        else:
            raise ValueError(msg_1)

    def __mul__(self, other):
        result = self.num_section * other.num_section
        return Cell(result)

    def __floordiv__(self, other):
        result = self.num_section//other.num_section
        return Cell(result)

    def __truediv__(self, other):
        return self.__floordiv__(other)

    def make_order(self, num_rows):
        tmp_row = [i+1 for i in range(self.num_section-1)]
        result = ''
        for i in range(0, len(tmp_row), num_rows):
            tmp_str = ''.join(map(str, tmp_row[i:i+num_rows]))
            result += tmp_str + '\n'
        return result


if __name__ == "__main__":
    '''
    Клетки для испытаний:
        item_1 = Cell('jj')
        new_item_1 = item_3 + item_2
        print(new_item_1.num_section)
        new_item_2 = item_2-item_3
        print(new_item_2.num_section)
        new_item_3 = item_2*item_3
        print(new_item_3.num_section)
        new_item_4 = item_2 / item_3
        print(new_item_4.num_section)   
    '''

    item_2 = Cell(19)
    item_3 = Cell(91)
    new_item_4 = item_3.make_order(8)
    print(new_item_4)
