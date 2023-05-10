class Car:
    def  __init__(self,model: str, color:str):
     self.model= model
     self.model= color
     print(f'{model} {model}')

    def ev_sports_drive(self):
        print(f'{self.model}  drive mode is EV enabled ')



car: Car = Car("Benz","Red")
car.ev_sports_drive()
