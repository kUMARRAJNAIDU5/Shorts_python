


# With out walrus
# nums=[]
# num= input('type a number')
# while num.isdigit():
#     nums.append(input(num))
#     num = input('type a number')

nums=[]
while(num:= input("Type the number")).isdigit():
    nums.append(num)
print(nums)

# Walrus operator
foods=list()
while food:= input("enter teh food?: ")!='q':
    foods.append(food)
print(list[foods])