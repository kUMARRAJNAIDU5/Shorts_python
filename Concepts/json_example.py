import json
import requests


def main():
    data = {
        'username': 'KumarRaJ',
        'active': True,
        'subscribers': 237612,
        'order_total': 39.99,
        'movies_watcghed': ['RRR', 'titanic', 'superman'],
        'favoirurte_food': ['fish rice', 'chicken grilled', 'fruits shake'],
        'workout_format': ['yoga','boxing','core -workout'],
        'company_employeed':['Shell','Telstra','Cisco']
    }

    print(data)

    # printing object as json string
    s = json.dumps(data)
    print(s)
    print(type(s))
    print(json.dumps(s, indent=5))


    # getting python object from json string
    data2 = json.loads(s)
    assert data2 == data

    # writing data to file
    with open('test_data.json', 'w') as f:
        json.dump(data, f)

    # reading data from file
    with open('test_data.json') as f:
        data3 = json.load(f)
    assert data3 == data

    r = requests.get('https://jsonplaceholder.typicode.com/users')
    print(type(r.json()))


if __name__ == '__main__':
    main()