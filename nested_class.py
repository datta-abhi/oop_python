class Car:

    # initialize constructor
    def __init__(self,brand):
        self.brand = brand
        self.steering_obj = self.Steering()

    def drive(self):
        print('Drive')

    class Steering:
        # inner class
        @staticmethod
        def rotate():
            print('Rotate')

c1 = Car('ABC')
c1.drive()
steering = c1.Steering()
steering.rotate()