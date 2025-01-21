class Hous:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
    def __del__(self):
        print(f'дом {self.name} снесен но он останется в истории')


h1 = Hous('ЖК Эльбрус', 10)
print(Hous.houses_history)
h2 = Hous('ЖК Акация', 20)
print(Hous.houses_history)
h3 = Hous('ЖК Матрёшки', 20)
print(Hous.houses_history)

# Удаление объектов

del h2
del h3
print(Hous.houses_history)




