"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, params):
        self.params = params


    @abstractmethod
    def consumption(self):
        pass

    def __str__(self):
        return str(self.params)

class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.params / 6.5 + 0.5, 2)


class Suit(Clothes):

    @property
    def consumption(self):
        return round(self.params * 2 + 0.3, 2)


C = Coat(51)
S = Suit(1.82)

print(f'Расход ткани на пальто: \n {C.consumption}')
print(f'Расход ткани на костюм: \n {S.consumption}')
print(f'Общий расход ткани: \n {C.consumption + S.consumption}')
