# Распаковка списков(list)
my_car = ['bmw 320', 'opel omega', 'nissan leaf', 'audi a4']
my_bmw, my_opel, my_nissan, my_audi = my_car
print(my_bmw)
print(my_opel)
print(my_nissan)
print(my_audi)
# Использование * при распаковке
my_bmw, *other_car = my_car
print(my_bmw)
print(other_car)
# Рпспаковка списка в позиционные аргументы
user_data = ['Alex', 23]


def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(*user_data))

# Распаковка словаря(dict) в аргументы с ключевыми словами
user_profile = {
    'name': 'Alex',
    'comments_qty': 23,
}


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(**user_profile))

