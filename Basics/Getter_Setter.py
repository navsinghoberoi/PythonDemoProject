"""" Getter Setter used to incorporate data abstraction concept."""


class Student:

    def __init__(self, value):
        print("Object is created")
        self._value = value

    def __str__(self):
        return str(self._value)

    @property
    def value(self):
        print("This is getter method")
        print("Value of variable = ", self._value)
        return self._value

    @value.setter
    def value(self, value):
        print("This is setter method, here we are setting the variable value as ", value)
        self._value = value


obj1 = Student(10)
obj1.value           # Calling getter method before updating value
obj1.value = 20     # Invoke setter method
obj1.value     # Calling getter method after updating value
