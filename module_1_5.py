immutable_var=1,5,"cat", 'dog','8',3.14, True, ['apple', 1965]
print(immutable_var)
mutable_list=['apple',1,3,5,6.626,True]
print(mutable_list)
mutable_list[0]='sumsung'
mutable_list[5]='ложь'
print(mutable_list)

#значения элементов кортежа изменить нельзя тк это не изменяемые объекты, внутри кортежа можно лишь изменить
# изменяемые объекты если он таковые содержит