import json
# Создать словарь используя ключи с значениями разных типов
my_dict = {
    'id': 450,
    'name': 'Alex',
    'age': 31,
    'weight': 63.3,
    'married': True

}
# Конвертируй словарь в JSON
my_dict_json = json.dumps(my_dict, indent=2)
# Результирующий JSON вывести в терминал
print(my_dict_json)
# Вывести в терминал тип результирущего значения
print(type(my_dict_json))
