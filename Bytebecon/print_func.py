movies_names =["ironman","superman","batman","spiderman"]
print(movies_names)


movies_names_time=["ironman",120,"superman",167,"batman",101]
print(movies_names_time)

movies_names_tuple=(
    ["ironman",8.5],
    ["superman",8],
    ["batman",9.5]
)

kumar_info_dict = {
    'username': 'KumarRaJ',
    'active': True,
    'social':['insta','linkiden'],
    'movies_watcghed': ['RRR', 'titanic', 'superman'],
    'favoirurte_food': ['fish rice', 'chicken grilled', 'fruits shake'],
    'workout_format': ['yoga', 'boxing', 'core -workout'],
    'company_employeed': ['Shell', 'Telstra', 'Cisco']
}
STR_OUTPUT= 'OUTPUT'
print(f'{STR_OUTPUT:*^23}')
print(movies_names, sep=",")
print(movies_names_time, sep=" - ")
print(movies_names_tuple, sep=" - ")
print(type(movies_names_tuple))
print(kumar_info_dict.keys(), sep=" - ")
print(kumar_info_dict.values(), sep=" - ")

# if you don't key to have  dict_keys, dict_values, [] at start and end  using *

print(f'{STR_OUTPUT:*^23}')
print(*movies_names, sep=",")
print(*movies_names, sep="-->")
print(*movies_names_time, sep=" - ")
print(*movies_names_tuple, sep=" - ")
print(*kumar_info_dict.keys(), sep=" - ")
print("Values:",*kumar_info_dict.values(), sep=" - ")
print("Keys:",*kumar_info_dict, sep=" -> ")
print(f'{STR_OUTPUT:*^23}')