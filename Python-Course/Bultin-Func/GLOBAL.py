def hello():
    return 'GLOBAL'


class fruit:
    def __init__(self):
        print('GLOBAL')


print(globals())