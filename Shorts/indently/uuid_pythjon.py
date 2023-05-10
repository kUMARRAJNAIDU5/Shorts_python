from uuid import uuid4
print(uuid4())

users= {'kumarRAJNaidu':uuid4(),
        'Manju':uuid4()
        }
for k,v in users.items():
    print(k,v, sep=' : ')