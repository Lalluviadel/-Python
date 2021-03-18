# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police(булево).

# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;

# добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля;

# для классов TownCar и WorkCar переопределите метод show_speed.

# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    is_police = False
    speed = 0

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def show_speed(self):
        if self.speed > 0:
            print(f"{self.color} {self.name} движется со скоростью {self.speed} км/ч")
        else:
            print(f"{self.color} {self.name} стоит на месте")

    def go(self, speed):
        self.speed = speed
        print(f"{self.color} {self.name} разгоняется")
        self.show_speed()

    def stop(self):
        m = self.speed
        self.speed = 0
        print(f"{self.color} {self.name} останавливается.  \n")
        if m > 60 and not self.is_police:
            print(f"Полицейский наконец нагнал {self.name} и штрафует его. \n")
        elif self.is_police:
            print(f"{self.name} продолжает патрулирование. \n")

    def turn(self, direction):
        print(f"{self.color} {self.name} поворачивает {direction}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} мчится со скоростью {self.speed} км/ч"
                  f" и превышает допустимую на {self.speed - 60} км/ч.\n"
                  f"Это замечает полицейский, включается мигалка, полицейский"
                  f" преследует {self.name}")
        elif self.speed == 0:
            print(f"{self.color} {self.name} стоит на месте")
        else:
            print(f"{self.color} {self.name} движется со скоростью {self.speed} км/ч")


class SportCar(Car):
    unique_charact = 'мощный двигатель'

    def go(self, speed):
        x = 2.5
        self.speed = int(speed*x)
        print(f"{self.color} {self.name} разгоняется в {x} раз быстрее: у него {self.unique_charact}")
        self.show_speed()


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} мчится со скоростью {self.speed} км/ч"
                  f" и превышает допустимую на {self.speed - 40} км/ч.\n"
                  f"Это замечает полицейский, включается мигалка, полицейский"
                  f" преследует {self.name}")
        elif self.speed == 0:
            print(f"{self.color} {self.name} стоит на месте")
        else:
            print(f"{self.color} {self.name} движется со скоростью {self.speed} км/ч")


class PoliceCar(Car):
    is_police = True


def check_out_car(car, user_speed):
    if car.is_police:
        print(f"{car.name} - полицейская машина")
    car.show_speed()
    car.go(user_speed)
    car.turn('направо')
    car.stop()


car_1 = TownCar('красная', 'Mazda 6')
car_2 = SportCar('оранжевый', 'McLaren 675LT')
car_3 = WorkCar('желтый', 'Caterpillar Cat 986k')
car_4 = PoliceCar('белый', 'Ford Focus 2')

if __name__ == "__main__":
    check_out_car(car_1, 80)
    check_out_car(car_2, 50)
    check_out_car(car_3, 40)
    check_out_car(car_4, 40)
