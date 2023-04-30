import secrets
import string

# print(string.ascii_letters)  # весь алфавит в верхнем и нижнем регистре
# print(string.ascii_lowercase)  # алфавит в нижнем регистре
# print(string.ascii_uppercase)  # алфавит в верхнем регистре
# print(string.digits)  # Цифры 0123456789
# print(string.punctuation)  # спец символы

# print(string.ascii_letters + string.digits + string.punctuation)

all_chars = string.ascii_letters + string.digits + string.punctuation
print(''.join(secrets.choice(all_chars) for i in range(8)))
