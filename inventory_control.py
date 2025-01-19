from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return self.name, self.weight, self.category


class Shop:
    def __init__(self):
        self.__file_name = 'product.txt'

    def get_product(self):# метод открывает файл для чтения
        with open(self.__file_name, 'r') as file:
            print(file.read())# выводит имеющиеся записи в консоль
            return

    def add_product(self):
        name = input('наименование продукта: ')# метод запрашивает наименование продукта
        name_product = name
        with open(self.__file_name, 'r') as file:
            for line in file:
                if name_product == line.split(',')[0]:
                    print(f'такой продукт {name_product} уже существует')# если такой продукт найден - сообщает об этом
                    return
            weight = input('вес продукта: ')# если не найден то запрашивает остальные аргументы
            category = input('категория продукта:')
            with open(self.__file_name, 'a') as file:
                file.write(f'{name_product}, {weight}, {category}\n')# производит запись в файл и сообщает об этом
                print(f'продукт {name_product} успешно добавлен')

    def add(self, *products):# метод принимает любое количество продуктов
        for product in products:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    if product.name == line.split(',')[0]:# проверяет наличие записи в файле
                        print(f'продукт {product.name} уже существует, не добавлен')# сообщает о результате проверки
                        return
                else:
                    with open(self.__file_name, 'a') as file:# если запись не найдена добавляет продукты в файл
                        file.write(f'{product.name}, {product.weight}, {product.category}')
                        print(f'продукт {product.name} успешно добавлен')

if __name__ == '__main__':
      s1 = Shop()
      p1 = Product('Potato', 50.5, 'Vegetables\n')
      p2 = Product('Spaghetti', 3.4, 'Groceries\n')
      p3 = Product('Potato', 5.5, 'Vegetables\n')
      # print([p2])
      s1.add(p1, p2, p3)
      s1.get_product()


#     shop = Shop()  # создаем объект класса
#     shop.get_product()
#     shop.add_product()  # вызываем метод для добавления продукта
#     shop.get_product()

