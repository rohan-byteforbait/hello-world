def computepay(h,r):
    if h>40:
        pay=(h-40)*r*1.5+40*r
        return pay
    else:
        pay=h*r
        return pay
hr=input("enter hours:")
h= float(hr)
rate=input("enter rate:")
r=float(rate)
print(computepay(h,r))
