#1>add two nubers 
#step1 = static addition
a=15
b=20
print(a+b)
#step2=dynamic addition
a=int(input("enter the first number:"))#type_casting
b=int(input("enter the second number:"))
sum=a+b
print("sum of two numbers: ",sum)

#2>How to find the Average of 2 Entered Numbers on Python?
a=int(input("enter the first number:"))#type_casting
b=int(input("enter the second number:"))
avarage=(a+b)/2
print("avarage of two numbers:",avarage)


#3>How to show the Class Pass Status (PASSED — FAILED) of the Student whose Written Average Has Been Entered on Python?

#step1:avarage is given
average = 25
if average < 25:
    print("fail")
else:
    print("pass")

#step2:average is user given
average = float(input("enter the average:"))
if average < 25:
    print("fail")
else:
    print("pass")

#step3 combination
a=float(input("enter the first number:"))#type_casting
b=float(input("enter the second number:"))
average=(a+b)/2
print("average of two numbers:",average)
if average<25:
    print("fail")
else:
    print("pass")








