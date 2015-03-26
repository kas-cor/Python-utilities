import os
import sys

num=0
folders=0
files=0
task=[]

def show_all(sSrc,folders,files):
    for file in os.listdir(sSrc):
        file=os.path.join(sSrc,file)
        if os.path.isdir(file):
            task.append(file)
            print file
            folders+=1
            folders,files=show_all(file,folders,files)
        else:
            files+=1
    return folders,files

for path in sys.argv[1:]:
    folders,files=show_all(path,folders,files)

print "=============="
print "Total folders: %d" % folders
print "Total files: %d" % files
print

task.reverse()
for path in task:
    new=path.split("\\")
    old=new.pop()
    if not old.isdigit():
        new.append(str(num))
        num+=1
        to="\\".join(new)
        print path+" to "+to
        os.rename(path,to)
