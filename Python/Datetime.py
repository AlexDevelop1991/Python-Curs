from datetime import date
from datetime import time
from datetime import datetime, timedelta
import time

# my_date = date(2030, 10, 23)
# print(my_date)
# print(my_date.year)
# print(my_date.month)
# print(my_date.day)
# print(my_date.isocalendar())


# my_time = time(20, 23, 56)
# print(my_time)
# print(my_time.hour)
# print(my_time.minute)
# print(my_time.second)


# my_datetime = datetime(2250, 5, 16, 17, 30, 22)
# # print(my_datetime)
# # print(my_datetime.isoformat())
# # print(my_datetime.now())

# # если вместо b написать m то месяц будет ввиде числа,так вместо - можно использоват /(слэшь)
# # print(my_datetime.strftime('%d-%m-%Y'))
# # print(my_datetime.strftime('%d-%b-%Y %H:%M:%S'))

# # date_str = '16-05-2250'

# # date_converted = datetime.strptime(date_str, '%d-%m-%Y')
# # print(date_converted)


# print(my_datetime + timedelta(days=100, minutes=120))

# star_time = time.time()
# print(time.ctime(4546567669))
# time.sleep(2.5)
# end_time = time.time()
# print(end_time - star_time)

star_time = time.time()

my_list = list(range(1_000_000))
print(my_list[1000])

end_time = time.time()

print('Total duraction in the operation: ', end_time - star_time)
