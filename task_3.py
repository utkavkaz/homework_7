"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker_1 = Position("Иван", "Иванов", "программист", 83000, 50000)
print(f"{worker_1.get_full_name()} - {worker_1.position}: доход с учетом премии составляет "
      f"{float(worker_1.get_total_income())} рублей")

worker_2 = Position("Петр", "Петров", "директор", 125000, 80000)
print(f"{worker_2.get_full_name()} - {worker_2.position}: доход с учетом премии составляет "
      f"{float(worker_2.get_total_income())} рублей")
