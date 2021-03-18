# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'Пока не кончились чернила, {self.title} будет писать')


class Pencil(Stationery):
    def draw(self):
        print(f'Если {self.title} хорошо заточен, можно рисовать')


class Handle(Stationery):
    def draw(self):
        print(f'Если {self.title} не высох, можно провести линию')


item_1 = Stationery('тушь')
item_2 = Pen('шариковая ручка')
item_3 = Pencil('акварельный карандаш')
item_4 = Handle('текстовыделитель')

if __name__ == "__main__":
    tools = (item_1, item_2, item_3, item_4)
    for item in tools:
        item.draw()
