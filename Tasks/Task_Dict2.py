# Создать три словаря и объединить их
button_info = {
    'text': 'Buy',
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300,
}

button_price = {
    'price': 25,
    'other price': 40,
}

button = {               ## Либо с помощью |(прямая черта)
    **button_info,
    **button_style,
    **button_price,
}

print(button)
