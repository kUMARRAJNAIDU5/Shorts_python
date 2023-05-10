#  string str_builder ID does not remainsame throught the loop
my_string=""
print(id(my_string))
for i in range(5):
    my_string+= f"video{i}\n"
    print(id(my_string))
    print(my_string)

print(id(my_string))
print(my_string)


#  string str_builder ID remains same throught teh loop
import  io
str_builder= io.StringIO()
print('builder id:',id(str_builder))
for i in range(5):
    str_builder.write(f"video {i}\n")

print('builder id:',id(str_builder))
my_string_new= str_builder.getvalue()
print('string id:',id(my_string_new))
print('string value:',my_string_new)