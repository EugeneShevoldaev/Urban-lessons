# создание класса
class Hous:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    # определение размера как количество этажей
    def __len__(self):
        return self.number_of_floor

    # вывод количества этажей
    def __str__(self):
        return f' Название: {self.name}, количество этажей: {self.number_of_floor}'

   # сравнение количества этажей
    def __eq__(self, other):
       return  self.number_of_floor == other.number_of_floor

    # проверка меньше ли первое значение чем второе
    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor

    # проверка меньше или равено первое значение чем второе
    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor

    # проверяем больше ли первое значение чем второе
    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor
    # проверка больше или равно первое значение чем второе
    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor

    # проверка неравенства первого и второго значений
    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor

    # увеличение значения
    def __add__(self, value):
        if not  isinstance(value, int):
            print('значение должно быть целым числом')
        else:
            return Hous(self.name, self.number_of_floor + value)

    def __iadd__(self, value):
        if not isinstance(value, int):
            print('значение должно быть целым числом')
        else:
            self.number_of_floor += value
        return self

    def __radd__(self, value):
        if not isinstance(value, int):
            print('значение должно быть целым числом')
        else:
            self.number_of_floor += value
        return self

h1 = Hous('Жуковский', 10)
h2=Hous('Суворовский', 5)

print(h1)
print(h2)

print(h1 == h2)

print(h1 < h2) # __lt__

print(h1 <=h2) # __le__

print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 != h2) # __ne__

print(h1 + 15) # __add__

# __iadd__
h1 += 20
print(h1)

# __radd__
h1 += 20
print(h1)






