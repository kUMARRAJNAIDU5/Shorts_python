import json
import pickle
class Food():
    def __init__(self, name:str,calories:float):
        self.name= name
        self.calories=calories

    def describe_fruit(self):
        print(self.name, self.calories, sep=":->")

if __name__ == '__main__':

    food_items_calories={}

    fruit: Food = Food("mango", 65)
    fruit.describe_fruit()
    food_items_calories['fruit']=fruit

    chicken: Food = Food("chicken-burger", 150)
    chicken.describe_fruit()
    food_items_calories['chicken'] = chicken

    with open('data.pickle','wb') as file:
        pickle.dump(food_items_calories,file)

    with open('data.pickle', 'rb') as file:
        print('After reading from pickle ')
        food_obj: Food= pickle.load(file)
        f= food_obj['fruit']
        c= food_obj['chicken']
        print(f' fruits : {f.name} : {f.calories}')
        print(f' chicken :{c.name} : {c.calories}')

        # Normal way of storing data in json format
        # with open('banana.json','w') as file:
        #     data={'name':fruit.name,'calories':fruit.calories}
        #     json.dump(data,file)
        #
        # with open('banana.json','r') as file:
        #     data=json.load(file)
        #     print("data recived back",data)