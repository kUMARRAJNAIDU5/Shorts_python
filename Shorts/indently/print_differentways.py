from string import Template

name= 'KumarRaj Naidu'
age='36'
print(name+' : '+ str(age))
print(name,' : ',str(age))
print('{}:{}'.format(name,age))
print('%s :%s'%(name,age))
print(f'{name} : {age}')
sentence= {name} and {age}
