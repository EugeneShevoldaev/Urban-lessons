my_dict={'Николай II': 1868,'Александр III':1845,'Александр II':1818} #  Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение

print('1. Dict: ',my_dict,'\n') #  Выведите на экран словарь
print('2. Выбор по существующему значению: ',my_dict['Николай II'],'\n') # Выведите на экран одно значение по существующему ключу
print('3. Выбор по Не существующему значению: ',"'Andrey' ",my_dict.get('Andrey','- ключ не найден'),'\n') # одно по отсутствующему из словаря my_dict без ошибки

my_dict.update({'Александр Невский':1221,'Юрий Долгорукий':1099}) # Добавьте ещё две произвольные пары того же формата в словарь

print('4. Добавлено две пары: ','Александр Невский, Юрий Долгорукий','\n')
print('5. ',my_dict,'\n')
print('6. ОДна пара удалена - "Николай II"','\n')
print('7. Вывод значения удаленной пары: ',my_dict.pop('Николай II'),'\n') # Удалите одну из пар в словаре по существующему ключу из словаря


my_set={0, 4, 8, 'cat', 'dog', 4, 4, 10, 9, 8,(3,2,7,2)} # Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
print('8. Вывод на экран My Set: ',my_set,'\n') # Выведите на экран множество my_set (должны отобразиться только уникальные значения).

(my_set.add(2)) # Добавьте 2 произвольных элемента в множество my_set, которых ещё нет
(my_set.add(5))

my_set.discard(4) # Удалите один любой элемент из множества
print('9. Вывод измененного множества: ',my_set) # Выведите на экран измененное множество