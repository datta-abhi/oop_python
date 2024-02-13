class Circle:

    #dont initialize any constructor
    @staticmethod
    def area(r):
        return 3.14*r*r

    @staticmethod
    def circumference(r):
        return 3.14*2*r

radius = 10
print('For radius of 10, area is {} and circumference is {}'.format(Circle.area(radius),Circle.circumference(radius)))