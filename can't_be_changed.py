class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_owner(self):
        print(f'владелец: {self.owner}')

    def get_model(self):
        print(f'модель: {self.__model}')

    def get_horsepower(self):
        print(f'мощность: {self.__engine_power}')

    def get_color(self):
        print(f'цвет: {self.__color}')

    def print_info(self):
        print(f'владелец: {self.owner}')
        print(f'модель: {self.__model}')
        print(f'мощность: {self.__engine_power}')
        print(f'цвет: {self.__color}')

    def set_color(self, new_color):
            if new_color.lower() in Vehicle.__COLOR_VARIANTS:
                self.__color = new_color
                print(f'цвет изменен на {new_color}')
            else:
                print(f'изменить цвет на {new_color} не возможно, выберите '
                  f'другой цвет')
    def set_owner(self, new_owner):
        self.owner = new_owner
        print(f'новый владелец: {self.owner}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, owner, model, engin_power, color):
        super().__init__(owner, model, engin_power, color)




vehicle = Vehicle('Kolya', 'Solaris', 112, 'White')
# vehicle.print_info()
# vehicle.get_color()
# vehicle.set_color()
# vehicle.get_color()


print('')

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'Blue')
vehicle1.print_info()

vehicle1.set_color('Pink') # смена цвета не удачная
vehicle1.set_color('Black')# смена цвета удачная
vehicle1.get_owner() # владелец
vehicle1.set_owner('Vasyok') # смена владельца









