class Person:

    # initialize a constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # instance method which acts upon instance self
    def greet(self):
        print('Hello my name is {} and I am {} yrs old'.format(self.name,self.age))

    def name_length(self):
        return len(self.name)

p1 = Person('Abhi',32)
p1.greet()
length = p1.name_length()
print(length)