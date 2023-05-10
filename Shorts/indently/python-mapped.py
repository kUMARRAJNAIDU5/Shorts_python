values=[5,10,15,20]

def x_ify(n: int) -> str:
    return n*'x'

mapped=map(x_ify,values)
print(list(mapped))