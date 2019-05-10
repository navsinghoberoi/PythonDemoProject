# Lists aren’t the only data types that represent ordered sequences of values.
# For example, strings and lists are actually similar, if you consider a string to be a “list” of single text characters.
# Many of the things you can do with lists can also be done with strings: indexing; slicing; and using them with for loops,
# with len(), and with the in and not in operators.
# Only difference is that List is mutabe and String is non mutable datatype


# Importing built in modules to use methods #
import random
import time
from functools import reduce

startTime = time.time()

# Print data using print()
word = 'word'
line = "This is a line"
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

print("hello world!")
print("Word var value = " + word)
print("Line var value = " + line)
print("Paragraph var value = " + paragraph)

# Take user Input
name = 'Navpreet'
# name = input("Enter user name : ")  Uncomment to take users input
print("\nName of the user = " + name)

# Strings
str = "Hello"
print(str[0])
print(str[0:2])
print(str[2:])
print(str + " concat")
print("Length of string = ", len(str))

strWithSpaces = '  Hello Buddy    '
print("String after removing blank spaces from left side = ", strWithSpaces.lstrip())
print("String after removing blank spaces from right side = ", strWithSpaces.rstrip())
print("String after removing blank spaces from left and right side  = ", strWithSpaces.strip())

# Numbers are of 2 types -- int and float

intA = 10
floatA = 10.2
print("Int variable value = ", intA, "Float variable value = ", floatA)

# Lists  (Lists are mutable)
list = ['cd', 100, 2.23, 'john', 70]
tinylist = [123, 'wick']

print(list)  # Prints complete list
print(list[0])  # Prints first element of the list
print(list[1:3])  # Prints elements starting from 2nd till 4th
print(list[2:])  # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist)  # Prints concatenated lists

print("Index of john in list = ", list.index('john'))  ## Find index of a value in list
list.append('last object in list (appended)')  ## append method adds new values at end of list
list.insert(1, 'insert in list')  ## insert method inserts new values at mentioned index
print("List after using append and insert  methods = ", list)
list.remove(2.23)
print("List after removing a value = ", list)

## Lists can be sorted if it contains only numbers or only string values

disorderedList = [2, 19, -2, 3]
disorderedList.sort()
print("List in ascending order = ", disorderedList)
disorderedList.sort(reverse=True)
print("List in descending order = ", disorderedList)

# Sets

randomList = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 3, 2]
z = set(randomList)
print("Set with no duplicate values = ", z)

# Tupple (Tuples are immutable which means you cannot update or change the values of tuple elements.)

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # Prints complete list
print(tuple[0])  # Prints first element of the list
print(tuple[1:3])  # Prints elements starting from 2nd till 3rd
print(tuple[2:])  # Prints elements starting from 3rd element
print(tinytuple * 2)  # Prints list two times
print(tuple + tinytuple)  # Prints concatenated lists

# tuple[1] = 120    Error as tupple element cannot be updated
# print("Tuple value after updation = " , tuple[1])


# if-else flow (indentation is important)

var = 1000
if var > 900:
    print("Statement 1 after if condition is passed")
    print("Statement 2 after if condition is passed")
elif var > 800 and var < 900:
    print("Var value is bw 800 and 900")
else:
    print("Default statement")

## for loop ##
# quite similar to for each loop of Java

fruitsArray = ['apple', 'mango', 'banana']
for fruit in fruitsArray:
    print("Current fruit : = ", fruit)

# Print 0 to 9 using for loop (range function operates from 0 to n-1)
for num in range(10):
    print("Number from loop1 = ", num)

# Print 10 to 15 using for loop
for num1 in range(10, 16):
    print("Number from loop2 = :", num1)

# Print 5 to 0 using for loop
for i in range(5, -1, -1):
    print("Number from loop in reverse order = ", i)

# Print reverse string
userName = 'Adam Evans'
reverseUserName = userName[::-1]
print("String after reversing = ", reverseUserName)

### while loop ###
count = 0
while count < 4:
    print("The count is:", count)
    count = count + 1

### Converting data types ###

one = 10.0
print(one)
two = int(one)  # converts to int (similarly we can use float() and str() methods)
print(two)

### Dictionary (key value pair with unique keys, mutable datatype) ###
# Diff bw Lists and Dictionary -- Unlike lists, items in dictionaries are unordered.
# Because dictionaries are not ordered, they can’t be sliced like lists.

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict)
print("Name from dictionary = ", dict['Name'])  # accessing value via key
dict['Age'] = 8;  # update existing entry
dict['School'] = "DPS School";  # Add new entry
print(dict)

# Print all keys of dictionary
for i in dict.keys():
    print("Keys from dictionary = ", i)

# Print all values of dictionary
for j in dict.values():
    print("Values from dictionary = ", j)

# Print all keys and values of dictionary
for k in dict.items():
    print("Keys and values from dictionary = ", k)

print(dict.get('Age', 0))  # Value of age key is fetched
print(dict.get('College', 'IPU'))  # As College key is not in dict, default value 10 is fetched

# Generate random number from random module imported in class
r = random.randint(100, 300)
print("Random value generated is = ", r)

### Boolean values are True and False

print(2 > 1)  # print True
print(2 < 2)  # print False

## None value is a special value in python. Every method returns something. The methods that dont return anything return None ex print()

checkNone = print()
print("Value returned from print method = ", checkNone)

## bool() method is used to return or convert a value to a Boolean value
# bool() method returns False for only three values (known as Falsey values ) -- 0,0.0,''

print("Boolean value of 0 = ", bool(0))  # will return False
print("Boolean value of 10 = ", bool(10))  # will return True

## in and not in Operators of List (returns True / False)
students = ['Jas', 'Preet', 'Aman']
inValue = 'Jas' in students
print("in value returns = ", inValue)

notInValue = 'Jas' not in students
print("not in value returns = ", notInValue)

# String with in operator   (alternative of contains method of Strings in java)
collegeName = 'Harvard University Of England'
checkInValue = 'Harvard' in collegeName
print("in value used with string returns = ", checkInValue)

# Swapping variables
var1 = 10
var2 = 20
print("Before swapping values are = ", var1, " and ", var2)

var1, var2 = var2, var1
print("After swapping values are = ", var1, " and ", var2)


endTime = time.time()
print("Total time taken to execute script in seconds = ", (endTime - startTime))
