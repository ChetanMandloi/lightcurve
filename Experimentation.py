from os import listdir
from os.path import isfile, join
path = "/home/tachyon"
only_files = [f for f in listdir(path) if isfile(join(path, f)) if ".fits" in f]
print only_files