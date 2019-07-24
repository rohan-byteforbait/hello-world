fname=input("enter your file name:")
fn=open(fname)
ls=list()
count=0
for line in fn:
    if line.startswith('From '):
        ls=line.split()
        print(ls[1])
        count=count+1
    else:
        continue
print(count)
