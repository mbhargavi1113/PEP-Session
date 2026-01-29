#custom errors

'''class LowBalanceError(Exception):
    #this line creates a custom exceptio named LowBalanceErroe
    #pass is used because class cannot be empty in python
    #we dont need to add any logic inside the cass right now
    pass
balance = 500
withdraw = int(input("enter amount: "))
if withdraw>balance:
    raise LowBalanceError("Insufficient Balance")
print("withdraw successful")'''

'''try:
    num=int(input("enter a number"))
    print(100/num)
except:
    print("error")'''

'''try:
    try:
        print(1/0)
    finally:
        print("inner finally")
except ZeroDivisionError:
    print("outer exception")
finally:
    print("outer finally")'''

'''def test():
    try:
        return 10
    finally:
        return 20
print(test())'''

'''try:
    try:
        x=int("abc")
    except ValueError:
        print("Inner handled")
        raise
except Exception:
    print("outer handled")'''

'''def test():
    try:
        return 10
    except:
        return 20
    else:
        return 30
print(test())'''

'''age = int(input("enter ur age"))
if age<18:
    raise ValueError("age must be 18 or above")
print("you are eligible")'''
          
'''num = int(input("enter a number:"))
#if number is negative, we usually raise an error
#python does not automatically treat negative number as wrong
if num = 0:
    raise ValueError("Num must bepositive")
print("you entered 
'''

'''print(True+True+False)
print("5"+"4")
print("5"*10)'''

'''def change(x):
    x+=10
a = 5
change(a)
print(a)'''

'''def update(lst):
    lst.append(10)
nums = [1,2,3]
update(nums)
print(nums)'''

'''t = (1,2,3)
t = t+(4,)
print(t)'''

'''s = {1,2,3,4}
print(len(s))'''

#move all zeros to the end
'''nums = [0,1,4,8,0,2,0]
result = []
zero_count = 0
for n in nums:
    if n==0:
        zero_count += 1
    else:
        result.append(n)
for i in range(zero_count):
    result.append(0)
print(result)'''


#check a string is palindrome or not
'''text = "naman"
left = 0
right = len(text)-1
isPalindrome = True
while left<right:
    if text[left]!= text[right]:
        isPalindrome = False
        break
    left += 1
    right -= 1
print(isPalindrome)
'''

#largest word in a sentence
'''sent = "Python makes problem solving fun"
words = sent.split()
longest = ""
for i in words:
    if len(i)>len(longest):
        longest = i
print(longest)'''

nums = [10,20,30,40,50]
slow = 0
fast = 0
while fast<len(nums) and fast+1<len(nums):
    slow+=1
    fast+=2
print(nums[slow])
