with open('input.txt','r') as input,\
    open('output.txt','w') as output:
    text= input.readline()
    uppercase= [t.upper() for t in text]
    output.writelines(uppercase)