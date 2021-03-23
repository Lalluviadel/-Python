# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.

# Методичка (дополнение):Следующий шаг — реализовать перегрузку метода __str__()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:

    def __init__(self, list_l):
        self.list_l = list_l
        self.checkout()

    def checkout(self):
        try:
            for i in self.list_l:
                if not len(i) == len(self.list_l[0]):
                    msg = "Неверные исходные данные: длина одной из строк матрицы отличается от остальных"
                    raise ValueError(msg)
        except TypeError:
            print("Ошибка в значении атрибута экземпляра.\nДля формирования матрицы требуется список списков.")
            exit(1)

    def __str__(self):
        fine_view = ''
        for i in self.list_l:
            fine_view += f"{i}\n"
        return fine_view

    def __add__(self, other):
        if len(self.list_l) == len(other.list_l) and len(self.list_l[0]) == len(other.list_l[0]):
            sum_matrix = [[num_1 + num_2 for num_1, num_2 in zip(row_1, row_2)]
                          for row_1, row_2 in zip(self.list_l, other.list_l)]
            return sum_matrix
        else:
            msg = "Матрицы должны быть одинакового размера"
            raise ValueError(msg)


if __name__ == "__main__":
    '''
    Матрицы для испытаний
    a = Matrix([0, 1])
    a = Matrix ([[3, 4, 6], [3, 4], [5, 5]])
    a = Matrix(9)
    a = Matrix([[0], [1], [2]])
    b = Matrix([[1, 3], [1, 3]])
    '''
    a = Matrix([[0, 3], [1, 4], [2, 5]])
    print(a)
    b = Matrix([[0, 3], [1, 4], [2, 5]])
    print(b)
    c = Matrix(a + b)
    print(c)
