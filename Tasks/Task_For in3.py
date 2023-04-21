# Вариант 1
# Сокращенный For in
# Создай словарь с несколькими ключами,значение которых должно быть типа 'str'
my_dict = {
    'one': 'true',
    'two': 'false',
    'three': 'none'
}
# Создать новый словарь на основании существующего,в котором значение всех ключей должны быть в верхнем регистре
new_dict = {k: v.upper() for k, v in my_dict.items()}
# Результат словаря вывести в терминал
print(new_dict)

print(my_dict)


# Вариант 2
# Формирование нового словаря в обычном режиме For in
my_dict = {
    'one': 'true',
    'two': 'false',
    'three': 'none'
}

new = {}

for key, value in my_dict.items():
    new[key] = value.upper()

print(new)

print(my_dict)
