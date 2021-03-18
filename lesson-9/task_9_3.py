# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};

# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        sum_inc = 0
        for inx in self._income:
            sum_inc = sum_inc + int(self._income[inx])
        return sum_inc


person_1 = Position('Алексей', 'Пажитнов', 'Senior Game Designer', {"wage": 100, "bonus": 40})
person_2 = Position('Джордан', 'Мекнер', 'Game Writer', {"wage": 90, "bonus": 30})
person_3 = Position('Говард', 'Тодд', 'Executive Producer', {"wage": 100, "bonus": 45})

if __name__ == "__main__":
    department_list = [person_1, person_2, person_3]
    for i in department_list:
        print(f"Имя сотрудника: {i.get_full_name()}, должность: {i.position}, полный доход: {i.get_total_income()}")
