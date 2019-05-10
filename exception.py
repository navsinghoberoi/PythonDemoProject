try:
    a = 2/0
except IOError:
    print("IO Exception is handled")
except :
    print("Generic exception code block is executed")
else:
    print("This statement is printed only when exception does not occurs")

print("Normal flow resumes")


######  Assertion  #######

try:
    assert 'Shuttl' == 'app', "Strings are not equal"
except AssertionError:
    print("Assertion exception is handled")
print("Next Line")