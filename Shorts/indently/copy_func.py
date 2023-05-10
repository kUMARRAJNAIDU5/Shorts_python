import copy
# Int copy
salary1 = 10000
salary2= salary1
print('********************************************')
print("salary1 :{} anb ID:{}: ".format(salary1,id(salary1)))
print("salary2 :{} anb ID:{}: ".format(salary2,id(salary2)))
salary1 = 20000
print('********************************************')
print("salary1 :{} anb ID:{}: ".format(salary1,id(salary1)))
print("salary2 :{} anb ID:{}: ".format(salary2,id(salary2)))
print('********************************************')

# String  copy
var1='Benz'
var2=var1
print("var1 :{} anb ID:{}: ".format(var1,id(var1)))
print("var2 :{} anb ID:{}: ".format(var2,id(var2)))
var1='Benz_Audi'
print("var1 :{} anb ID:{}: ".format(var1,id(var1)))
print("var2 :{} anb ID:{}: ".format(var2,id(var2)))
print('********************************************')

# Copy() creates a new memory space and object... always use with collection dataytyuoe
car_names = ["lamborghini","Ferrari", "Maserati", "Benz"]
car_names_copy= car_names.copy()

car_names_copy= car_names
print("car_names :{} anb ID:{}: ".format(car_names,id(car_names)))
print("car_names_copy :{} anb ID:{}: ".format(car_names_copy,id(car_names_copy)))

print('*****************After-extend()***************************')
car_names.extend(["rolls royace","VW","Jaggur","Ducati"])
print("car_names :{} anb ID:{}: ".format(car_names,id(car_names)))
print("car_names_copy :{} anb ID:{}: ".format(car_names_copy,id(car_names_copy)))