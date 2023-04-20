# Вариант 1
# Создать функцию route_info которой будет передаваться словарь
def route_info(rount):
# Если в словаре есть ключ 'distance' и его значение целое число,верни строку 'Distance in your distanation is <distance>.
    if ('distance' in rount) and (type(rount['distance'] == int)):
        return f"Distance in your distination is {rount['distance']}"
# Иначе если в словаре есть ключи 'speed' и 'time' верни строку 'Distance in your distanation is <speed * time>.
    if ('speed' in rount) and ('time' in rount):
        return f"Distance in your distanation is {rount['speed'] * rount['time']}"
# Иначе верни строку 'No distance info is available'.
    return f"No distance info is available"

# Вариант 2 можно и так написать функию но лучше первый вариант!!!!
# def route_info(rount):
#     if ('distance' in rount) and (type(rount['distance'] == int)):
#         route_info = f"Distance in your distination {rount['distance']}"

#     elif ('speed' in rount) and ('time' in rount):
#         route_info = f"Distance in your distanation is {rount['speed'] * rount['time']}"

#     else:
#         route_info = f"No distance info is available"
#     return route_info

# Вызвать функцию несколько раз с разными аргументами.
print(route_info({'distance': 20}))

print(route_info({'speed': 50, 'time': 3}))

print(route_info({'max speed': 100}))
