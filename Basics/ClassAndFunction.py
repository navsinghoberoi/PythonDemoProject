# Functions #


# NOTE -- Indendation plays a major role in Python as brances are not used to define code blocks.
# Increase in indentation means starting of a code block. All subsequent lines with same indentation means they are part of
# same code block.


## Defining a func
def add_num(var1, var2, var3=10):
    sum_of_numbers = var1 + var2 + var3
    print("Sum of two numbers = ", sum_of_numbers)
    return sum_of_numbers

# Calling a fund
finalSum = add_num(10, 5.2)
print("Value returned from method = ", finalSum)

finalSum = add_num(10, 5.2, 2)
print("Value returned from method = ", finalSum)


########################################################################################################################

# Classes and Objects #


# self is to refer to the current object (same as this in Java). Self is mandatory for all methods of a class including constructor

class Student:
    def __init__(self, name, amount=100):     # Constructor is created
        print("Object is created via this constructor")
        self.name = name
        self.amount = amount

    def print_data(self):
        print("Hello ", self.name)
        print("You need to submit amount ", self.amount)


obj1 = Student('Ajeet')     # Creating object of class
obj1.print_data()
obj2 = Student('Mini', 2000)
obj2.print_data()






# Private members of a class #

class PrivateStudent:


    dress = 'Generic Dress'
    __dress__ = 'Public Dress'


    def __init__(self,name):
        self.name = name

    def getStudentName(self):
        print("Private var = ",self.__dress__)
        print("Public var = ", self.dress)



stud1 = PrivateStudent('Jas')
stud1.getStudentName()


print(stud1.dress)
print(stud1.__dress__)
