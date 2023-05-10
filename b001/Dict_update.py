STR_OUTPUT= 'OUTPUT'
print(f'{STR_OUTPUT:*^23}')
profile ={
    'name':'N/A',
    'email': 'N/A',
    'phone': 'N/A',
    'mobile': 'N/A'
}

user_input={
    'name': 'kumarraj',
    'email': 'kmr.23@gmail.com',
    'mobile': '9538222888'
}

# New way of doing it
profile |= user_input
print(profile)


print(f'{STR_OUTPUT:*^23}')
print("Values:",*profile.values(), sep=" - ")
print("Keys:",*profile, sep=" -> ")
print("Values:",profile.values(), sep=" - ")
print("Keys:",profile, sep=" -> ")

# old way of doing it
profile.update(user_input)
print(profile)


