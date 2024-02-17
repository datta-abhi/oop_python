class Parent:

    # initializing parent constructor
    def __init__(self):
        self.parent_balance = 9999

    def display_balance(self):
        print('Balance of parent Class is : ',self.parent_balance)

class Child(Parent):
    pass

class OverChild(Parent):

    def __init__(self):
        self.balance = 4999

class SuperChild(Parent):

    # constructor of cild
    def __init__(self):
        self.child_balance = 20000   # child balance
        super().__init__()      #accessing parent balance using super
    def display_child_balance(self):
        print('Child balance is: ',self.parent_balance + self.child_balance)

# mike = Child()
# mike.display_balance()
#
# john = OverChild()
# john.display_balance()

tom = SuperChild()
tom.display_child_balance()