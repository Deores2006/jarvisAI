# # sum = 0
# # n = int(input("enter the number: "))
# # for i in range(0, n+1,2):
# #     sum += i
# # print(sum)
# # sum = 0
# # i = 0
# # j = 0
# # for i in range (1,5):
# #     for j in range(i):
# #         sum += j
# #     print("*")
# # i = 1
# # for i in range(5):
# #     print("*",i)
# #
# #     for j in range(i):
# #         print("*",j)
# #
# # # n = 5
# # for i in range(0,n):
# #     for j in range(0,i):
# #         print("*",end=" ")
# #     print()
# #
# # for i in range(n-1,0,-1):
# #     for j in range(i):
# #         print("*",end=" ")
# #     print()
# #
# # n = 5
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #     print()
# #
# #
# # n = 5
# # for i in range(1,n+1):
# #     print(i,end=" ")
# #     for j in range(1,i):
# #         print(i,end=" ")
# #     print()
# #
# #
# # a = 10
# # b = 20
# #
# # x = a
# # a = b
# # b = x
# # print(a)
# # print(b)
# #
# # fruits = ["apple", "banana", "cherry"]
# # print(fruits[1])
# # print(fruits[-2])
# #
# # numbers = [1,3,0,5,6]
# # numbers.sort()
# # print(numbers)
# #
# # fruits = ["apple", "banana", "cherry"]
# # for fruits in fruits:
# #     print(fruits)
# #
# # students = ("sauarbh",2006,"artificial")
# # for students in students:
# #     print(students)
# #
# # a = [1,2,3,4]
# # b = a.copy()
# # b.append(5)
# # print(a)
# # print(b)
# #
# # student = {
# #     "name" : "saurabh",
# #     "roll no." : 19,
# #     "branch" : "machanical"
# # }
# # del student["roll no."]
# # print(student["name"],student["roll no."],student["branch"])
# #
# # student = {
# #     "class A":{
# #     "name" : "saurabh",
# #     "roll no." : 19,
# #     "branch" : "machanical"
# # },
# #     "class B":{
# #     "name" : "sahadev",
# #     "roll no." : 29,
# #     "branch" : " advance machanical"
# # }
# # }
# #
# # print(student["class B"]["branch"])
# #
# # def add(a,b):
# #     return a+b
# # result = add(10,20)
# # print(result)
# #
# # def square(n):
# #     return n*n
# # m = int(input("Enter a number: "))
# # print(result)
# # result = square(m)
# #
# # def hello(n):
# #     if n == 0:
# #        return
# #
# #     print("Hello")
# #     hello(n-1)
# #
# # hello(2)
# #
# # def factorial(n):
# #     if n== 0:
# #         return 1
# #     else:
# #         return n*factorial(n-1)
# # n = int(input("Enter a no. :- "))
# # print(f"the factorial of no. is {factorial(n)}")
# #
# # s = "\nhey how are you"
# # f = open("demo.txt","r")
# # f.write(s)
# # f.close()
# #
# # with open("demo.txt","r") as f:
# #      text = f.read()
# #
# # print(text)
# #
# #
# # f = open("poem.txt","r")
# # text = f.read()
# # if "twinkle" in text:
# #     print("present")
# # else:
# #     print("not present")
# #
# # f.close()
# #
# # f = open("demo.txt", "r")
# # text = f.read()
# #
# # if "twinkle" in text.lower():
# #     print("Present")
# # else:
# #     print("Not Present")
# #
# # f.close()
# #
# #
# # import os
# #
# # folder_name = "Tables"
# #
# # if not os.path.exists(folder_name):
# #     os.mkdir(folder_name)
# #
# # for i in range(2,20):
# #
# #     file = open(f"{folder_name}/Table_{i}.txt","w")
# #
# #     for j in range(1,11):
# #         file.write(f"{i}*{j} = {i*j}\n")
# #
# #     file.close()
# #
# # print("all tables are created successfully")
# #
# #
# file = open("xyz.txt","r")
# y =file.read()
# file.close()

# y = y.replace("#####","donkey")
# word = "donkey"
# convert = y.lower()
# count = convert.count(word)
# print(f"the word donkey is used {count} times ")
# file = open("xyz.txt","w")
# file.write(y)
# file.close()
# #
# # class student:
# #     pass
# # s1 = student()
# # s1.name = "saurabh"
# # s1.age = 20
# # print(s1.name)
# # print(s1.age)
# #
# # class student:
# #     def __init__(self,name,marks,rank):
# #         self.name = name
# #         self.marks = marks
# #         self.rank = rank
# #
# # s1 = student("sahadev",108,"1st")
# # s2 = student("saurabh",100,"2nd")
# # print(s1.name,s1.marks,s1.rank)
# # print(s2.name,s2.marks,s2.rank)

# class employee:
#     company = "ITC"
#     def show(self):
#         print(f"the employee is {self.name} and the salary is {self.salary}")

# # class programmer:
# #         company = "ITC innfotech"
# #         def show(self):
# #             print(f"the name is {self.name} and he is good with {self.salary}")
# #
# #         def showlanguage(self):
# #             print(f"the is {self.name} and he is good with {self.company} language")

# class programmer (employee):
#     company = "ITC infotech"
#     def showlanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language")
# a = employee()
# b = programmer()

# print(a.company,b.company)

# from math_package.add import add
# from math_package.multiply import multiply

# x = int(input("Enter 1st number :- "))
# y = int(input("Enter 2nd numebr :- "))

# print(f"the sum of numbers is {add(x,y)}")
# print(f"the multiplication of this numbers is {multiply(x,y)}")

# def reverse_string(s):
#     return s[::-1]

# n = input("Enter a string:-")
# print(f"the reverse of strinng is {reverse_string(n)}")

# square =[]

# for i in range(1,5):
#     square.append(i*i)

# square.append(25)
# print(square)

# def new_func():
#     square = [i*i for i in range(1,5)]
#     square.append(25)
#     print(square)

# new_func()

# evens = []
# for i in range(1,11):
#     if i%2 == 0:
#         evens.append(i)
# print(evens)

n  = [2,7,11,15,6,3,4,5,12]

x = 9
for i,num1 in enumerate(n):
    for j,num2 in enumerate(n):
        if num1 + num2 == 9:
            print(f"[{i},{j}]")