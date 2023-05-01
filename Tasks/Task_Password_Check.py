import re


def check_password(password):
    # Проверка пароля на длинну \S- говорит о том что tab,пробел и переход на новую строку не считаються
    length_pattern = re.compile(r'\S{8,}')
    # Проверка на буквы в нижнем регистре
    lowercase_pattern = re.compile(r'^.*[a-z]+.*$')
    # Проверка на буквы в верхнем регистре
    uppercase_pattern = re.compile(r'^.*[A-Z]+.*$')
    # Прверка на наличиние хотя бы одной цифры
    number_pattern = re.compile(r'^.*[0-9]+.*$')
    # Проверка на наличие хотя бы одного спец символа
    special_symbol_pattern = re.compile(r'^.*[@%#!&*^]+.*$')
    # Проверка на пробелы, tab, и другие спец символы
    no_whitespace_pattern = re.compile(r'^\S*$')

    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, 'No whitespaces allowed in the password')

    if not re.fullmatch(length_pattern, password):
        return (False, 'Password must have at least 8 symbols')

    if not re.fullmatch(lowercase_pattern, password):
        return (False, 'Password must have at least one lowercase letter')

    if not re.fullmatch(uppercase_pattern, password):
        return (False, 'Password must have at least one uppercase letter')

    if not re.fullmatch(number_pattern, password):
        return (False, 'Password must have at least one number')

    if not re.fullmatch(special_symbol_pattern, password):
        return (False, 'Password must have at least one special symbol @%#!&*^')

    return (True, 'Password is valid!')


# print(check_password('1334Nv @&46NH'))
# print(check_password('123'))
# print(check_password('12345678'))
# print(check_password('1234567a'))
# print(check_password('abcdAGCT'))
# print(check_password('12kvsLAZ'))
# print(check_password('123V3nd$&'))

while True:
    password = input('Enter password: ')
    password_check_res = check_password(password)
    if password_check_res[0]:
        print(password_check_res[1])
        break
    print(password_check_res[1])
