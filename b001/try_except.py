balance = 945.70

while True:
    try:
        num= float(input('Deposit'))
        break
    except ValueError:
            print("must be a vaild nummber..")

balance+=num
print(f'balnce:{balance}')