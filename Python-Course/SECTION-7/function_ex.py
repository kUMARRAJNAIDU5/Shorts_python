def greet_msg(name : str):
    print(f'Hello , {name}')

def greet_msg_culture_bases(name:str, message: str ='Hello -dutch- turkey', country:str ="india"):
    print(f'{name} {message} {country}')

greet_msg('Kumar')
greet_msg_culture_bases('Kumar')
greet_msg_culture_bases(name='Kumar',message='Australia hello',country='Australia')


def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2
    return num3

print(add(25,25))

def do_something():
    for i in range(5):
        print("do something")
do_something()