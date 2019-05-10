class Parent:


    aVar = 10
    bVar = 20


    def printMethod(self):
        print("Value of variables = ",self.aVar ,"", self.bVar)



p = Parent()
p.printMethod()