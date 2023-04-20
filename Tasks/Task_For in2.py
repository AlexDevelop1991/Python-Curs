# Создать функцию filter_list которая будет фильтровать список
# У функции должны быть два параметра список и тип значение
# Функция должна вернуть новый список в котором остнануться значение только того типа
# который был передан в вызове функции вторым аргументом
def filter_list(list_to_filter, value_type):
    filtered_list = []
    for element in list_to_filter:
        if type(element) == value_type:
            filtered_list.append(element)
    return filtered_list

# Функцию можно вызвать например так: filter_list([35, True, 'abc', 10]) и получить [35,10]
print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))


# Можно так
def filter_list(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))


res = filter_list([10, True, 5.6, 45, 'ava'], int)
print(res)

