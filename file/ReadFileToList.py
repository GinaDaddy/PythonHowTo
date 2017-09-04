f = open("/Users/bmoon/git/PythonHowTo/resources/test.txt", "r")

myList = []

for line in f:
    myList.append(line)

print(myList)
f.close()