fhn=open('mbox-short.txt')
count=dict()
hourlist=list()
for line in fhn:
    words=line.split()
    if line.startswith("From "):
        time=words[5]
        times=time.split(":")
        hour=times[0]
        hourlist.append(hour)
for hrs in hourlist:
    for hr in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]:
        if hr==float(hrs):
            count[hrs]=count.get(hrs,0)+1

final=list()
final=count.items()
x=list()
x=sorted(final)
for k,v in x:
    print(k,v)
