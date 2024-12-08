import random


def generate_unique_password(number):
    password = set()

    for i in range(1, 20):
        for j in range(1, 20):
            if number % (i + j) == 0 and i <= j:
                password.add((i, j))

    return list(password)


# Получаем случайное число в заданном диапазоне
number = random.randint(3, 20)

# Генерируем уникальный пароль
unique_password = generate_unique_password(number)

# Преобразуем результат в строку для вывода
password_str = ' '.join(f'{pair[0]} {pair[1]}' for pair in unique_password)

# Выводим результаты
print('Код:', number)
print('Уникальный пароль:', password_str)