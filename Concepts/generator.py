# Defining a generator function
def filtering_odd( numbers ):
    for num in range( numbers ):
        if num % 2 != 0:
            yield num
# Calling the generator function, passing a vale and declaring a generator object.
odd_num = filtering_odd( 20 )
print(list( odd_num ))