import random
class Animal:
    def __init__(self):
        self.live = True  # животное живо
        self.sound = None  # звук по умолчанию
        self._DEGREE_OF_DANGER = 0  # степень опасности по умолчанию
        self._cords = [0, 0, 0]  # координаты
        self.speed = 0  # оформляется при создании объекта

    def move(self, dx, dy, dz):
        new_dx = self._cords[0] + dx * self.speed
        new_dy = self._cords[1] + dy * self.speed
        new_dz = self._cords[2] + dz * self.speed
        if new_dz < 0:
            print("It's too deep, I can't dive :(")
            return
        else:
            self._cords = [new_dx, new_dy, new_dz]

    def get_cords(self):
        print(self._cords)

    def attack(self):
        if self._DEGREE_OF_DANGER == 0:
            # return ("This animal is not dangerous.")
            print(f"This animal is not dangerous. {self._DEGREE_OF_DANGER}")
        elif self._DEGREE_OF_DANGER == 3:
            # return ('This animal is somewhat dangerous.')
            print(f'This animal is somewhat dangerous. {self._DEGREE_OF_DANGER}')
        elif self._DEGREE_OF_DANGER == 8:
            # return ('Watch out! This animal is highly dangerous!')
            print(f'Watch out! This animal is highly dangerous! {self._DEGREE_OF_DANGER}')

    def speak(self):
        if self.sound == None:
            print('This animal is silent.')
        else:
            print(self.sound)
'''-------------------------------------------------------------------------------------------------'''
class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.beak = True
    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f'The {self.__class__.__name__} laid {eggs} eggs.')

'''-------------------------------------------------------------------------------------------------'''
class AquaticAnimal(Animal):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= dz * self.speed
        if self._cords[2] < 0:
            self.speed = self.speed / 2
            print('deep: ', self._cords[2], ' speed: ', self.speed)
        else:
            print('deep: ',self._cords[2], ' speed: ', self.speed)
'''-------------------------------------------------------------------------------------------------'''
class PoisonousAnimal(Animal):
    def __init__(self):
        super().__init__()
        self._DEGREE_OF_DANGER = 8
    def attack(self):
        super().attack()
'''-------------------------------------------------------------------------------------------------'''

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird, Animal):
    def __init__(self):
        super().__init__()
        self._DEGREE_OF_DANGER = 3  # Устанавливаем степень опасности утконоса на 3
        self.sound = ("Click-click-click")
    def speak(self):
        super().speak()
    def attack(self):
        super().attack()
    def lay_eggs(self):
        super().lay_eggs()
    def dive_in(self, dz):
        super().dive_in( dz)





