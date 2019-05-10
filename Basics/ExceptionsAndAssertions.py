#### Handling Exceptions ####

try:
    a = 2/0
except IOError:
    print("IO Exception is handled")
except :
    print("Generic exception code block is executed")
else:
    print("This statement is printed only when exception does not occurs")

print("Normal flow resumes")

# Raise an exception and print stack trace

import traceback

try:
    raise Exception("Raising an exception to check stack trace")
except :
    print("Stack trace of the exception = \n",traceback.format_exc())


######  Assertion  #######

# When result of assertion is false, exception is thrown! So need to handle exception

try:
    assert 'Shuttl' == 'app', "Strings are not equal"
except AssertionError:
    print("Assertion exception is handled")
print("Next Line")



a = 'open'
assert a == 'open'