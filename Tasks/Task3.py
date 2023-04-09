# Создать пустой словарь
my_dict = {}
# Трижды попросите пользователя сначала ввести название ключа,потом ввести значение для этого ключа
# Всего должно быть 6 запросов на ввод текста.
key_dict = input('Ведите первый предмет: ')
key2_dict = input('Введите второй предмет: ')
key3_dict = input('Введите третий предмет: ')
total_key = key_dict, key2_dict, key3_dict
my_dict.copy(total_key)
value_dict = input(key_dict + 'Введите оценку: ')
value2_dict = input(key2_dict + 'Введите оценку: ')
value3_dict = input(key3_dict + 'Введите оценку: ')
total_value = value_dict, value2_dict, value3_dict
my_dict.copy(total_value)

print(my_dict)