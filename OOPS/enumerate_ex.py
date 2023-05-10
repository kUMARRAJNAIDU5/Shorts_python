directions = [
    'Head north on Broadway toward W 48th St',
    'Turn left onto W 58th St',
    'Turn right onto 8th Ave',
    'Turn left onto Broadway',
    'Turn left onto Lincoln Center Plaza',
    'Turn right onto Jaffe Dr',
    'Turn left onto Broadway',
    'Turn left onto W 65th St'
]

for count, direction in enumerate(directions, start=5):
    print(count, direction)


for count, direction in enumerate(directions):
    print(count, direction)
