def custom_write(file_name, strings):
    # Открываем файл для записи с указанием кодировки
    with open(file_name, 'a', encoding='utf-8') as file:
        for string in strings:
            file.write(f'{string}\n')

    # Открываем файл для чтения с указанием кодировки
    with open(file_name, 'r', encoding='utf-8') as file:
        # Чтение всех строк в файл
        file_content = file.readlines()

        strings_positions = {}
        position = 0

        for line_number, line in enumerate(file_content, start=1):
            # Добавляем кортеж (номер строки, позиция начала) как ключ и саму строку как значение
            strings_positions[(line_number, position)] = line.strip()
            position += len(line)  # Обновляем позицию для следующей строки

    return strings_positions


# Данные для записи
strings_to_write = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

# Путь к файлу
file_name = 'sample.txt'

# Вызов функции и вывод результата
positions = custom_write(file_name, strings_to_write)

# Печать на консоль в нужном формате
for key, value in positions.items():
    print(f"{key}: {value}")
