hotbar=[
    "Torch",
    "Rock",
    "Sword",
    "Shield"
]
print(hotbar)
index= hotbar.index('Sword')
item= hotbar.pop(index)
hotbar.insert(0,item)
print(hotbar)