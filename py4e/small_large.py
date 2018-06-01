largest =None
smallest=None
while True:
    num= input("enter a number: ")
    if num=="done":
            break
    try:
        num1=float(num)
        if largest==None :
            largest=num1
        elif num1>largest:
            largest=num1
        if smallest==None:
            smallest=num1
        elif num1<smallest:
            smallest=num1
    except:
        print("invalid input")
        continue
print(largest,smallest)
