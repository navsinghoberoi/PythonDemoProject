'''Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.'''

# Sol 1 use Set()
list1 = [1,2,1,2,3,3,1,2,3]
newList1 = set(list1)
print("List without duplicate values = ",newList1)



# Sol 2 using loops
def removeDuplicate(list):
    print("Original list with duplicates = ",list)
    listWithoutDuplicates = []
    for i in list:
        if i not in listWithoutDuplicates:
            listWithoutDuplicates.append(i)
    return listWithoutDuplicates

output = removeDuplicate(list1)
print(output)

