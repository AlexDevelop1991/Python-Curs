my_img = ('1920', '1080', 50)

info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else 'Incorrect image formatting'

print(info)

# Переписать пример испрользуя инструкцию if, else
my_img = ('1920', '1080')

if len(my_img) == 2:
    print(f"{my_img[0]}x{my_img[1]}")

else:
    print('Incorrect image formatting')
# С помощью тернарного оператора можно было проверить длинну строки
my_str = "Very llllllllooooooooooooooooooooooooooooooooooooooooooooooooooooooooooonggggggg"
# Если длинна строки больше 79 символов выводит в терминал 'Long string' если нет то 'Short string'
str_len = f"Long string" if len(my_str) > 79 else 'Short string'


print(str_len)
