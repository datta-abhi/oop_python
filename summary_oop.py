# creating a class
class Vehicle:

    #creating class attribute
    class_att = 'This is a vehicle class'

    #creating class method
    @classmethod
    def class_method(cls):
        print('Method of  Vehicle Class')
        print('I can access the class attribute: ',cls.class_att)

    # creating a static method
    @staticmethod
    def static_method():
        print('I am a static method')

    # creating constructor to add instance variable
    def __init__(self,name,color):
        self.name = name
        self.color = color

    # instance method
    def display_info(self):
        print('Name of vehicle: {}, color  is {}'.format(self.name,self.color))

# Inheritence of Parent to Child class
class Car(Vehicle):
    def __init__(self,name,color,fuel_type):
        super().__init__(name,color)  #super method to retain parent attributes and also have new attributes
        self.fuel_type = fuel_type

    # override parent method by child staticmethod
    def display_info(self):
        print('Name of Car: {}, color is {}, fuel type is {}'.format(self.name,self.color,self.fuel_type))

# creating an object of a class
v1 = Vehicle('Coolcar','red')
print('Name: {}, Color: {}'.format(v1.name,v1.color))
print(v1.class_att)
v1.class_method()
v1.static_method()

v1.display_info()

#creating object of Child Class
car1 = Car('Luxury Car','Black','Electric')
car1.display_info()
