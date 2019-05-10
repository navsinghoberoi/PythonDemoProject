import os

for filename in os.listdir("/Users/navpreetsingh/PycharmProjects/try/Basics/folder"):
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)