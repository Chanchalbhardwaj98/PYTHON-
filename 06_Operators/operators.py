#operators

# 1. Arithmetic operators

a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# 2. Comparison operators - output is boolean (T/F)

a=5
b=3
print(a>b)
print(a<b)
print(a==b)
print(a!=b)

# 3. Assignment Operator
a=5   # = is assignment operator

# 4. Logical Operator
a=10
b=20
print(a>10 and b<10)  # and operator
print(a==10 or b<10) # or operator
print(a==10 or b==10)

print(not(a==10 and b == 20))

# 5. Identity operators - is, is not
x=[1,2,3]
y=x
z=[1,2,3]
print(x is y)
print(x is z)
print(x is not z)

# # 6. Membership operator- in, not in
my_list=['apple', 'orange', 'watermelon']
print('apple' in my_list)
print('orange' not in  my_list)

#.Bitwise operator- AND &, OR |, XOR^,  NOT~
a=5               # 5-  0101
b=3               # 3-  0011
print(a&b)        # 1-  0001

print(a|b)        # 7 - 0111