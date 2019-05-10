def epic():
    print("This is great method")


if __name__  == '__main__':
    print("This method prints where current file is not imported")   # This method is called only when this class (or method) is executed

else:
    print("This method prints only when module is imported")