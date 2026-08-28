# square = lambda x: x**2
# print(square(5))

# multiply = lambda x,y,z :  x*y*z
# print(multiply(2,3,4))

# add = lambda a,b : a+b
# print(add(2,3))

# greet = lambda : "welcome!"
# print(greet())

# smallest = lambda x,y : x if x<y else y
# print(smallest(10,11))

# is_even = lambda a : a%2  == 0
# x = int(input("Enter a number: "))
# print(is_even(x))

# length = lambda s : len(s)
# print(length("saurabh"))

# upper =  lambda s : s.upper()
# print(upper("sauarbh"))

# start = lambda s : s.startswith("p")
# x = input("Enter a string :")
# print(start(x))

# average = lambda a,b,c : (a+b+c)/3
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = int(input("Enter third number: "))
# print(average(x,y,z))

# number = lambda x : "+ve" if x>0 else "-ve" if x<0 else "zero"
# x = int(input("Enter a number: "))
# print(number(x))

# def square(x):
#     return x*x

# number = [1,2,3,4,5,6,7,8,9]

# result = list(map(square,number))
# print(result)

# number = [1,2,3,4,5]

# result = list(map(lambda x:x*x,number))
# print(result)

# words = ["saurabh","python","programming","language"]
# result = list(map(lambda s:s.lower(),words))
# print(result)

# numbers_1 = [10,20,30,40,50]
# numbers_2 = [1,2,3,4,5]
# result = list(map(lambda x,y : x+y,numbers_1,numbers_2))
# print(result)   


# list_1 = [1,2,3]
# list_2 = [4,5,6]

# result = list(map(lambda x,y : x*y,list_1,list_2))
# print(result)

# word = ["python","java","c"]
# result = list(map(lambda s:len(s),word))
# print(result)


# word = ["hello","world"]
# result = list(map(lambda s:s.title(),word))
# print(result)

# number = [1,2,3,4,5,6]
# result = list(filter(lambda x:x%2==0,number))
# print(result)

# words = ["om","saurabh","hello","cat","krushnesh"]
# result = list(filter(lambda s:len(s)<3,words))
# print(result)

# a = int("20",4)
# print(a)

# number = [1,2,3,4,]

# result = filter(lambda x:x%2 == 0,number)
# print(next(result))
# print(next(result))

# i = 10
# while i>0:
#     print(i)
#     i-=1    

# name = ["Sauarbh","Sahadev","krushnesh","vrunda","sarthak"]
# result = list(filter(lambda s:s.lower().startswith("s"),name))
# print(result)

# string = ["Hi","Hello","","python"]
# result = list(filter(lambda s: s!="",string))
# print(result)

# number = [i for i in range(1,54) if i%3==0 and i%5==0]
# print(number)

# num = [i for i in range(1,54)]
# result = list(filter(lambda x:x%3==0 and x%5==0,num))
# print(result)

# fruits = ["apple","banana","kiwi","mango","grapes"]
# result = list(filter(lambda s: "a" in s, fruits))
# print(result)

# greater_number = [25,40,35,90,78,39]
# result = list(filter(lambda x:x>40,greater_number))
# print(result)

# n = 123
# count = 0
# while n>0:
#     digit = n%10
#     # print(digit)
#     n = n//10
#     count += 1
# print(f"Number of digits: {count}")

# employees = [
#     ("ram",25000),
#     ("shyam",30000),
#     ("sita",40000),
#     ("gita",35000)

# ]
# result = list(filter(lambda emp:emp[1]>30000,employees))
# print(result)

# i=1
# while i<=5:
#     print(i)
#     i-=1

# fruits = ["apple","banana","Mango"]
# for i in range(len(fruits)):
#     print(i,fruits[i])

# fruits = ["apple","banana","Mango"]

# for index,fruit in enumerate(fruits):
#     print(index,fruit)

# i = 1
# while i <= 10:
#     if i == 7:   # when i reaches 6
#         break        # stop the loop
#     print(i)
#     i += 1           # increment i

# i = 1
# while i <=10:
#     if i%6 == 0:
#         break
#     print(i)
#     i -= 1

# colours = ["red","green","blue","yellow"]
# result = list(enumerate(colours))
# print(result)

# names = ["A","B","C"]
# for index, name in enumerate(names,start= 1):
#     print(index,name)

# students = ["ram","shyam","mohan"]
# for index,name in enumerate(students,start=201):
#     print(index,name)

# numbers = [5,3,1,4,8]
# numbers.sort()
# print(numbers)

# employees = [
#     {"name":"rahul","salary":45000},
#     {"name":"Amit","salary":70000},
#     {"name":"saurabh","salary":55000}
# ]
# result = sorted(employees,key=lambda x:x["salary"])
# print(result)

# nums = [9,2,7,1,5]
# num = sorted(nums)
# print(num)

'''a=*
   b=**
   c=***
   d=****'''

import math

x = int(input("Enter the position: "))

n = math.ceil((math.sqrt(8 * x + 1) - 1) / 2)

alphabet = chr(96 + n)

print("The alphabet is:", alphabet)

# class Solution:
#     def validSequence(self, word1, word2):
#         n, m = len(word1), len(word2)
        
   
#         suffix_match = [-1] * (n + 1)
#         w2_idx = m - 1
#         for i in range(n - 1, -1, -1):
#             if w2_idx >= 0 and word1[i] == word2[w2_idx]:
#                 w2_idx -= 1
#             suffix_match[i] = w2_idx + 1


#         result = []
#         w2_idx = 0
#         changed = False 

#         for i in range(n):
#             if w2_idx == m:
#                 break
                
#             if word1[i] == word2[w2_idx]:
#                 result.append(i)
#                 w2_idx += 1
                
#             elif not changed and suffix_match[i + 1] <= w2_idx + 1:
#                 result.append(i)
#                 w2_idx += 1
#                 changed = True 


#             return result if len(result) == m else []


# number = [10,20,30,40]

# for num in number:
#     print(num)

# numbers = [10,20,30]

# it = iter(numbers)

# print(next(it))
# print(next(it))
# print(next(it))

# numbers = [10,20,30]

# it = iter(numbers)

# print(next(it))
# print(next(it))

# for x in it :
#     print(x)

# n = int(input("Enter your number")) 

# its_prime = True

# if n<=1:
#     print(f"{n} is not prime")

# else:
#     for i in range(2,int(n**0.5) + 1):
#         if n%i == 0:
#             its_prime = False
#             break

# if its_prime:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not  prime number")

# x = [1, 2, 3, 4, 5]

# result = [i * 2 for i in x if i % 2 == 1]

# print(result)

# numbers = [10,15,20,25,30,35,40]
# result = [i for i in numbers if i%5 == 0 and i%10!= 0]
# print(result)

# number = [1,2,3,4,5]
# result = {i:i*i for i in number }
# print(result)
# n=3
# for i in range(0,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n =4
# for i in range(4):
#     print("x",end="")

# class student:
#     def __init__(self):
#         print("constructure")
# student()
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"my name is {self.name}, i am {self.age} years old.")

# s1 = student("Rahul",20)
# s2 = student("Amit",21)

# s1.introduce()
# s2.introduce()

# names = ["sauarbh","sahadev","python"]
# uppercase = [name.upper() for name in names]
# print(uppercase)

# number = [10,20,30]
# it = iter(number)

# print(next(it))
# print(next(it))

# data = ["A","B","C","D"]

# it = iter(data)

# print(next(it))
# print(next(it))

# X = next(it)

# print(X)
# print(next(it))

# numbers = [10,20,30]

# it = iter(numbers)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("finished")
#         break

# numbers = [1,2,3]

# it = iter(numbers)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("finished")
#         break

