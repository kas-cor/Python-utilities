import os

num=0
task=[]

def show_all(sSrc):
    for file in os.listdir(sSrc):
        file=os.path.join(sSrc,file)
        if os.path.isdir(file):
            task.append(file)
            print file
            show_all(file)

show_all("E:\\Projects\\gulp-skeleton")

print "=============="

task.reverse()
for path in task:
    new=path.split("\\")
    old=new.pop()
    if len(old)>3:
        new.append(str(num))
        num+=1
        to="\\".join(new)
        print path+" to "+to
        os.rename(path,to)
