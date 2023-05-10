class Person:
    number_of_people =0
    GRAVITY=2.3
    per_lst=[]

    def  __init__(self,name):
     self.name= name
     self.per_lst.append(name)
     Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
     cls.number_of_people+=1

p1 = Person("kumar")
p2 = Person("raj")
p =  Person("naidu")

print(Person.number_of_people_())
print(Person.per_lst)