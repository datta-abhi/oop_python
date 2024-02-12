class Product:
    # class attributes
    quantity = 100

    def __init__(self,name,price):
        # name and price are instance attributes
        self.name = name
        self.price =price

    def summer_discount(self,discount):
        self.price = self.price*(1-discount/100)
        return self.price

# p1 = Product('iphone',2000)
# print(p1.name)
# print(p1.price)
#
p2 = Product('laptop',4000)
print(p2.name)
print(p2.price)
print(p2.summer_discount(10))

p3 = Product('T-shirt',10)
print('Price of {} after discount is {}'.format(p3.name,p3.summer_discount(20)))
