# Создай функцию с одним параметром типа dict:
def image_info(img):
    # Функция ожидает словарь в котором должно быть как минимум два ключа: image_id, image_title
    if ('image id'not in img) or ('image title'not in img):
        # Если хотя бы одного ключа нет в словаре функция должна сгенерировать ошибку TypeError
        raise TypeError('Keys image id and image title must be present')
    # Функция должна возвращать строку такого вида: Image 'my cat' has id 123
    return f"Image '{img['image title']}' has id {img['image id']}"


print(image_info({'image title': 'My cat', 'image id': 123}))
# Корректная обратоботка в случаи ошибки
try:
    print(image_info({'image id': 123}))
except TypeError as e:
    print(e)
