first = 69
second = 3


def divide(first, second):
    if second == 0:
        return 'ошибка, на ноль делить нельзя'
    resolt = round(first / second, 2)
    return resolt


print(divide(first, second))
