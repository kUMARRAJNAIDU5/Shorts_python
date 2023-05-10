class Car:
    def  __init__(self,model: str, color:str,mfd:str):
     self.model= model
     self.color= color
     self.mfd = mfd
     self.mileage="23km/-"  #instance variable that is not passed via constructor
     self._p_data_bhp = "120 bhp"  #private variable
     print(f'{model} {model}')

    def __str__(self):
        print(f'***********************')
        print(f'I''m from __str__ method()')
        print (f'model class data : {self.model} :{self.color}: {self.mfd} : {self.mileage}: {self._p_data_bhp}')
        return (f'model class data : {self.model} :{self.color}: {self.mfd} : {self.mileage}: {self._p_data_bhp}')

    def __repr__(self):
        print(f'***********************')
        print(f'I''m from __repr__ method()')
        # print (f'model class data : {self.model} :{self.color}: {self.mfd} : {self.mileage}: {self._p_data_bhp}')
        print( "%s(%r)" % (self.__class__, self.__dict__))
        return f'car class data({self.model} :{self.color}: {self.mfd} : {self.mileage}: {self._p_data_bhp})'

    def __eq__(self,other):
        print(f'***********************')
        print(f'I''m from __eq__ method()')
        return self.__dict__ == other.__dict__

    def ev_sports_drive(self):
        print(f'{self.model}  drive mode is EV enabled ')

car: Car = Car("Benz","Red","2023")
car2: Car = Car("Benz","Red","2023")
# car2: Car = Car("Benz","Blue","2023")
print(car)
print(car.__repr__())
print(car.__str__())
print(car==car2)

