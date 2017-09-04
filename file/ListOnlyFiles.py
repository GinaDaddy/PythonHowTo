from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("/Users/bmoon/Downloads") if isfile(join("/Users/bmoon/Downloads", f))]
print(onlyfiles)
