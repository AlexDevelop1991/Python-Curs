import random

print(random.random())
print(random.randint(1, 10))

print(random.choice('abcd'))
print(random.choice([1, 7, 19, 67]))

print(random.choices([3, 8, 12, 2, 49, 28], k=3))

my_list = [2, 9, 24, 60, 18]
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)


print(''.join(random.choices('ABCD0123456789', k=8)))
