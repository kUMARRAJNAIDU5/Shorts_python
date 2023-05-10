def greet_msg(name : str):
    print(f'Hello , {name}')

def greet_msg_culture_bases(name:str, message: str ='Hello -dutch- turkey', country:str ="india"):
    print(f'{message} {name} {country}')

greet_msg('Kumar')
greet_msg_culture_bases('Kumar')
greet_msg_culture_bases(name='Kumar',message='hello Australia',country='Australia')


def sum_numbers(num1: int, num2: int) -> int:
    """Add two numbers"""
    return num1 + num2
print('sum_numbers : ',sum_numbers(25,25))

