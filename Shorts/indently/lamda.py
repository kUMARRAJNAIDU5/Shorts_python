def add2(a,b):
    return a+b

add = lambda  a,b : a+b
print(add(5,16,))
print(add2(5,16,))


sports=['cricketcup','footbal','hockey','bedgames','swim']
sorted_games = sorted(sports, key=lambda x: len(x) )
print(sorted_games)


