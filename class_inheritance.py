class Animal:  # родительский класс для животных
    def __init__(self):
        self.alive = True  # живой
        self.name = ""
        self.fed = False  # не накормлен

    def eat(self, food):
        if food.edible == False:
            print(f'{self.name} не стал есть {food.plant_name}')
            self.alive = False
            self.fed = False
        else:
            print(f'{self.name} съел {food.plant_name}')
            self.fed = True
            self.alive = False


class Mammal(Animal):  # дочерние классы животных
    def __init__(self):
        super().__init__()  # super используется чтобы не копировать код из родительского класса
        self.name = 'Hatiko'


class Predator(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Волк с Уолл-Стрит'


class Plant:  # родительский класс для растений
    def __init__(self):
        self.edible = False  # не съедобный
        self.plant_name = ""


class Flower(Plant):
    def __init__(self):
        super().__init__()
        self.plant_name = "Цветик семицветик"


class Fruit:
    def __init__(self):
        super().__init__()
        self.plant_name = "Заводной апельсин"
        self.edible = True


a1 = Predator()  # волк
a2 = Mammal()  # Хатико
p2 = Fruit()  # апельсин
p1 = Flower()  # цветок

print(a1.name)
print(p1.plant_name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)


