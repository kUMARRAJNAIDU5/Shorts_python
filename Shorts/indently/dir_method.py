text:str ='text'
number: int =10

car_names = ["lamborghini","Ferrari", "Maserati", "Benz"]

print(dir(text))
print(dir(number))

for attr in dir(text):
    print("string: ",attr)

for attr in dir(number):
    print("Number: ",attr)

str=''
for car in dir(car_names):
    print("car: ",car)
    str+=car+"-->"
