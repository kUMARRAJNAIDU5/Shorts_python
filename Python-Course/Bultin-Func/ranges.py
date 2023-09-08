import sys

numbers : range = range (9)
print(numbers)

numbers2 : range = range (25*253)
print(numbers2)

print(sys.getsizeof(numbers2))

