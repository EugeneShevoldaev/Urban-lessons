import os
import time

# Указываем директорию (по умолчанию текущая папка)
directory = "."

# Обход всех каталогов и файлов
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию
        parent_dir = os.path.dirname(filepath)

        # Вывод информации о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')