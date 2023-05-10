class Lamp:
    def __init__(self, name:str, model:str):
        self.name=name
        self.__model= model


    def description(self):
        print(self.name, self.__model)



lamp:Lamp = Lamp('led lamp',1023)
print(lamp.description())

