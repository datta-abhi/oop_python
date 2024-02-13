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

    # class method to calculate age from birth year
    @classmethod
    def from_birth_year(cls,name,birth_year):
        age = 2024 - birth_year
        return cls(name,age)

    #using staticmethod to check if adult or not
    @staticmethod
    def is_adult(age):
        return age>=18


p1 = Person('Abhi',32)
p1.greet()
length = p1.name_length()
print(length)
print('-'*30)

# pass name and year of birth as parameters to class method
p2 = Person.from_birth_year('Bobby',2007)
p2.greet()

# pass age as parameter to static method
is_bob_adult = Person.is_adult(p2.age)
print(is_bob_adult)