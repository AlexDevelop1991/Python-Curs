# Созлать класс Image.
# У каждого экземпляра класса Image должно быть три собственных атрибута: resolution, title, extension.
class Image:
    def __init__(self, resolution, title, extension):
        self.rezolution = resolution
        self.title = title
        self.extension = extension
# В классе должен быть метод resize с помощью которого можно поменять разрещение изображение.
# Вы должны просто менять значение атрибута: resolution
    def resize (self, new_resolution):
        self.rezolution = new_resolution
# Конвертиция обчекта класса Image в строку.
    def __str__(self):
        return f"{self.title}.{self.extension}"


first_img = Image('1920x1080', 'My dog', 'jpg')

print(first_img.rezolution)
print(first_img.title)
print(first_img.extension)

first_img.resize('4000x3000')

print(first_img.rezolution)

second_img = Image('8000x5000', 'My cat', 'png')

print(first_img)




# Мой пример:
class Car:
    def __init__(self, brand, price, vol_engine):
        self.brand = brand
        self.price = price
        self.vol_engine = vol_engine

    def new_brand(self, new_brand):
        self.brand = new_brand

    def __str__(self):
        return f"{self.brand},{self.price},{self.vol_engine}"


my_car = Car('Bmw', '20_000', '2.4')

print(my_car)

my_car.new_brand('Audi')

print(my_car)
