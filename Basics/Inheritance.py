class Parent:  # define parent class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        self.parentAttr = attr

    def getAttr(self):
        print("Value of attribute :", self.parentAttr)


class Child(Parent):  # define child class
    def __init__(self):
        print("Calling child constructor")
        super().__init__()       # invoking parent class constructor

    def childMethod(self):
        print('Calling child method')


c = Child()  # instance of child
# c.childMethod()  # child calls its method
# c.parentMethod()  # calls parent's method
# c.setAttr(200)  # again call parent's method
# c.getAttr()  # again call parent's method

print(c.__dict__)
print("Original attribute value of parent class : ",Parent.parentAttr)