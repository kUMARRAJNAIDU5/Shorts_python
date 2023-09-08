class MobilePhone():
    def __init__(self,name:str, model:str, color:str):
        self.name=name
        self.model= model
        self.color= color
        print("base class Mobile Phone been called ")

    def  battery_status(self):
        print("base class : battery_status() func ")

    def  take_photos(self):
        print("base class : take_photos() takes very low quality  photo ")

class Iphone(MobilePhone):
    def __init__(self,name:str, model:int, color:str, price:int):
        super().__init__(name,model,color)
        self.price=price

    def  take_photos(self):
        # How to excplity called the base method()
        super().take_photos()
        print(f'iphone {self.model} takes 4k  quality photos and videos ')

    def battery_status(self):
        print(f'{self.model} battery is too good to last for 1-2 days ')


class Android(MobilePhone):
    def __init__(self, name: str, model: int, color: str, price: int):
        super().__init__(name, model, color)
        self.price = price

    def take_photos(self):
        super().take_photos()
        print(f'Android {self.model} take good/average quality photos and videos ')

print('*************************')
iphone:Iphone= Iphone("apple","iphone 14 pro","white",130000)
iphone.take_photos()
iphone.battery_status()

print('*************************')
samasung:Android= Android("samasung","ultranote plus","white",98000)
samasung.take_photos()