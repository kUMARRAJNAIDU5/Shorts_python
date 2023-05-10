log= lambda *args: print(*args)

has_money = True
has_time = True
has_friends = True
has_internet = True

# def func():
#     if has_money:
#         if has_time:
#             if has_friends:
#                 if has_internet:
#                     log("Superb enjoYYYY")
#
#
# func()

# betterv approach here is
# Guard clause pattern



has_money = False
has_time = False
has_friends = False
has_internet = False

def func2():
    if not has_money:
        log("No money.....")
        return

    if not has_friends:
        log("No friends.....")
        return

    if not has_internet:
        log("No internet.....")
        return
    if not has_time:
        log("No time.....")
        return

func2()