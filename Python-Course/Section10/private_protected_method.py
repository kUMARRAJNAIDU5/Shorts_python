class Lamp:
    def __init__(self, name:str, model:str,version:int):
        self.name=name
        self.__model= model
        self._version = version
        print("I'm being triggered base class init")
    def description(self):
        print(self.name, self.__model)
        # how to call private method inside normal method
        self.__self_maintenance()
    # private method been defined
    def __self_maintenance(self):
        print('private method been called within class')

class SolarLamp(Lamp):
    def __init__(self , name:str, model:str, version:int):
        super().__init__(name,model,version)
        print("I'm being triggered derived class init")


    def recharge_solar_lamp(self):
        print('recharghing from sun source light ')
        print("class attributes values : (%r)" % ((self.__dict__)))
        print("(%r)" % dict.keys((self.__dict__)))
        print("(%r)" % dict.values((self.__dict__)))
        print("sfsd (%r)" % (self.__dict__))
        var1=(self.__dict__)
        print("class attributes values : ",var1)

print('*************************')

lamp:Lamp = Lamp('led lamp',1023,5555)
print(lamp.description())
print(lamp._Lamp__model)
print(lamp._Lamp__self_maintenance())

print('*************************')
solarlamp:SolarLamp = SolarLamp('solar lamp',1023,7777)
print(solarlamp.recharge_solar_lamp())


