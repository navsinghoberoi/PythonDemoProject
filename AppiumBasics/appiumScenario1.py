from AppiumBasics.Setup import Setup


class Scenario1(Setup):
    def __init__(self):
        print("Creating object of current class")


obj1 = Scenario1()

# Calling setup method of parent class  (First scenario of every test)
driver = obj1.setup_android_session(True)
# Calling quit method to close session
driver.quit()
print("Driver session has been closed")
