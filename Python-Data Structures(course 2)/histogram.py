fhn=open("mbox-short.txt")
dic=dict()
maxvalue=None
maxkey=None
for line in fhn:
    words=line.split()
    if line.startswith('From '):
        dic[words[1]]=dic.get(words[1],0)+1
for key,value in dic.items():
    if maxvalue==None or value>maxvalue:
        maxvalue=value
        maxkey=key
print(maxkey,maxvalue)
