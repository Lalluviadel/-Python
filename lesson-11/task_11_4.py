# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создайте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, list_parts):
        self.list_parts = list_parts

    def __str__(self):
        if self.list_parts[0] == 0:
            result = f"{self.list_parts[1]}i"  # мнимые числа
        elif self.list_parts[1] == 0:
            result = f"{self.list_parts[0]}"  # действительные числа
        else:
            result = f"{self.list_parts[0]}{self.list_parts[1]:+g}i"
        return result

    def __add__(self, other):
        result = [x + y for x, y in zip(self.list_parts, other.list_parts)]
        result_num = Complex(result)
        return result_num

    def __mul__(self, other):
        # (3+2i)(2-4i) = 3*2 + 2i*2 -4i*3 -4i*2i = 6 + 4i - 12i - 8*-1 = 14-8i
        tmp_list = [x*y for x in self.list_parts for y in other.list_parts]
        result = [tmp_list[0]-tmp_list[3], tmp_list[1]+tmp_list[2]]
        result_num = Complex(result)
        return result_num


a = Complex([3, 2])
print(a)
b = Complex([2, -4])
print(b)
c = a+b
print(c)
v = a*b
print(v)
