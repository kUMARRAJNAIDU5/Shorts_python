class Student:
    name = 'unknown'  # class attribute,
    def __init__(self, name, age):
        self.name = name  # instance attribute cannot access this fields in cls method
        self.age = age  # instance attribute

    @classmethod
    def getobject(cls):
        return cls('Steve', 25)


student=Student.getobject()
print(student.age,student.name)