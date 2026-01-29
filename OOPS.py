#OOPS 
#Encapsulation
# class Student:
#     def __init__(self,marks):
#         self.__marks = marks
# s1 = Student(100)
# print(s1.marks)

#Abstraction
# class Student:
#     def __init__(self,marks):
#         self.__marks = marks
#     def get_marks(self):
#         return self.__marks
# s1 = Student(100)
# print(s1.get_marks())

#create a class bank where the balance is hidden and we have to access bank
# class Bank:
#     def __init__(self,balance):
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
# b1 = Bank(5000)
# print(b1.get_balance())


# class Student:
#     def __init__(self,marks):
#         self.__marks = marks
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,new_marks):
#         self.__marks = new_marks
# s1 = Student(100)
# s1.set_marks(80)
# print(s1.get_marks())

class Bank:
    def __init__(self,balance):
        self.balance = balance
    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("insfficient balance")
    def deposit(self,amount):
        self.__balance += amount
acc = Bank(5000)
acc.deposit(1000)
print(acc.get_balance())
        
    
    
    


