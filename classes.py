# self is to refer to the current object (same as this in Java). Self is mandatory for all methods of a class including constructor

class Student:
    def __init__(self, name, amount=100):
        print("Object is created via this constructor")
        self.name = name
        self.amount = amount

    def print_data(self):
        print("Hello ", self.name)
        print("You need to submit amount ", self.amount)


obj1 = Student('Ajeet')
obj1.print_data()
obj2 = Student('Mini', 2000)
obj2.print_data()
