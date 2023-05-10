from io import StringIO

vowels: int = 0
strcontents : list =[]
str=""
string = StringIO()
print(id(string))
print(id(str))
for i in 'bananaou':
    if i in 'aeiou':
        vowels+=1
        strcontents.append(i)
        str+=i
        # print(id(str))
        string.write(i)
        print("string : ", id(str))
        print("string  builderID : ",id(string))

print(vowels)
print(strcontents)
print(str)
print(string.getvalue())