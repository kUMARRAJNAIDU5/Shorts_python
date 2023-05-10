from uuid import uuid4

car_info= {'lamborghini':uuid4(),
        'Ferrari':uuid4(),
        'Maserati':uuid4()
        }

for k, v in car_info.items():
     print(k ,v , sep='-->')