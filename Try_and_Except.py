def add_everything_up(var1, var2):
    try:
       return var1 + var2
    except Exception as exc:
        return (f'данные разных типов не складываются   {var1} {var2}  ошибка: {exc}')




print(add_everything_up('123', '321' ))
print(add_everything_up(123, 321 ))
print(add_everything_up(123, '321' ))