#composition
# class Address:
#     def __init__(self,city):
#         self.city = city
#     def show_address(self):
#         print("City:",self.city)
# #student class
# class Student:
#     def __init__(self,name,city):
#         self.name = name
#         #composition:
#         #creating object of address class inside student class
#         self.address = Address(city)
#     def show_student(self):
#         print("Name:",self.name)
#         #using object of another class 
#         self.address.show_address()
# s = Student("karan","Delhi")
# s.show_student()


class Engine:
    def start(self):
        print("Engine Started")
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()
        print("car is moving")
c = Car()
c.drive()

