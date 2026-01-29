#Abstraction
# class Payment:
#     def start(self):
#         print("Payment started")
#     def pay(self,amount):
#         pass
# class UPI(Payment):
#     def pay(self,amount):
#         print("Through UPI",amount)
# class Card(Payment):
#     def pay(self,amount):
#         print("Through card",amount)
# obj1 = UPI()
# obj1.start()
# obj1.pay(100)
# obj2 = Card()
# obj2.start()
# obj2.pay(200)


#Example of abstract and interface
class Course:
    def course_info(self):
        print("Course name is programming in python")
    def duration(self):
        pass
class Exam:
    def exam_type(self):
        pass
class Python_course(Course,Exam):
    def duration(self):
        print("Duration is 1 month")
    def exam_type(self):
        print("Practical Exam")
obj1 = Python_course()
obj1.course_info()
obj1.duration()
obj1.exam_type()


