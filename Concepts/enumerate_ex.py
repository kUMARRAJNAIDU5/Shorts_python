nums = [1,2,3,4,5]
car_brand_names=["Benz","bmw","Aston Martin","bentley","jaggur","bugatti"]
numitr = iter(car_brand_names)
print(next(numitr, 0)) # prints 1
print(next(numitr, 0)) # prints 2
print(next(numitr, 0)) # prints 3
print(next(numitr, 0)) # prints 4
print(next(numitr, 0)) # prints 5
print(next(numitr, 0)) # prints 0
print(next(numitr, 0)) # prints 0