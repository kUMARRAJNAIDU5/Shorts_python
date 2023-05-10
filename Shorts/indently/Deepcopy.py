from copy import deepcopy

a = [[1,2],[3,4]]
print("A: ",id(a))
b = a.copy()
print("B :",id(b))
b = deepcopy(a)
print("B :",id(b))
print(f'{a = }')
print(f'{b = }')

b[0][0] = 999
print(f'{a = }')
print(f'{b = }')