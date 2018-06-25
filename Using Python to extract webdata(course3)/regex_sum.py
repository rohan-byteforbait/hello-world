fhand=open("regex_sum_102136.txt")
l=list()
y=list()
k=0
import re
for line in fhand:
    y=y+re.findall("[0-9]+",line)
for h in y:
    k=k+float(h)
print(k)
