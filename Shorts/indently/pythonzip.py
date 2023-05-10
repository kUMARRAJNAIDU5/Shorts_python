fruits = ["fruits",'🍏','🍇','🍐']
sports = ["sports",'⚽️','⚾️','🏉']
cars = ["cars",'🚗','🚁','🛻']

for f,s,c in zip(fruits,sports,cars):
    print(f,s,c, sep='   ---   ')


