def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting('Good morning')
print(morning_greeting('Alex'))

evening_greeting = greeting('Good evening')
print(evening_greeting('Alex'))

day_greeting = greeting('Good day')
print(day_greeting('Alex'))