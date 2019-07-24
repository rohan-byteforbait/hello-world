fn=open("romeo.txt")
final=list()

i=1
new=list()
for line in fn:
    k=0
    ls=line.split()
    while k<len(ls):
        new.append(ls[k])
        k=k+1
final.append(new[0])
while i<len(new) and i>0:
    j=0
    while j>=0 and j<i:
        if new[i]==new[j]:
            i=i+1
            break
        elif new[i]!=new[j] and j!=i-1:
            j=j+1
            continue
        elif new[i]!=new[j] and j==i-1:
            final.append(new[i])
            i=i+1
            break

final.sort()
print(final)
