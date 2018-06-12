fn=input("enter file name: ")
fh=open(fn)
count=0
textfl=0.0
for lx in fh:
    if lx.startswith("X-DSPAM-Confidence:"):

        count=count+1
        textpos=lx.find(":")
        textfx=float(lx[textpos+1:])
        textfl=textfl+textfx
    else:
        continue
#print(count)
print("average span Confidence: ",textfl/count)
