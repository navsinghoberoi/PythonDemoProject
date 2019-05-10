# Input a string from user and check if palindrome or not


def checkPalin():
    name = input("Enter a string to check it is palindrome or not")
    revName = name[::-1]    # this method gets reverse of string (or a list)

    if revName == name:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")


checkPalin()