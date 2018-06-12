# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for lx in fh:
    ln=lx.strip()
    l1=ln.upper()
    print(l1)
