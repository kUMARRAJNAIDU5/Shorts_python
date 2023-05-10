def myfunc():
  global x
  x = 300

myfunc()

print(x)



def func():
  x = 20

  def inner_func():
      nonlocal  x
      x =10
      print('Inner ', x)

  inner_func()
  print('Outer',x)



func()
