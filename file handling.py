# file = open("data.txt","mode->r,w,a")
'''file = open("students.txt","w")
file.write("Name: Rahul \n")
file.write("Course: Python \n")
file.close()'''

'''file = open("students.txt","r")
data = file.read()
print(data)
file.close()'''

'''with open("students.txt","r") as file:
    data = file.read()
    print(data)'''

'''file = open("students.txt","a")
file.write("marks: 90\n")
file.close()
with open("students.txt","r") as file:
    data = file.read()
    print(data)'''

'''file = open("students.txt","r")
data2 = file.readlines()
print(data2)'''

'''file = open("data.txt","w")
file.write("Name: Bhargavi \n")
file.write("City: Hyd \n")
file.write("Age: 20 \n")
file.close()'''

'''file = open("data.txt","r")
data = file.read()
print(data)
file.close()'''

'''file = open("data.txt","r")
data1 = file.readlines()
print(data1)
file.close()'''

'''data1 = file.readlines()
print(len(data1))'''

'''file = open("my file.txt","w")
file.write("my name is bhargavi")
file.close()'''

'''file = open("my file.txt","r")
data4 = file.read()
print(data4)
file.close()'''

'''file = open("my file.txt","r")
data4 = file.read()
print(data4.upper())
file.close()

print("characters in the file: ",len(data4))
file.close()'''

'''file = open("my file.txt","r")
data4 = file.read()
count=data4.lower().count("bhargavi")
print("word count: ", count)
file.close()'''

'''file = open("my file.txt", "r")
data4 = file.read()
data4.replace("bhargavi","varsha")
print(data4)
file.close()'''


'''file = open("movies.txt","w")
file.write("kgf\n")
file.write("salaar\n")
file.write("spirit\n")
file.close()

file = open("movies.txt","r")
data = file.read()
print(data[:10])
file.close()'''

'''file = open("movies.txt","r")
data = file.read()
print(data.replace("salaar","rrr"))
file.close'''

'''file = open("movies.txt","r")
data = file.read()
words = data.split()
for w in words:
    print(w[::-1])
file.close()'''


try:
    #risky code
except:
    #error handling code

try:
    a = int(input("enter 1st number"))
    b = int(input("enter 2nd number"))
    print(a/b)
except:
    print("error occurred!!!")

try:
    file = open("movies.txt","r")
    print(file.read())
except:
    print("file is not found")
finally:
    print("program ends")
