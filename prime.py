def is_prime():

    number = int(input("Enter number to check if prime : "))

    if number > 1:
        for i in range(2, number):
            if (number % i == 0):
                print(number, " is not a prime number")
                break                                  ## code working changes after removing indentation of break
        else:
            print(number, " is a  prime number")

    else:
        print("Enter number greater than 1")

# Call method
is_prime()
