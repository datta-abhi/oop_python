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

# inheritance child class inherits parent Class
class DigitalProduct(Product):

    def __init__(self,link):
        # digital products has additional attribute link other than name and price
        self.link = link

    def get_link(self):
        self.link = input("Enter the link: ")

    def show_link(self):
        print('Link to view: ',self.link)




p1 = DigitalProduct("")
p1.get_data()
p1.get_link()
p1.show_data()
p1.show_link()