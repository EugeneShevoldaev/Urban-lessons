import random

number = random.randint(3, 20)  # получаем случайное число в заданном диапазоне
password = []  # создаем пустой список

for i in range(1, 20):  # перебор всех значений для подбора шифра
    for j in range(1, 20):
        if number % (i + j) == 0:
            pas = (i, j)
            revers_pas = (j, i)
            if pas not in password and revers_pas not in password:
                password.append(pas)



print('cod: ', number)  # вывод на печать полученного рандомно значения кода
print('пароль: ', *password)  # вывод на печать полученного пароля
