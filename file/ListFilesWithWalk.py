# It gives you list of directories and files
from os import walk

f = []
d = []
for (dirpath, dirnames, filenames) in walk("/Users/bmoon/Downloads"):
    f.extend(filenames)
    d.extend(dirnames)
print(f)
print(d)
