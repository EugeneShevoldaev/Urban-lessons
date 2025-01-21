def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a = 1, b = 25, c = [1, 2, 3])

value_list = ['Привет', 123, 9.99]
value_dict = {'a': 'Привет', 'b': 42, 'c': 3.14}

print_params(*value_list)
print_params(**value_dict)

value_list_2 = ['New Year', 2025]
print_params(*value_list_2, 42)
