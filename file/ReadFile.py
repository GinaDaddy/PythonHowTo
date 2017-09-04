# f = open("../../resources/test.txt", "r")
f = open("/Users/bmoon/git/PythonHowTo/resources/test.txt", "r")

# Read one line
print(f.readline())

# Print all of them in one line. New line is represented as \n.
# print(f.readlines())

f.close()