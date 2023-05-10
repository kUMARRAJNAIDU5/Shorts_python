

from secrets import compare_digest
my_input='cornhub123'
password='cornhub123'

print(my_input == password)

print(compare_digest(my_input,password))