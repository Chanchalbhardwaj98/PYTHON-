# Conditional statements  in python

# 1. If statement- it only works for true conditions

a=26
b=108
if b>a:
    print("b is greater than a ")
    
age = int(input("Enter your age: "))
if age>19:
    print("you are an adult")

# print(10>100)  o/p- False

# 2. If-else statement- it works for both T&F conditions

age=int(input("Enter your age:  "))
if age>19:
    print("You are an adult")
else:
    print("You are not an adult")


temp=45
if temp<30:
    print("It's a cool day ")
else:
    print("It's a hot day ")