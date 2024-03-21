#1. Decisions at the Crossroad
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif  number == 0:
   print("The number is zero.")
else:
    print("The number is negative.")

#2. The Greatest Showdown
    #Task 1: Identify the Greatest
x = int(input("Give me the first number:"))
y = int(input("Give me the second number:"))
z = int(input("Give me the third number:"))

if x > y and x > z:
    print("the greatest number is", x)
elif y > x and y > z:
    print("the greatest number is", y)
else:
    print("the greatest number is", z)
    
    #Task 2: Identify the Smallest
if x < y and x < z:
    print("the smallest number is", x)
elif y < x and y < z:
    print("the smallest number is", y)
else:
    print("the smallest number is", z)

#Task 3: Equality Check3
if x==y==z:
    print("All numbers are equal")
elif x==y:
    print("the first number,",x,",and the second number,", y, ",are both equal")
elif x==z:
    print("the first number,",x,",and the third number,", z, ",are both equal")
elif y==z:
    print("the second number,",y,",and the third number,", z, ",are both equal")
#I think (2.the greatest showman) could've been done in a shorter version. ^ 

#3. Leap Year Explorer
#Task 1: Leap Year Checker
leap_year = int(input("Find out whether or not your year input is a leap year, input a year:"))
if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
    print("this is a leap year!")
else:
    print("this is not a leap year.")

#having trouble with divisible, come back to (3.leap year checker).^