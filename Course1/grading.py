marks= input("enter marks between 0 and 1.0: ")
try:
    marks1=float(marks)
except:
    print("enter numeric marks")
    quit()
if marks1>=0.9:
    print("A")
elif marks1>=0.8:
    print("B")
elif marks1>=0.7:
    print("C")
elif marks1>=0.6:
    print("D")
else:
    print("F")
