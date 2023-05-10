import  itertools

food_menu_listy=[['chicken','chicken-Biryani'],['mutton','mutton-Biryani'],['egg','egg-Biryani'],['egg','egg-Biryani']]
print(food_menu_listy)
str_output='OUTPUT'
print(f'{str_output:*^23}')
print(list(itertools.chain.from_iterable(food_menu_listy)))
# [['chicken', 'chicken-Biryani'], ['mutton', 'mutton-Biryani'], ['egg', 'egg-Biryani']]
# ['chicken', 'chicken-Biryani', 'mutton', 'mutton-Biryani', 'egg', 'egg-Biryani']
print(f'{str_output:*^23}')

