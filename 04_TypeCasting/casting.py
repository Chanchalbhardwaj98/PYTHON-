#Casting in Python

a=1
print(type(a))

b="1"
print(type(b))

c=int(b)
print(type(c))

print(a+int(b))
print(a+c)

# all string type can't be cast into numerical
# All numerical type can be cast into string
mynum=26
mynum2=str(mynum)

print(type(mynum2))
print(type(str(mynum)))

f1=22.55
print(type(f1))
print(type((int(f1))))

f2= int(f1)
print(type(f2))

in1=67
print(type(float(in1)))


# Implicit type casting- it performs auto,atically by python interpreter.
var1=10  #int type
var2=15.5  #float type
var3=var1+var2

print(var1+var2)
print(var3)
print(type(var3))

#Explicit type casting  performs manually by programmer using built in functions
int_num=101
str_num=str(int_num)
print(type(str_num))

#Boolean  0-Flase & 1-True
a0=bool(0)
print(a0)
print(type(a0))

a1=bool(1)
print(a1)
print(type(a1))