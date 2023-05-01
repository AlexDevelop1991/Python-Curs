import secrets
import string
import re


def check_password(password):
    symbol = r'^'
    if len(password) < 8:
        raise TypeError('To be 8 element or more')
    return (password)


my_password = input('Enter password: ')

print(check_password(my_password))
