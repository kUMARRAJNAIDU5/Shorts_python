STR_OUTPUT= 'OUTPUT'
print(f'{STR_OUTPUT:*^23}')

# Type-1
for _ in range (10):
    print(f'kumar:{_}')

# Type-1
for i in  range(10):
    print(i)
print(f'{STR_OUTPUT:*^23}')

# Type-3
car_names = ["lamborghini","Ferrari", "Maserati", "Benz","Audi","BMW", "rolls royace","VW","Jaggur","Ducati"]
for car in enumerate(car_names):
    print(car,sep='->')
print(f'{STR_OUTPUT:*^23}')

# Type-4
for idx,car in enumerate(car_names):
    print (idx,car, sep='->')
print(f'{STR_OUTPUT:*^23}')

# Type-5
for idx in range(len(car_names)):
    print (idx,car_names[idx], sep='->')
print(f'{STR_OUTPUT:*^23}')

# Type-6
place_name="india"
for idx in range(len(place_name)):
    print (idx,place_name[idx], sep='->')
print(f'{STR_OUTPUT:*^23}')