car_names: list[str] = ["lamborghini","Ferrari", "Maserati", "Benz","Audi","BMW", "rolls royace","VW","Jaggur","Ducati"]
for name in car_names:
    print(car_names.index(name)+1,":",name )

print('***************************************')
for name in car_names:
    print(car_names.index(name) + 1, "->", name)


print('***************************************')
for i, name in enumerate(car_names) :
    print(i+1,":",name)
