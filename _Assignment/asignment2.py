#Q1. WAP to print input student name and marks of 3 students
# print name and marks and percentage

# name1=input("Enter the name of student 1: ")
# marks1=input( "hindi marks: ")
# marks2=input( "eng marks: ")
# marks3=input( "maths marks: ")

# #calculate % 
# percentage=(((int(marks1)+int(marks2)+int(marks3))/300)*100)
# print(percentage)

# #print result
# print(f"The result of {name1} is {percentage}% . Well done! ")

# #Optimized solution

# print("Percentage calculator")

# name1=input("Enter the name of student 1: ")
# marks1=int(input( "hindi marks: "))
# marks2=int(input( "eng marks: "))
# marks3=int(input( "maths marks: "))

# #calculate % 
# percentage=(((marks1)+(marks2)+(marks3))/300)*100
# print(percentage)

# #print result
# print(f"The result of {name1} is {percentage}% . Well done! ")

#Q2. WAP that collects multiple types of data( eg. name, age, height, & student status) from user input, s
# stores them in a dictionary, and then prints out the collected data?

# initializing a dictionary
user_data={}

# input from user
user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['student'] = input("Are you a student (yes/no): ")

# print the input from user
print(user_data)





