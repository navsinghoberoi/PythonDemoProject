def add_num(var1, var2, var3=10):
    sum_of_numbers = var1 + var2 + var3
    print("Sum of two numbers = ", sum_of_numbers)
    return sum_of_numbers


finalSum = add_num(10, 5.2)
print("Value returned from method = ", finalSum)

finalSum = add_num(10, 5.2, 2)
print("Value returned from method = ", finalSum)



eggs = 42
def spam():
    eggs = 10
    print(eggs)

print("Local variable value = " , end='')
spam()
print("Global variable value = ", eggs)