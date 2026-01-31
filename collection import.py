""" from collections import Counter """
#ex:1
# Fruits = ["banana","apple","banana","papaya","mango","banana"]
# count = Counter(Fruits)
# print(count)

#ex:2
# sentence = "Python is easy and python is powerful"
# words = sentence.split()
# word_count = Counter(words)
# print(word_count)

#ex:3
# num = [1,2,3,4,5,2,3,1,4,2,2,1,3,4]
# count = Counter(num)
# print(count)
import os

#ex: current path
# current_path = os.getcwd()
# print(current_path)

#ex: current directory
# item = os.listdir()
# print(item)

#ex: new folder
# folder_name = "MyFolder"
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
#     print("folder created successfully")
# else:
#     print("folder is already present")