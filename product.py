class Product:

    # initialize constructor
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def get_data(self):
        # used to take user input
        self.name = input("Enter name of product: ")
        self.price = int(input('Enter the price: '))

    def show_data(self):
        # prints data
        print("Product: ",self.name)
        print("Price: ",self.price)

p1 = Product("","")
p1.get_data()
p1.show_data()