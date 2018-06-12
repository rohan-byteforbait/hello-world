fname=input("enter the file name : ")
fn=open(fname)
lc=list()
for lst in fn:
    lnls=lst.split()
    #print(lnls)
    lc=lnls+lc
lc.sort()
count=1
while count!=0:
    count=0
    for i in range(len(lc)):
        if i>0 and i<len(lc)-1 and lc[i]==lc[i-1]:
            lc[i]=lc[i+1]
            count=count+1
        elif i==len(lc)-1 and lc[i]==lc[i-1]:
            lc=lc[0:len(lc)-1]
        elif i==0:
            continue
print(lc)
