# Lambda function (func without any name, usually 1 liner functions)

lambdaMultiply = lambda x, y: x * y
print("Value computed using lambda method = ", lambdaMultiply(4, 5))

# Another way of implementing lambda functions:
print((lambda x, y: x * y)(4, 5))


# *args (used to pass variable number of arguments to a function)
def sumWithArgs(*args):
    s = 0
    for i in args:
        s += i

    print("Sum of the numbers = ", s)


sumWithArgs(1, 2, 3)
sumWithArgs(5, 4)
sumWithArgs(2, 3, 4, 5, 6)


# **kwargs (allows us to pass variable number of keyword argument)


def my_func(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


my_func(name='tim', sport='football', roll=19)
my_func(name='nav', sport='badminton')

# Compute count of each character in a word
from collections import Counter

str1 = 'abcdababaa again'
print("Counter of string 1 = ", Counter(str1))

# Reduce (Reduce is a function that turns an iterable into one thing, consists of function and iterable entity)
from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print("Reduce function output = ", product)

# Filter (Function to filter out things from iterable that user dont want in that iterable, consists of function and iterable entiity)

whole_range = range(-5, 5)
all_less_than_zero_values = list(filter(lambda varFilter: varFilter < 0, whole_range))

print("Filter function output = ", all_less_than_zero_values)

# List Comprehensions (A list comprehension is a way to generate lists in Python)

lc = range(-5, 5)
lc_all_greater_than_zero = [num for num in lc if num > 0]

lc_square_all_greater_than_zero = [num * num for num in lc if num > 0]

print("Numbers greater than 0 from list = ", lc_all_greater_than_zero)

print("Square of every number greater than 0 from list = ", lc_square_all_greater_than_zero)

# Zip ( It takes n number of iterables and returns list of tuples)

list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']

iterator1 = zip(list_a, list_b)  # It returns an iterator
zipped_list = list(iterator1)  # Converting iterator to list
print("Zipped list of given 2 lists = ", zipped_list)

# emoji
from emoji import emojize

print(emojize(":thumbs_up:"))

# To generate uuid
import uuid

for i in range(1, 4):
    print(uuid.uuid4())

# Map  (It applies a function to all the items in an input_list, generally used with lambda)
x = [1, 2, 3]
y = map(lambda x: x + 1, x)  # prints out [2,3,4]
print("Result of using map method = ", list(y))

# Plot graphs
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('Experience')
plt.xlabel('Knowledge')
plt.title('Experience vs Knowledge')
## plt.show()     uncomment to see plot


# Using shell commands
from subprocess import call

print("Present working directory = ")
call("pwd")
print("List of files and folders in current directory = ")
call("ls")
# call(["mkdir" ,"folderName"])

print("\n\n\n\n\n\n")
call("alias")
# call(["jump"])





from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])
