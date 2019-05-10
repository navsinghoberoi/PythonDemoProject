# Import built in modules to use methods #

import random
import time

startTime = time.time()

# Print data
word = 'word'
line ="This is a line"
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

print("hello world!")
print("Word var value = "+word)
print("Line var value = " +line)
print("Paragraph var value = "+paragraph)


# Take user Input
name = 'Navpreet'
name = input("Enter user name : ")
print("\nName of the user = " +name)


# Strings
str = "Hello"
print(str[0])
print(str[0:2])
print(str[2:])
print(str + " concat")


# Lists
list = ['cd', 100 , 2.23, 'john', 70]
tinylist = [123, 'wick']

print(list)          # Prints complete list
print(list[0])       # Prints first element of the list
print(list[1:3])     # Prints elements starting from 2nd till 4th
print(list[2:])     # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist) # Prints concatenated lists


# Tupple (Tuples are immutable which means you cannot update or change the values of tuple elements.)

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)           # Prints complete list
print(tuple[0])        # Prints first element of the list
print(tuple[1:3])      # Prints elements starting from 2nd till 3rd
print(tuple[2:])       # Prints elements starting from 3rd element
print(tinytuple * 2)   # Prints list two times
print(tuple + tinytuple) # Prints concatenated lists

# tuple[1] = 120    Error as tupple element cannot be updated
# print("Tuple value after updation = " , tuple[1])


# if-else   (indentation is important)
var = 1000
if var>900:
    print("Statement 1 after if condition is passed")
    print("Statement 2 after if condition is passed")
elif var>800 and var<900 :
    print("Var value is bw 800 and 900")
else:print("Default statement")

#### for loop (similar to for each loop of java) ####
fruitsArray = ['apple','mango','banana']
for fruit in fruitsArray:
    print("Current fruit : = ", fruit)

# Print 0 to 9 using for loop (range function operates from 0 to n-1)
for num in range(10):
    print("Number from loop1 = ", num)

# Print 10 to 15 using for loop
for num1 in range(10,16):
    print("Number from loop2 = :",num1)


# Print 5 to 0 using for loop
for i in range(5,-1,-1):
    print("Number from loop in reverse order = ",i)


# Print reverse string
userName = 'Adam Evans'
reverseUserName = userName[::-1]
print("String after reversing = ",reverseUserName)

### while loop ###
count = 0
while count < 4:
   print("The count is:", count)
   count = count + 1


### Converting number data types (int , float, complex) ###

one=10.0
print(one)
two = int(one) # converts to int
print(two)


### Dictionary (key value pair with unique keys) ###

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict)
print("Name from dictionary = ", dict['Name']) # accessing value via key
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print(dict)


# Generate random number
r = random.randint(100,300)
print("Random value generated is = ",  r)

endTime = time.time()
print("Total time taken to execute script in seconds = " ,(endTime - startTime))

