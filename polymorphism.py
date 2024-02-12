# print(len('helloworld'))
# print(len(['apple','banana','mango']))

class Food:
    def class_name(self):
        print('FOOD')

class Fruit(Food):
    def class_name(self):
        print('FRUIT')

f = Fruit()
f.class_name()