# Создайте две переменные и присвоите им одинаковые последовательности типа SET при этом не копируй одну переменную в другую
string1 = {'a', 'b', 'c', 'd'}
string2 = {'a', 'b', 'c', 'd'}
# Вывести в терминал результат сравнения двух созданых объектов,объясни результат
print(string1 == string2)  # Print(string1.__eq__(string2))
print(string1 != string2)
# Сравни два объекта используя оператор is,объясни результат
print(string1 is string2)
# Проверь есть ли определеные эдементы в наборе,используя оператор in
print('f' in string1)
print('b' in string2)
print('g' not in string1)
print('h' in string2)
print(() in string2)
# Error - TypeError: unhashable type: 'list'
# print([] in string1)