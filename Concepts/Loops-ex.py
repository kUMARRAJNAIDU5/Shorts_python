for _ in range(5):
    print(_)
    print("Value: " + str(_))


def get_resturant_items():
    return "chicken","mutton","egg"

food ,_,_  = get_resturant_items()
print('************')
print(_)
print("food: ",food)
print("food: {}".format(food))

print('************enumerate')
car_brand_names=["Benz","bmw","Aston Martin","bentley","jaggur","bugatti","Rolls-Royce","Ferrari","McLaren"]
for index,item in enumerate(car_brand_names):
    print(index,":"+item)

print('************enumerate')
for count, direction in enumerate(car_brand_names, start=2):
    print(count,":",direction)
print('************range')
for _ in range(len(car_brand_names)):
    print(_)

print('************while')
x=0
while x < len(car_brand_names):
    print(car_brand_names[x])
    x = x+1
print('************transformed_data')
transformed_data = [" Hi "+value for value in car_brand_names ]
print(transformed_data)

print('************lambda')
double_value = lambda x: str(x).capitalize()
for value in car_brand_names:
  print(double_value(value))
print('************')

"""
range
enumerate


car_brand_names=["Mercedes","Lamborghini","Aston Martin","bentley","jaggur","bugatti","Rolls-Royce","Ferrari","McLaren"]

for x in range(len(car_brand_names)): 
    print(lst[x]) 

for x in car_brand_names: 
    print(x) 

[print(x) for x in car_brand_names] 

 
x = 0
 
# Iterating using while loop 
while x < len(car_brand_names): 
    print(car_brand_names[x]) 
    x = x+1  
    

import numpy as np
n = np.arange(34)
for x in np.nditer(car_brand_names):
    print(x)

[print(x) for x in car_brand_names]
print('************')
_
"""