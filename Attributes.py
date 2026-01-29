#Attributes
# class Student:
#     collage_name = "LPU"
#     def __init__(self,Fullname,marks):
#         self.name = Fullname
#         self.marks = marks
# S1 = Student("Rahul",86)
# S2 = Student("Karan", 63)
# print(S1.name)
# print(S2.name)
# print(S1.collage_name)
# print(S2.collage_name)
    
# class Car:
#     def __init__(self,model,price):
#         self.name = model
#         self.price = price
# C1 = Car("Audi",1500000)
# C2 = Car("BMW",2000000)
# print(C1.name,C1.price)
# print(C2.name,C2.price)

# class Student:
#     college_name = "LPU"
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
# S1 = Student("Rahul",86)
# S2 = Student("Karan", 63)
# #before changing the college name 
# print(S1.name,S1.marks,S1.college_name)
# print(S2.name,S2.marks,S2.college_name)
# #after changing the college name using class
# Student.college_name = "IIT"
# print(S1.name,S1.marks,S1.college_name)
# print(S2.name,S2.marks,S2.college_name)

# class Employee:
#     def __init__(self,emp_name,emp_salary):
#         self.name = emp_name
#         self.salary = emp_salary
# E1 = Employee("Rahul", 763000)
# E2 = Employee("Jiya",10000000)

# class Student:
#     total_students = 0
#     def __init__(self,name):
#         self.name = name
#         Student.total_students += 1 #increase count when object is created
# s1 = Student("Rahul")
# s2 = Student("karan")
# s3 = Student("Anita")
# print("total no of students:",Student.total_students)

# class Student:
#     def __init__(self,name):
#         self.name = name
#     def hello(self):
#         print("Welcome",self.name)
# s1 = Student("rahul")
# s1.hello()

# class Student:
#     def __init__(self,name):
#         self.name = name
#     def hello(self):
#         print("welcome",self.name)
#     @staticmethod
#     def college_name():
#         print("This is LPU")
# s1 = Student("Rahul")
# s1.hello()
# s1.college_name()


#method
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)
# s1 = Student("rahul",98)
# s1.display()

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def hi(self):
#         print("welcome", self.name, "your marks are: ",self.marks)
#     @staticmethod
#     def college_name():
#         print("this is lpu")
# s1 = Student("bhargavi",89)
# s1.hi()
# s1.college_name()

        

        