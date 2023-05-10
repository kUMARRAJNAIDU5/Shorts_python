from enum  import  Enum

class  State(Enum):
    OFF = 0
    ON = 1
    HOLD = 2


state=State.ON
print(State.ON.value)
print(State.OFF.value)
if state == State.ON:
     print("configuration is turned ON in prod")
elif  state == State.OFF:
    print("configuration is turned OFF in prod")


class Signal(Enum):
    RED = 'Red'
    GREEN = 'Green'
    ORANGE = 'Orange'
color= Signal.RED

if color == Signal.RED:
     print(color.value)
elif  color == Signal.GREEN:
    print(color.value)
elif  color == Signal.ORANGE:
    print(color.value)


for signal in (Signal):
    print(signal.value, "-", signal.value, )

