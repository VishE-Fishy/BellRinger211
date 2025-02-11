import datetime
now = datetime.datetime.now()


l = int(input("What is the current date in the month(number): "))
m = int(input("what is the current hour of the day: "))
timel = 14 - l
hoursp = (timel*24) - m

print(hoursp)
