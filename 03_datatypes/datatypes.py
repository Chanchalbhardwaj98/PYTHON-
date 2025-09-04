# Data types in python

a=1
b=2
print(a+b)

c="1"
d="2"
print(c+d)

print(type(a+b),type(c+d)) #checking datatype int & string

#Basic Datatypes in python:

# 1. Numeric
a1 = 1
a2 = 1.5
print(type(a2)) #float

a3 = complex(3,5) #real,imaginary
print(a3)
print(type(a3))

# 2. Sequence
b1 = "Madhav" #2a. string
print(type(b1)) 

b2=[1,4,5,6,8,0,98,23,'chanchal'] #2b. list
print(type(b2))
 
b3 = (1,4,5,6,8,0,98,23,) #2c. tuple
print(type(b3))

# 3. Dictionary-  key-value pair
my_dictionary={'name': 'Chnachal', 'age': 26, 'city':'bulandshahr'}
print(my_dictionary)
print(type(my_dictionary))

# 4. Sets: combinations of elements and objects
my_sets = {1,4,5,6,8,0,98,23,'chanchal'}
print(my_sets)
print(type(my_sets))

# 5. Boolean: True or False
bool1= True
bool2= False
print(type(bool),type(bool2))

# 6. Binary
# bytes, bytearray, memoryview
byte1=b"chanchal"
print(byte1)
print(type(byte1))