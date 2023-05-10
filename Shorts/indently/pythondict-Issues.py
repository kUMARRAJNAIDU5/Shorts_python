def func(key,value,d={}):
    d[key] = value
    print(d)

print(func(10,20))
print(func(100,200))


def func2(key,value,d=None):
    if d is None:
        d = {}
    d[key] = value
    print(d)

print(func2(10,20))
print(func2(100,200))