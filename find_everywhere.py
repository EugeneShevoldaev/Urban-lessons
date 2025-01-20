import string


class WordsFinder:
    def __init__(self, *file_names):
        # Принимаем неограниченное количество файлов и сохраняем их в атрибуте
        self.file_names = file_names

    def get_all_words(self):
        # Словарь для хранения слов из всех файлов
        all_words = {}

        # Перебираем все файлы
        for file_name in self.file_names:
            # Считываем содержимое файла
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()  # Приводим весь текст к нижнему регистру
                # Убираем пунктуацию
                text = text.translate(str.maketrans('', '', string.punctuation))
                # Разбиваем текст на слова
                words = text.split()
                # Сохраняем в словарь
                all_words[file_name] = words

        return all_words

    def find(self, word):
        # Получаем все слова с помощью get_all_words
        all_words = self.get_all_words()
        # Создаем словарь с позициями
        positions = {}

        # Перебираем файлы и их слова
        for file_name, words in all_words.items():
            try:
                # Ищем первое вхождение слова
                position = words.index(word.lower()) + 1  # Позиция с 1, а не с 0
                positions[file_name] = position
            except ValueError:
                # Если слово не найдено, пропускаем файл
                positions[file_name] = None

        return positions

    def count(self, word):
        # Получаем все слова с помощью get_all_words
        all_words = self.get_all_words()
        # Считаем количество вхождений
        counts = {}

        # Перебираем файлы и их слова
        for file_name, words in all_words.items():
            # Считаем количество вхождений слова
            count = words.count(word.lower())
            counts[file_name] = count

        return counts


# Создаем файл с тестовым содержимым
with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("""It's a text for task Найти везде,
Используйте его для самопроверки.
Успехов в решении задачи!
text text text""")

# Создаем объект WordsFinder
finder = WordsFinder('test_file.txt')

# Проверяем работу методов
print(finder.get_all_words())  # Смотрим все слова
print(finder.find('TEXT'))  # Ищем первое вхождение слова 'TEXT'
print(finder.count('teXT'))  # Считаем количество вхождений 'text'
