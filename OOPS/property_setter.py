class Student:
    def __init__(self, name):
        self.__name = name
        self.__location= "Sydney"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter  # property-name.deleter decorator
    def name(self, value):
        print('Deleting..')
        del self.__name


s = Student('Steve')
print(s.name)
print(s.name)