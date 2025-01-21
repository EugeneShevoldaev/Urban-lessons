from math import inf

first = 49
second = 7


def divide(first, second):
    if second == 0:
        return inf
    else:
        resolt = round(first / second, 2)
    return resolt


print(divide(first, second))
