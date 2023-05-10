



"""
cars=[
    {"name":"bmw","price":50000,"offer":1},
    {"name":"benz","price":5000,"offer":1},
    {"name":"audi","price":60000,"offer":0},
    {"name":"bentely","price":900000,"offer":0},
    {"name": "ferrai", "price": 900000, "offer": 2}
    ]

STR_OUTPUT= 'OUTPUT'
print(f'{STR_OUTPUT:*^23}')
filer_result=[car for car in cars if car['offer']==1]

# filer_result=[car for car in cars if car['offer']==1]
print(*filer_result)
print(filer_result)

print(f'{STR_OUTPUT:*^23}')
filtered = filter(lambda car: car['offer'] ==2, cars)
print(list(filtered))

print(f'{STR_OUTPUT:*^23}')
def offer_filter(car):
    # if (car['offer'] == 1):
    #     return True
    # else:
    #     return False
    if not (car['offer'] == 1):
        return True

filtered_heights = filter(offer_filter, cars)
print(list(filtered_heights))
print(f'{STR_OUTPUT:*^23}')


# map function
def get_on_road_price(car_price):
    return car_price["price"]*0.67

on_road_price = map(get_on_road_price, cars)
print(list(on_road_price))

from functools import reduce

def get_total_cost_for_cars(cars):
    # Using List Comprehension with sum()
    return sum([car['price']*.3 for car in cars])

print(cars)
total = get_total_cost_for_cars(cars)
print("total:", total)



