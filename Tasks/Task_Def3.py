def update_car_info(**car):
    car['is availabal'] = True
    return car


res = update_car_info(brand='Audi', price=15_000)
print(res)

# Error - TypeError: update_car_info() takes 0 positional arguments but 2 were given
# res2 = update_car_info('Audi', 15_000)
# print(res2)
