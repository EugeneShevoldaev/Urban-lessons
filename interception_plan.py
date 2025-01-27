def personal_sum(numbers):
    resolt = 0
    incorrect_data = 0
    for i in numbers:
        try:
            resolt += i
        except:
            incorrect_data += 1
    return resolt, incorrect_data


def calculate_average(numbers):
        if isinstance(numbers, int):
            print('не корректные данные')
            return
        if len(numbers) == 0:
            return ('не достаточно данных')
        try:
            resolt, incorrect_data = personal_sum(numbers)
        except TypeError:
            return ('не корректные данные')
        try:
        # print('среднее:', resolt / len(numbers)-incorrect_data)
            return resolt / len(numbers) - incorrect_data
        except ZeroDivisionError:
            return 0
        except TypeError:
            return ('не корректные данные')






print()

print('     calculate_average')
#print(calculate_average([42, 15, 36, 13]))

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип

print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3

print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция

print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать






