#Diamond Problem
class A:
    def message(self):
        print("this is message from class")
class B(A):
    def message(self):
        print("this is message from class B")
class C(A):
    def message(self):
        print("this is message from class c")
class D(B,C):
    def message(self):
        print("this is message from class D")
obj = D()
obj.message()