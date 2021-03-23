# Реализовать проект расчёта суммарного расхода ткани на производство
# одежды. Основная сущность (класс) этого проекта — одежда, которая может
# иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
#
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
#
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания.
#
# Реализовать абстрактные классы для основных классов проекта
# и проверить работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    cons_counter = 0

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def cons_new_product(self):
        raise NotImplementedError

    @staticmethod
    def calculate_cons(cons_unit):
        Clothes.cons_counter += cons_unit
        return Clothes.cons_counter


class Coat(Clothes):
    def __init__(self, size, title):
        super().__init__(title)
        self.size = size
        self.calculate_cons(self.cons_new_product)

    @property
    def cons_new_product(self):
        result = round((self.size / 6.5 + 0.5), 1)
        return result

    def __str__(self):
        return f"\nРасход ткани на {self.title} размера {self.size}: {self.cons_new_product} м"


class Suit(Clothes):

    def __init__(self, height, title):
        super().__init__(title)
        self.height = height
        self.calculate_cons(self.cons_new_product)

    @property
    def cons_new_product(self):
        result = round((2*self.height + 0.3), 1)
        return result

    def __str__(self):
        return f"\nРасход ткани на {self.title} при росте {self.height}: {self.cons_new_product} м"


if __name__ == "__main__":

    item_1 = Coat(21, 'Пальто-кромби')
    item_2 = Coat(15, 'Пальто-кокон')
    item_3 = Suit(1.85, 'Фрачный костюм')
    item_4 = Suit(1.67, 'Костюм-двойка')
    print(item_1, item_4)
    print(f"Общий расход ткани на все изделия: {Clothes.cons_counter} м")
