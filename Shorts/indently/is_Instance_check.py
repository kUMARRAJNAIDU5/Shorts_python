# type vs isinstance

class fruit:
    pass

class banana(fruit):
    pass

a = isinstance(fruit(), fruit)
print("check-1:",a)

b = type(fruit())==fruit
print("check-2:",b)

c = isinstance(banana(), fruit)
print("check-3:",c)


c = type(banana())== fruit
print("check-4:",c)