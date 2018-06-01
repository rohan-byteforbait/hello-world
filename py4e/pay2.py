hour= input("enter hours")
rate= input("enter hourly rate")
hour1= float(hour)
rate1= float(rate)
if hour1 <40.0:
    pay=hour1*rate1
    print(pay)
else:
    pay=(hour1-40)*rate1*1.5+40*rate1
    print(pay)
