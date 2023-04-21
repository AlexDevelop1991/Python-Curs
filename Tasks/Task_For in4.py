# Вариант 1
# Сокращенный For in с фильтрацией списка
# Создать список с элементами str
my_list = ['abc', 'da', 'none', 'brand', 'no']
# Из этого списка создай новый список в котором остнануться только строки длинна которых больше 3
new_list = [string for string in my_list if len(string) > 3]
# Результат списка вывести в терминал
print(new_list)

print(my_list)

my_list = ['abc', 'da', 'none', 'brand', 'no']

new_list = []

for string in my_list:
    if len(string) > 3:
        new_list.append(string)

print(new_list)

print(my_list)