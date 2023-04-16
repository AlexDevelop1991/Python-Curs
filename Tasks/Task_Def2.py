# Создать функцию и задать два параметра
def merge_list_to_dict(list_one, list_two):
    # В функии должна быть встроенная функция ZIP для объединения двух списков,Конвертируй объект ZIP в словарь
    return dict(zip(list_one, list_two))

res_one = merge_list_to_dict(list_one=['a', 'b', 'c'], list_two=[10, True, False])
print(res_one)

res_two = merge_list_to_dict(list_two=[100, False, []], list_one=['abc'])
print(res_two)

res_tree = merge_list_to_dict([50, True, 'abc'], list_two=['id'])
print(res_tree)

# Error - SyntaxError: positional argument follows keyword argument
# res_tree = merge_list_to_dict(list_two=['id'],[50, True, 'abc'])
# print(res_tree)