list=[1,-23,1,3,5,6]

if any(n>0  for n in list):
    print('Success')


if all(n>0  for n in list):
    print('All Success')
else:
    print("All Failed")