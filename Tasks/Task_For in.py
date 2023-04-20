# Создать функцию dict_to_list которая будет конвертировать словарь в список кортежей
# Функция должна принимать словарь а возвращать список кортежей,в каждом кортеже должны быть пары(key,value) из словарей
def dict_to_list(dict_to_convert):
    list_to_convert = []
    for k, v in dict_to_convert.items():
        # Если значение ключа целое число  о его нужно умножить на 2 перед добавлением в кортеж
        if type(v) == int:
            v *= 2
        list_to_convert.append((k, v))
    return list_to_convert


print(dict_to_list({'a': 30, 'b': True, 'c': 4}))
