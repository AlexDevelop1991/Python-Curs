# Создать список с тремя словарями:
user_prof = [{
    'name': 'Sam',
    'id': 46,
},
    {
    'name': 'Jonny',
    'id': 789,
},
    {
    'name': 'Alex',
    'id': 390,
}]

# С помощью оператора распаковки списка создать три переменные каждая из которых будет содержать один из словарей
first_prof, second_prof, three_prof = user_prof


# Создать функцию которая будет принимать два аргумента,функция должна распаковывать словарь
def info_prof(name, id):
    if not id:
        return f"Name {name} not id"
    return f"Name {name} profile id: {id} "


# Вызвать функцию три раза:
print(info_prof(**first_prof))
print(info_prof(**second_prof))
print(info_prof(**three_prof))
