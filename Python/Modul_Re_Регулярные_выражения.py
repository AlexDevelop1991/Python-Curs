import re

# my_name = 'My name is Alexander.Alexander is good man'

# # res = re.search(r'Alexander', my_name)
# # print(res)

# # res = re.search('Alex....r.$', my_name)
# # print(res)
# # print(res.span())
# # print(res.start())
# # print(res.end())

# # my_pattern = re.compile(r'^My.*\.$')
# # print(my_pattern)
# # print(my_pattern.match(my_name))


# my_pattern = re.compile(r'Alex....r')
# print(my_pattern.findall(my_name))

# Регулярные выражения для проверки e-mail
def email_check(email):
    email_regexp = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$'
    email_check_pattern = re.compile(email_regexp)
    validation_result = 'Valid' if email_check_pattern.fullmatch(
        email) else 'Not valid'
    return (email, validation_result)


print(email_check('stars@gmail.com'))
print(email_check('@gmail.com'))
print(email_check('stars@gmail.'))
print(email_check('starsgmail.com'))
print(email_check('.com'))
print(email_check('StArS@gmail.com'))
print(email_check('st_ar_s@gmail.com'))
print(email_check('stars@sub.gmail.com'))
