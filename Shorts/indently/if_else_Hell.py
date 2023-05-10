def first_func():
    print("I from first_func ")
def second_func():
    print("I'm from second_func ")
def thrid_func():
    print("I'm from thrid_func ")
def fourth_func():
    print("I'm from fourth_func ")
def default():
    print("I  from default ")

var: int = 4
func: dict = {
1: first_func,
2: second_func,
3: thrid_func,
4: fourth_func
}

final = func.get(var,default)
final()

