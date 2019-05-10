# This method will update original list value because variables do not store list values directly; they store references to lists
def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)



# To keep original list intact , use copy module
import copy

def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
spamListCopy = copy.copy(spam)     # A separate copy of list is created
eggs(spamListCopy)
print("Modified list after using copy = ",spamListCopy)
print("Original list intact after using copy = ",spam)
