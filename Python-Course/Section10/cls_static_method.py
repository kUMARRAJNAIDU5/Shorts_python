class Iphone():
    def __init__(self,name:str,model:str, gb:int):
        self.name= name
        self.model= model
        self.gb = gb
        print('i''m trigeered intit')

    def  get_instance_data(self):
         print("get_instance_data:",self.__dict__)

    def  display_iphone_spec(self):
        print("iPhone spec details are:",self.__dict__)

    @classmethod
    def get_iphone_memory_size(cls):
       return cls('iphone14 pro','14pro',256)

    @staticmethod
    def get_iphone_imea_no(name: str):
        return name.capitalize()

# calling class method()
iphone=Iphone.get_iphone_memory_size()
iphone.get_instance_data()
# iphone.display_iphone_spec()

# calling static method()
iphone2=Iphone.get_iphone_imea_no("kumar2342")
print("get_iphone_imea_no:",iphone2)