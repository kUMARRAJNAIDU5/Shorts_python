def get_car_info(year:int,*cars: list ):
    print(cars)
    for car in cars:
        print(f'Year: {year} car name: {car}')


brand_names=["Benz","bmw","Aston Martin","bentley","jaggur","bugatti","Rolls-Royce","Ferrari","McLaren"]
get_car_info(2013,brand_names)


kumar_info_dict = {
    'username': 'KumarRaJ',
    'active': True,
    'social':['insta','linkiden'],
    'movies_watcghed': ['RRR', 'titanic', 'superman'],
    'favoirurte_food': ['fish rice', 'chicken grilled', 'fruits shake'],
    'workout_format': ['yoga', 'boxing', 'core -workout'],
    'company_employeed': ['Shell', 'Telstra', 'Cisco']
}

def get_person_info(**kwargs):
    print(kwargs)
    print('username:',kwargs.get('username'))
    print('social:', kwargs.get('social'))
    print('movies_watcghed:', kwargs.get('movies_watcghed'))

get_person_info(**kumar_info_dict)