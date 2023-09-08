is_connected : bool = True
has_electricity: bool =True
has_paid: bool = True

has_internet: bool = all([is_connected, has_electricity, has_paid])
print('Internet:',has_internet)

has_paid: bool = False
requirements: list[bool] =[is_connected,has_electricity,has_paid]
has_internet: bool = all(requirements)
print('Internet:',has_internet)̌

has_internet: bool = any(requirements)
print('Internet:',has_internet)