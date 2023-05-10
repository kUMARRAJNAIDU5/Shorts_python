# text: str ="kumarRajnaidu"
# print(text*5,sep='->')



#creating a function
def print_string(n):
    print("THE STRING IS 'Money Heist'")
    print("The string will be printed", n ,"times")
    print ("KumarRaj Naidu "*n,sep="-->" )
    print("KumarRaj" ," Naidu ", sep="-->")

#input function
print_string(5)


print(*range(5), sep="-->")
print("hello", "world"*4, sep=" cruel ")


for i in range(10):
    if i != 9:
        print(i, end="<--> ")
    else:
        print(i)

