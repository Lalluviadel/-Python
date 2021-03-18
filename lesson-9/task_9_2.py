# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия
# одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    standard_unit_weight = 25

    def __init__(self, lenght, wight):
        self._length = lenght
        self._width = wight

    def mass_calculation(self, thickness=5):
        m = (self._length * self._width * self.standard_unit_weight * thickness)/1000
        print(f"Для строительства дороги с параметрами:\n "
              f"-длина {self._length} м,\n -ширина {self._width} м,\n "
              f"-толщина полотна {thickness} см\nпотребуется {m} тонн асфальта")


if __name__ == "__main__":
    new_road = Road(5000, 20)
    new_road.mass_calculation(4)
