import os

print(os.getcwd())   # current working dir
# os.chdir('C:\\Windows\\System32')   # changing dir

# create dir
try:
    os.mkdir('/Users/navpreetsingh/PycharmProjects/try/Basics/folder')
except FileExistsError:
    print("Directory is already created")


# Get absolute / relative paths
print("Absolute path = ",os.path.abspath('./folder'))
print("Relative path = ",os.path.relpath('./folder'))


# Get file size and folder contents

# print("Size of file = ",os.path.getsize('/Users/navpreetsingh/PycharmProjects/try/Basics/BeginnerConcepts.py'), "Bytes")

dirContents = os.listdir('/Users/navpreetsingh/PycharmProjects/try/Basics')
print("Contents of the directory are = ",dirContents)
totalSize = 0
for i in dirContents:
    sizeOfFile = os.path.getsize(i)
    print("Size of file" ,i , "is = " ,sizeOfFile, "Bytes")
    totalSize += sizeOfFile

print("Total size of all files present in the folder = " ,totalSize , "Bytes")



# Read / Write files
fileObject = open("/Users/navpreetsingh/PycharmProjects/try/Basics/folder/hello.txt")
fileContent = fileObject.readlines()
print("Content read from the file before appending = ",fileContent)

fileObject.close()

# Cant write to file because file opened in read only mode by default
#fileContent = fileObject.write("This line is Written using program")

# Open file in write mode to write in file (Pass second param as 'a' to append and 'w' to overwrite existing contents)

fileObject1 = open("/Users/navpreetsingh/PycharmProjects/try/Basics/folder/hello.txt",'a')

fileContent1 = fileObject1.write("\nLine written via program")
fileObject1.close()

fileObject2 = open("/Users/navpreetsingh/PycharmProjects/try/Basics/folder/hello.txt")
content = fileObject2.readlines()
fileObject2.close()
print("Content read from the file after appending text = ",content)