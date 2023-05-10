# Unpacking and packing
RE_Models=["RoyalEnfield Hunter 350","RoyalEnfield Classic 350",
    "RoyalEnfield Bullet 350","RoyalEnfield Continental GT 650","RoyalEnfield Himalayan"]
model1,model2, *other = RE_Models
print(model1)
print(model2)
print(*other,sep='-->')

def get_bike_models():
    RE_Models = ("RoyalEnfield Hunter 350", "RoyalEnfield Classic 350")
    return RE_Models

def get_first_last_bike_models():
    return RE_Models

_,name1,= get_bike_models()
print(name1,_,sep=",")

a1,*_,a5= get_first_last_bike_models()
print(a1,a5,sep="---")


def f():
    return 1, 2, 3

__, __, x = f()
print(__, __, x)
