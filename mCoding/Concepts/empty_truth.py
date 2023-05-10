def do_something(options=None):
    if not options:
        options = {'option1': 1}
    print(options)


if __name__ == '__main__':
    x = (_ for _ in [5])

    do_something(options={})
    do_something(options={'egg':23})
    x = 1
    y = [2]

    x = y

    print(x)