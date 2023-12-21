# print("Hello world")

# name = "KIRTI"
# for i in name:
#     print(i , end =",")

# n = input("Enter your name ")

# j = int(input("Enter a digit "))

# print("Your name is", n + " digit is", j)


# i = 6
# while (i < 5):
#     print(i, end = ",")
#     i = i + 1
# else :
#     print("Loop done")

# i = int(input("Enter a digit "))
# if(i < 10):
#     print(i)
# elif (i == 15):
#     print(i)
# else : 
#     print("oops")

# x = 1
# match x:
#     case 0:
#         print("Not matched")
#     case 4:
#         print("Matched")
#     case _ :
#         print("Oppppppsssss")

# for i in range(12):
#     if(i == 10):
#         break
#     print(i , end=",")

# friend = "Noob"
# afriend = 'Noobi'
# print(friend + " " + afriend)

# use = 'Sorry, "I am late"'
# use1 = "Sorry, \"I am late\""
# use2 = "Sorry'"
# use3 = 'Sorry\''
# print(use1)

# print(use2 + " " + use3)
# apple = """
# I am an apple
# Thanks to eat me
# I love you
# """
# print(apple)

# banana = '''
# I am an banana
# Thanks to eat me
# I love you
# '''
# print(banana)

# name = "KIRTI"
# length = len(name)
# print(length)
# print(name[0:4])
# print(name[:5])
# print(name[:6])
# print(name[0:-4])
# print(name[:-4])
# print(name[-1:-3])  # Don't print anything
# print(name[-3:-1])
# nm = "Harry"
# print(nm[-4:-2])

# Strings are immutable
# name = "!!Kirti!!!"
# x = "I'm a girl also I am a student, I am a child too"
# print(name.endswith("!!"))
# print(name.endswith("!!",4, 9))
# print(name.endswith("!!!",4, 9))
# print(name.endswith("!!",4, 8))
# print(name.endswith("!!!",4, 10))
# print(name.find("i"))
# print(x.find("am"))
# print(x.index("am"))
# print(name.endswith("!!!!"))
# n = "kirti ....... ki"
# print(n.count("ki"))
# print(name.upper())
# print(name.lower())
# print(name)
# print(name.rstrip("!!!")) #only trailing !
# print(n.replace("ki", "Hi"))
# print(n.split(" "))
# print(name.split("!"))

# heading = "introduction to js"
# heading1 = "introductiOn To jS"
# print(heading.capitalize())
# print(heading1.capitalize())
# print(heading1.center(100))
# print(heading1.center(100, ","))
# print(len(heading1))
# print(len(heading1.center(100, ",")))

# str1 = "rwetyduibojwdiodhfhvcbjnSDFTYYT93873"
# str2 = "xcvhjhgfdfghAGH\n"
# str3 = "xcvhjhgfdfghAGH"
# str4 = "    "
# str5 = "       "
# str6 = "  huji     "
# str7 = "I am a girl"
# print(str1.isalnum())
# print(str1.isalpha())
# print(str1.isascii())
# print(str1.isdigit())
# print(str1.isdecimal())
# print(str1.islower())
# print(str1.isupper())
# print(str1.isnumeric())
# print(str2.isalpha())
# print(str3.isalpha())
# print(str1.isprintable())
# print(str2.isprintable())
# print(str4.isspace())
# print(str5.isspace())
# print(str6.isspace())
# print(str3.istitle())
# print(str3.swapcase())
# print(str3.startswith("xcvh"))
# print(str7.title())

# python list
# list1 = [1,2,4,7,9,"Mithu", True, "NOOB"]
# print(list1)
# print(list1[4])
# print(list1[-4])
# print(list1[2:5])
# print(list1[-2:])
# print(list1[:-4])
# print(list1[1:7:2])
# if "Mithu" in list1:
#     print("y")
# else :
#     print("n")
# if 100 in list1:
#     print("y")
# else :
#     print("n")
# List comprehension
# list2 = [i for i in range(4)]
# print(list2)
# list3 = [i*i for i in range(10) if i%2 == 0 and i*i >= 20]
# print(list3)
# l = [1, 3,2, 8,5,6,9, 2]
# l.append(7)
# l.sort()
# print(l)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(9))
# print(l.count(2))
# m = l
# m = l.copy()
# m[0] = 0
# print(l)
# print(m)
# l.insert(1,100)
# m = [100, 200, 300]
# l.extend(m)
# k = l + m
# print(l)
# print(k)

# tuple in python
# tuples are not changeable/ immutable
# tup = (1,2,3)
# tup = (1,2 ,4, "Mithu", True)
# print(type(tup), tup)
# tup1 = (1) #without comma python thinks it as an integer
# print(type(tup1), tup)
# tup2 = (1,)
# print(type(tup2), tup)
# print(tup[0])
# print(tup[-1])
# if True in tup:
#     print("Yes")
# tup2 = tup[1:4]
# print(tup)
# print(tup2)

# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")
# temp.pop(3)
# temp[2] = "Finland"
# countries = tuple(temp)
# print(countries)
# countries2 = ("India", "China")
# Uff = countries + countries2
# print(Uff)

# tup = (1, 2, 3, 4, 3, 3)
# print(tup.count(3))
# print(tup.index(3))
# print(tup.index(3, 3,5))
# print(tup.index(5))  It gives error 
# print(len(tup))

# import time
# timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
# timestamp2 = time.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
# print(timestamp2)
# hour = int(time.strftime("%H"))
# min = int(time.strftime("%M"))
# sec = int(time.strftime("%S"))
# print(timestamp)
# print(hour)
# print(min)
# print(sec)

# if hour < 12 and min <= 59 and sec <= 59:
#     print("Good Morning") 
# elif hour >= 12 and hour <= 16 :
#     print("Good Afternoon")
# else :
#     print("Good Evening")


# Fstring in python
# letter = "My name is {} and I am from {}"
# name = "Mithu"
# country = "India"
# age = 20
# price = 43.346
# print(letter.format(name, country)) #format method
# print(f"My name is {name} and I am {age} years old") #fstring method
# print(f"My name is {{name}} and I am {{age}} years old")
# print(f"The price of apple is {price:.2f}")
# print(f"{2*30}")

# docstring and pep-8
# Docstring is like comment but it can be accessed and it can change the output of a function
# def square(n):
#     '''Takes a number , returns a square''' #only after the declaration and above the body
#     print(n*n)
#     '''returns a square''' #It is not the docstring
# square(5)
# print(square.__doc__)

# zen of python
# import this    #shows a poem

# set in python ->
# It doesn't take duplicate values and doesn't maintain order
# s = {2,4, 2, 6}
# print(s)
# info = {"mithu", 9.5, 21, 32,True, 21}
# print(info)
# for value in info:
#     print(value)
# Hi = {}
# print(type(Hi)) #<class 'dict'> coz class dictionary also starts with {}
# Hii = set()     #To show the type as a set we need to do this
# print(type(Hii))

# s1 = {1,3, 5, 6, 8}
# s2 = {4, 7,9,5}
# print(s1.union(s2))
# print(s1, s2)
# s1.update(s2)
# print(s1)
# print(s1.intersection(s2))
# print(s1.symmetric_difference(s2))
# print(s1.isdisjoint(s2))
# print(s1.issuperset(s2))
# print(s1.issubset(s2))
# s1.add(2)
# s1.remove(9)  #error throws
# s1.discard(9) #Doesn't throw error
# s1.clear()
# s1.pop() #pop out a random value
# del s1
# print(s1)

#Dictionaries in python -- ordered
# dic = {
#     20 : "kirti",
#     50 : "mithu",
#     60 : "noob"
# }
# print(dic)
# print(dic.keys())
# print(dic.items())
# print(dic.values())
# print(dic[50])  #if not in the dictionary , throws error
# print(dic.get(60)) #if not in the dictionary , shows none
# for key in dic.keys():
#     print(dic[key])

# ep1 = {
#     100 : 70,
#     150 : 69,
#     200 : 89,
#     250 : 99,
# }
# ep2 = {
#     300 : 50,
#     350 : 76
# }
# ep1.update(ep2)
# ep1.clear()
# ep1.pop(150)
# ep1.popitem()
# del ep1[200]
# del ep1 #delete entire dictionary
# print(ep1)

#else with for loop
# for i in range(5):
#     print(i)
# else :
#     print("Ooooooooppssssssssss No i")
# for i in []:
#     print(i)
# else :
#     print("OOOOooooooooooooooooooooooopsssssssss No i")
# for i in range(5):
#     print(i)
#     if(i == 3):
#         break
# else :
#     print("Ooooooooppssssssssss No i") #hence it shows loop doesn't break, it is successfully completed
# i = 0
# while (i < 5):
#     print(i)
#     i += 1

#     if(i == 3):
#         break              #same as for loop , if it breaks , else not run
# else :
#     print("loop ends")

#exception handling
# input1 = input("Enter a number: ")
# arr = [1, 4, 5, 9]
# try:
#     print("multiplication table of")
#     for i in range(1,11):
#         print(f" {input1} x {i} = {int(input1)*i}")
#     print(arr[int(input1)])
# except:
#     print("invalid input")
# except Exception as e:
#     print(e)
# except ValueError:
#     print("Not an integer")
# except IndexError:
#     print("Not in index")

#finally clause 
# try:
#     l = [1, 6, 8, 7, 9]
#     i = int(input("Enter a number "))
#     print(l[i])
# except:
#     print("Error occurred")

# finally:
#     print("Execution finished")

# def fun():
#     try:
#         l = [1, 6, 8, 7, 9]
#         i = int(input("Enter a number "))
#         print(l[i])
#         return 1
#     except:
#         print("Error occurred")
#         return 0

#     finally:                          #Even after return statement, it runs
#         print("Execution finished")

# x = fun()
# print(x)

# custom errors 
# a = int (input("Enter a number between 5 and 10 "))
# if(a < 5 or a > 10):
#     raise ValueError("value must be between 5 and 10")

# b = input("Enter quit ")
# if(b == "quit"):
#     exit
# else:
#     raise ValueError("Write 'quit' properly")


# Enumerate in python
# marks = [12, 45, 23, 89, 56, 59, 98]
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Hurraahhh!")
#     index += 1

# for index, mark in enumerate(marks):
#     print(mark)
#     if(index == 3):
#         print("Hurraahhh!")

# fruits = ["Apple", "Banana", "Orange"]
# for i, fruit in enumerate(fruits):
#     print(i, fruit)
# for v in enumerate(fruits):   #shows the tuples
#     print(v)
# for i, fruit in enumerate(fruits, start=1):
#     print(i, fruit)

# OS module in python
# import os           
# print(os.getcwd())
# print(os.listdir())
# new_directory = "new_directory"
# os.mkdir(new_directory)
# os.rmdir(new_directory)
# os.chdir("..")
# os.rename("file.txt", "myfile.txt")

# Global and local variables
# x = 10
# y = 5
# def fun():
#     global y   # Here we are accesing the global y using global keyword
#     y = 1
#     x = 4
#     print("x" , x)
#     print("y " , y)
# fun()
# print("x" , x)
# print("y " , y)

# Difference between 'is' and '=='  ->> both are used for comparison
# 'IS' is used to compare the exact address location and '==' is used to compare the value
# a = [1, 4, 7]
# b = [1, 4, 7]
# print(a is b)  #false
# print(a == b)  #true
# But for immutable things both return true
# a = 3
# b = 3
# print(a is b)   #true
# print(a == b)   #true
# c = "Mithu"
# d = "Mithu"
# print(c is d)    #true 
# print(c == d)    #true

# File handling
# f = open('myfile.txt', 'r')
# f = open('myfile.txt', 'rt') #text file(by default)
# f = open('myfile.txt', 'rb') #binary or byte file like jpg, pdf etc.
# print(f)
# text = f.read()
# print(text)
# f.close()
# f = open('myfile.txt', 'a') #Append the part with those lines written
# f.write("\nHiii darling")
# f = open('myfile.txt', 'w')
# f.write("Hii sweetHeart")  #delete everything and then write
# f.truncate(5)
# f.close()
# with open('myfile.txt', 'a') as f:
#     f.write("\nHiii cute Noob....")

# f = open('myfile1.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])

#     print(f"Marks of student {i} in Math : {m1}")
#     print(f"Marks of student {i} in English : {m2}")
#     print(f"Marks of student {i} in Odia : {m3}")
#     print(f"Total marks of studen {i} is {m1+m2+m3}")

# f = open('myfile.txt', 'w')
# f = open('myfile.txt', 'a')
# lines = ['Hi Noob \n', 'Hii cutiepie\n', 'Hiii sweetheart\n']
# f.writelines(lines)
# f.close()

# f = open('myfile.txt', 'r')
# f.seek(14)
# print(f.tell())
# data = f.read(5)
# print(f.tell())
# f.close()
# print(data)


# Lambda functions -> Anonymous functions
# def double(x):
#     return x*2

# double = lambda x : x*2 #lambda function
# print(double(5))
# cube = lambda x : x*x*x
# print(cube(5))
# avg = lambda x,y,z : (x+y+z)/3
# print(avg(4, 5, 6))
# def appl(fx, value):
#     return 6 + fx(value)
# print(appl(lambda x: x*x, 3))
# add = lambda x,y : print(f"{x} + {y} = {x+y}")
# add(5, 6)

# map, reduce, fiter
# MAP
# def cube(x):
#     return x*x*x
# l = [1,2,3,4,5,6]
# to cube all the delements of list ->
# newl = []
# for i in l:
#     newl.append(cube(i))
# print(newl)
# or
# newl = list(map(cube, l))
# mewmpl = list(map(lambda x: x*x*x, l))
# print(mewmpl)
# print(newl)
# FILTER
# l = [1,2,3,4,5,6]
# def filter_fun(a):
#     return a>4
# newl = list(filter(filter_fun, l))
# newl = list(filter(lambda x: x > 4, l))
# print(newl)
# REDUCE
# from functools import reduce
# num = [1, 2, 3, 4, 5, 6]
# def fun(x,y):
#     return x+y
# sum = reduce(fun, num)
# sum = reduce(lambda x,y: x+y, num)
# print(sum)


# OOPS in Python
# class person:
#     name = "Harry"
#     occupation = "Software Engineer"
#     networth = 100
#     def info(self):
#       print(f"{self.name} is a {self.occupation}")

# a = person()
# a.name = "Mithu"
# a.occupation = "Software Developer"
# a.info()
# b = person()
# b.info()

# Constructor
# class person:
#     def __init__(self) :                 #Default constructor
#         print("HII EVERYONE")
# a = person()
# class person:
#     def __init__(self, name, occupation) :          #parameterized constructor
#         self.name = name
#         self.occupation = occupation
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
# a = person("Mithu", "Software Developer")
# a.info()

# Decorators
# def greet(fx):       #this can only use if we want to add decorator using @ ,
                    #If we want to pass the function ex- greet(hello)() -> if the function doesn't take parameters then it's fine otherwise we need to use below method 
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this!!")
#     return mfx
# def greet(fx):     #if there is argument(even works if no argument) use this method to add decorate
#     def mfx(*args, **kwargs): #*args -> arguments as a tuple, **kwargs -> arguments as a dictionary
#         print("Good Morning")
#         fx(*args, **kwargs)
#         print("Thanks for using this!!")
#     return mfx
# # @greet
# def hello():
#     print("Hii Noooooooooooob")
# # hello()
# greet(hello)()    #Either use this or use the above @greet method to decorate
# def add(a, b):
#     print(a + b)
# greet(add)(1,2)   #-> It doesn't pass the parameters to add, So we need to modify mfx by giving it parameters

# logging function -> decorator example
# import logging
# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"calling {func.__name__} with arguments {args} and kwargs {kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"Function {func.__name__} returned result: {result}")
#         return result
#     return decorated
# @log_function_call
# def fun(a,b):
#     return a+b
# fun(1,2)

# Getters and Setters
# class myclass:
#     def __init__(self, value) :
#         self._value = value
#     def show(self) :
#         print(f"Value is {self._value}")
#     @property
#     def value(self) :
#         return self._value
#     @value.setter
#     def value(self, nval):
#         self._value = nval
# obj = myclass(10)
# print(obj.value)
# obj.value = 20
# print(obj.value)
# obj.show()

# Inheritance    
# class employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def details(self):
#         print(f"The employee name is {self.name} and id is {self.id}")

# e1 = employee("Mithu", 400)
# e1.details()

# class programmer(employee):
    
#     def language(self,lang):
#         print(f"The language known is : {lang}")

# p1 = programmer("Kirti", 300)
# p1.details()
# p1.language("python")

# Static Method  ->This method is used without passing self as argument
# class Math:
#     def __init__(self,num) :
#         self.num = num
#     def addtosum(self, n):
#         self.num += n
#     @staticmethod
#     def add(a, b):
#         return a+b
# a = Math(5)
# a.addtosum(6)
# print(a.num)
# # print(add(5,6)) #show error
# print(a.add(5,6)) #Calling the static method by object
# print(Math.add(5,6))    #Calling the static method by Classname

# Instance variable VS Class variable
# class myclass:
#     companyname = "Alphabet"
#     noofemployees = 0
#     def __init__(self, name):
#         self.name = name
#         self.raiseamt = 2
#         myclass.noofemployees += 1
#     def show(self):
#         print(f"The employee name is {self.name}, working in {self.companyname} and percentage raise is {self.raiseamt}")
# e1 = myclass("Mithu")
# e1.raiseamt = 5     #we can access the instance variable by object
# e1.show()
# print(f"The {myclass.noofemployees} sized company")
# e2 = myclass("Noob")
# # e2.companyname = "Google"
# e2.show()
# print(myclass.companyname)   #we can access the class variable by classname or by object
# print(f"The {myclass.noofemployees} sized company")

# Class Method   -> This method is used to change the class variable
# class employee:
#     company = "Apple"
#     def show(self):
#         print(f"The name is {self.name} and the company is {self.company}")

#     @classmethod
#     def change(cls, ncompany):
#         cls.company = ncompany

# e1 = employee()
# e1.name = "Mithu"
# e1.show()
# employee.change("GOOGLE")
# # e1.change("Google")
# e1.show()
# e2 = employee()
# e2.name = "Noob"
# e2.show()

# Class method as alternative constructor
# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     @classmethod
#     def getname(cls, str):
#         return cls(str.split('-')[0],str.split('-')[1])
    
# e1 = employee("Mithu", 1200000)
# print(e1.name," ", e1.salary)
# string = "Noob-15000000"
# e2 = employee.getname(string)
# print(e2.name," ", e2.salary)

# class person:
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age
#     @classmethod
#     def fromSring(cls, string):
#         name, age = string.split(',')
#         return cls(name, age)

# p1 = person("Mithu", 22)
# print(p1.name, p1.age)

# p2 = person.fromSring("Noob, 21")
# print(p2.name, p2.age)

# dir() method, __dict__  -> an attribute, help() method ->
# x = [1, 2, 3]
# print(dir(x))
# y = (1,2,3)
# print(dir(y))

# class person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
# p = person("Noob", 20)
# print(p.__dict__)  #it gives details in dictionary format
# # print(help(person))
# print(help(str))

# Super keyword
# class pClass:
#     def parent(self):
#         print("This is the parent method")
# class cClass(pClass):
#     def child(self):
#         print("This is the child method")
#         super().parent()

# c = cClass()
# c.parent()  # Calls the parent class method
# c.child()

# class employee:
#     def __init__(self, name, id) :
#         self.name = name
#         self.id = id
# class programmer(employee):
#     def __init__(self, name, id, lang) :
#         super().__init__(name,id)    #calls the parent class constructor
#         self.lang = lang

# rohan = employee("Rohan", 500)
# harry = programmer("Harry", 230, "Python")

# print(rohan.name , rohan.id)
# print(harry.name , harry.id, harry.lang)

# Magic / Dunder function
# __len__: This method is used to define the length of an object. It is called when the built-in len() function is applied to an instance of your class. 
# class MyClass:
#     def __init__(self, data):
#         self.data = data

#     def __len__(self):
#         return len(self.data)

# obj = MyClass([1, 2, 3])
# print(f"Length of the object is {len(obj)}")  

# __str__: This method is called by the built-in str() function and the print() function to obtain a human-readable string representation of an object. 
# class MyClass:
#     def __init__(self, data):
#         self.data = data

#     def __str__(self):
#         return f"MyClass with data: {self.data}"

# obj = MyClass([1, 2, 3])
# print(str(obj)) 

# __repr__: This method is used to define the "official" string representation of an object. It is typically used for debugging and development. When you call repr() on an object, or when the interpreter needs a string representation, __repr__ is called
# class MyClass:
#     def __init__(self, data):
#         self.data = data

#     def __repr__(self):
#         return f"MyClass({self.data})"

# obj = MyClass([1, 2, 3])
# print(repr(obj))  

# __call__: This method allows an instance of a class to be called as a function.
# class CallableClass:
#     def __call__(self, x):
#         return x * 2

# obj = CallableClass()
# result = obj(5)
# print(result)  

# Method Overriding
# class Shape:
#     def area(self):
#         # A generic method for calculating the area
#         pass

# class Square(Shape):
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def area(self):
#         # Override the area method for squares
#         return self.side_length ** 2

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         # Override the area method for circles
#         return 3.14 * self.radius ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         # Override the area method for triangles
#         return 0.5 * self.base * self.height

# # Examples
# square = Square(4)
# circle = Circle(3)
# triangle = Triangle(5, 8)

# print("Area of Square:", square.area())     
# print("Area of Circle:", circle.area())    
# print("Area of Triangle:", triangle.area())  

# class square:
#     def __init__(self, length):
#         self.length = length
#     def area(self):
#         return self.length*self.length

# class circle(square):
#     def __init__(self, radius):
#         super().__init__(radius)
#     def area(self):
#         return 3.14* super().area()
        
# s = square(5)
# print(f"The area of the square is {s.area()}")
# c = circle(5)
# print(f"The area of the Circle is {c.area()}")

# Operator Overloading
# class vector:
#     def __init__(self, i , j , k) :
#         self.i = i
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
#     def __add__(self, x):
#         # return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k" #This returns the vector as a string
#         return vector(self.i+x.i, self.j+x.j, self.k+x.k)
#     def __sub__(self, x):
#         return vector(self.i-x.i, self.j-x.j, self.k-x.k)

# v1 = vector(1, 2, 3)
# v2 = vector(4, 5, 6)
# print(v1)
# print(v2)
# print(v1 + v2)
# print(v2 - v1)
# print(v1 - v2)
# print(type(v1))
# print(type(v1+v2))

# Multiple Inheritance  -> a class inherits more than one base class
# Diamond Shape Problem -> Sometimes Multiple inheritance creates confusion 
# class employees:
#     def __init__(self,name) :
#         self.name = name
#     def show(self):
#         print(f'The employee name {self.name}')
        
# class dancer:
#     def __init__(self, dance) :
#         self.dance = dance
#     def show(self):
#         print(f'The Dance style {self.dance}')

# class empdancer(employees, dancer): #It shows the employee show function first
# # class empdancer(dancer, employees):  #It shows the dancer show function first
#     def __init__(self,name,dance):
#         self.name = name
#         self.dance = dance

# o = empdancer("Mithu", "Kathak")
# o.show()
# print(empdancer.mro())  #It returns the Method Resolution Order
# print(empdancer.__mro__)  #It also shows the method resolution order

# Hybrid Inheritance
# class A:
#     def method(self):
#         print("A's method")

# class B(A):
#     def method(self):
#         print("B's method")

# class C(A):
#     def method(self):
#         print("C's method")

# class D(B, C):
#     pass

# # Method Resolution Order for class D
# print(D.__mro__)

# d_instance = D()
# d_instance.method()

# Multilevel Inheritance  -->   Parent -> child -> Child
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Mammal(Animal):
#     def speak(self):
#         Animal.speak(self)
#         print("Mammal runs")

# class Dog(Mammal):
#     def speak(self):
#         Mammal.speak(self)
#         print("Dog barks")

# d1 = Dog()

# d1.speak()  
# print(Dog.mro())  

# Hierarchical inheritance
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# cat = Cat()
# dog = Dog()

# cat.speak()  
# dog.speak()  
# cat.meow()   
# dog.bark()   

# Time module in Python
# import time
# def usingwhile():
#     i = 0
#     while i < 2000:
#         i += 1
#         print(i)
# def usingfor():
#     for i in range(2000):
#         print(i)

# init = time.time()
# usingwhile()
# t1 = time.time() - init
# init = time.time()
# usingfor()
# print(t1)
# print(time.time() - init)

# print("Hello")
# time.sleep(5)
# print("This is after 5 seconds")

# t = time.localtime()
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
# print(formatted_time)


# Difference between module, package and library
#   Python Module: A module is a single Python file that contains Python code, including variables, functions, and classes. Modules are used to organize code into reusable files. They help in breaking down a large program into smaller, manageable units.You can import and use modules in other Python scripts using the import statement. 
# Python Package:A package is a way of organizing related modules into a directory hierarchy. A package includes an __init__.py file (which can be empty) to indicate that the directory should be treated as a package.Packages provide a hierarchical structure for organizing modules. They help avoid naming conflicts and make it easier to manage and distribute code.
# Python Library:A library, in a broad sense, refers to a collection of modules or packages that provide pre-written code and functionality to perform specific tasks. It can include a variety of modules and packages designed for different purposes.Python has a standard library that includes many modules and packages covering a wide range of functionalities, such as math, os, datetime, etc. 

# Object introspection -> using dir(), typr() or id() --> These give details about the object
# class emp:
#     def show(self):
#         print("Hello, I'm an employee")
# e = emp()
# o = "This is a string"
# print(type(e))
# print(id(e))
# print(dir(e))
# print(type(o))
# print(id(o))
# print(dir(o))
# import inspect
# print(inspect.getmembers(e))

# Walrus operator  (:=)  --> Used to assign value to a variable within an expression
# print(a := False)
# Normal way
# foods = []
# while True:
#     food = input("What food do you like? ")
#     if food == "quit":
#         break
#     foods.append(food)
# Using warlus operator
# foods = []
# while(food := input("What food do you like? ")) != "quit":
#     foods.append(food)
# print(foods)

# Shutil module
# import shutil
# shutil.copy("python2.py", "main2.py")
# shutil.copy2("main.py", "main3.py")  #Copies the exact metadata also
# shutil.copytree("src", "dest") #This is used to copy the complete folder
# shutil.move("src", "dest")  # moves a file/folder one destination to another destination

# Request module
# import requests
# response = requests.get("https://www.google.com/")
# print(response)
# print(response.text)
# r = requests.get('https://api.github.com/events')
# print(r.json())

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text)
# print(r)
# print(r.status_code)
# print(r.headers)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())
# for anchor in soup.find_all("a"):
#     # print(anchor.text)
#     print(anchor)

# Generators  -> Concise and memory efficient, when required we use this

# def simple_generator():
#     yield 1       -> yield is used to generate 
#     yield 2
#     yield 3

# for value in simple_generator():
#     print(value)

# def my_generator():
#     for i in range(100):
#         yield i
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# for j in gen:
#     print(j)

# def fibonacci_generator(limit):
#     a, b = 0, 1
#     while a <= limit:
#         yield a
#         a, b = b, a + b

# for number in fibonacci_generator(21):
#     print(number)

# Function Caching
# import time
# import functools
# @functools.lru_cache(maxsize= None)
# from functools import lru_cache
# @lru_cache(maxsize= None)  # maxsize=None means the cache can grow without bound
# def fx(n):
#     time.sleep(3)
#     return n* 5

# print(fx(20))
# print("Done for 20")
# print(fx(2))
# print("Done for 2")
# print(fx(55))
# print("Done for 55")
# # This will show directly without waiting because the value has already been stored in cache and when again required it will be fetched from cache
# print(fx(20))
# print("Done for 20")
# print(fx(2))
# print("Done for 2")
# print(fx(55))
# print("Done for 55")

# @lru_cache(maxsize=None) 
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# result = fibonacci(10)
# print(result)

# Regular expression
# import re
# result = re.match('abc', 'abcdef')
# result = re.search('abc', 'abcdef')
# print(result)
# print(result.span)
# print(result.span())

# pattern = re.compile('(\d+)-(\w+)')
# result = pattern.match('123-abc')
# result = pattern.match('123--abc')  #pattern doesn't match
# result = pattern.match('123-7bc')
# result = pattern.match('123-456')
# result = pattern.match('123-a_c')   
# result = pattern.match('123-a-c')    #the group(2) is only 'a
# result = pattern.match('1-23-abc')    #group(1) = 1, group(2) = 23
# if result:
#     print(result.group(1))  
#     print(result.group(2)) 
# else:
#     print("Oops .. pattern not found") 

# result = re.findall('\d+', 'There are 123 apples and 456 oranges.')
# print(result)
# print(type(result))
# matches = re.finditer('\d+', 'There are 123 apples and 456 oranges.')
# for match in matches:
#     print(match.group())
#     print(type(match.group()))
# result1 = re.findall('\w+', 'There are 123 apples and 456 oranges.')
# print(result1)

# new_string = re.sub('\d+', 'X', 'There are 123 apples and 456 oranges.')  #Replacement occurs
# print(new_string)

# pattern = re.compile('\d')  # Matches any digit
# result = pattern.findall('The price is $20.99')
# print(result)
# pattern = re.compile('[a-zA-Z]')  # Matches any uppercase or lowercase letter
# result = pattern.findall('Hello World!')
# print(result)
# pattern = re.compile('\w')  # Matches any word character (alphanumeric + underscore)
# result = pattern.findall('user_name123@example.com')
# print(result)
# pattern = re.compile('a{2,4}')  # Matches 'a' repeated 2 to 4 times
# result = pattern.findall('aa abc aaaa aaaaaa')
# print(result)
# pattern = re.compile('ba*')  # Matches 'b' followed by zero or more 'a's
# result = pattern.findall('b bat baat baaat')
# print(result)
# pattern = re.compile('ba+')  # Matches 'b' followed by one or more 'a's
# result = pattern.findall('b bat baat baaat')
# print(result)
# pattern = re.compile('colou?r')  # Matches Zero or One Occurrence
# result = pattern.findall('color colour')
# print(result)

# Asynchio
# import asyncio
# async def my_coroutine():
#     print("Start")
#     await asyncio.sleep(1)
#     print("End")

# asyncio.run(my_coroutine())

# async def function1():
#     print("Func1")
#     await asyncio.sleep(2)
#     print("Func1 Ends")
# async def function2():
#     print("Func2")
#     await asyncio.sleep(1)
#     print("Func2 Ends")
# async def function3():
#     print("Func3")
#     await asyncio.sleep(3)
#     print("Func3 Ends")
# async def main():
#     # await function1()
#     # await function2()
#     # await function3()
#     # using gather(), all function starts execution parallelly
#     l = await asyncio.gather(
#         function1(),
#         function2(),
#         function3()
#     )
# asyncio.run(main())

# Using asyncio with aiohttp for HTTP Requests
# import aiohttp
# import asyncio

# async def fetch_data(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()

# async def main():
#     url = "https://jsonplaceholder.typicode.com/todos/1"
#     data = await fetch_data(url)
#     print(data)

# asyncio.run(main())

# Multithreading
# import threading
# import time

# def func(seconds):
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)
# # tim1 = time.perf_counter()
# # func(4)
# # func(2)
# # func(1)
# # tim2 = time.perf_counter()
# # print(tim2 - tim1)

# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[2])
# t3 = threading.Thread(target=func, args=[6])
# tim1 = time.perf_counter()
# t1.start()
# t2.start()
# t3.start()
# tim2 = time.perf_counter()
# print(tim2 - tim1)
# t1.join()
# t2.join()
# t3.join()
# tim2 = time.perf_counter()
# print(tim2 - tim1)

# Concurrent futures
# import time
# import threading
# from concurrent.futures import ThreadPoolExecutor

# def func(seconds):
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)
#     return seconds
# def poolingdemo():
#     with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func,3)
        # print(future1.result())
        # future2 = executor.submit(func,2)
        # print(future2.result())
        # future3 = executor.submit(func,4)
        # print(future3.result())
        # using map
#         l = [2, 5, 3, 4]
#         results = executor.map(func, l)
#         for result in results:
#             print(result)
# poolingdemo()

# Multiprocessing
# import multiprocessing
# import concurrent.futures
# import requests
# def downloadfile(url, name):
#     print("Started Downloading")
#     response = requests.get(url)
#     open(f"Files/file{name}.jpg", "wb").write(response.content)
#     print(f"Downloading Finished{name}")

# url = "https://picsum.photos/2000/3000"
# pros = []
# for i in range(5):
#     # Normal process
#     # downloadfile(url,i)
#     # Using multiprocessing
#     p = multiprocessing.Process(target=downloadfile, args=[url,i])
#     p.start()
#     pros.append(p)

# for p in pros:
#     p.join()

# Using concurrent futures
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     l1 = [url for i in range(5)]
#     l2 = [i for i in range(5)]
#     results = executor.map(downloadfile, l1, l2)
#     for result in results:
#         print(result)

# Random module
# import random
# random_number = random.random()  #generates a number between 0.0 to 1.0
# random_integer = random.randint(1, 10) #[1,10]
# print(random_integer)
# items = ["apple", "banana", "orange", "grapes"]
# random_item = random.choice(items)
# print(random_item)
# random.shuffle(items) #suffles the element sequences
# random_sample = random.sample(items, 2)  #select 2 random items
# print(random_sample)
# random_float = random.uniform(2.5, 5.5)  #Gives random floating point number
# print(random_float)
# random.seed(42)  # If you use the same seed value, you'll get the same sequence of random numbers.
# random_number = random.randrange(0, 100, 10)
# print(random_number)

# Merging the pdfs
# import os
# from PyPDF2 import PdfWriter

# merger = PdfWriter()
# files = [file for file in os.listdir() if file.endswith('.pdf')]
# for pdf in files:
# for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()

# from PyPDF2 import PdfReader, PdfWriter

# reader = PdfReader("BigFile.pdf")
# writer = PdfWriter()

# for page in reader.pages:
#     writer.add_page(page)

# writer.add_metadata(reader.metadata)

# with open("smaller-new-file.pdf", "wb") as fp:
#     writer.write(fp)

# Text to speech in windows
# import pyttsx3

# def text_to_speech(text):
#     # Initialize the text-to-speech engine
#     engine = pyttsx3.init()

#     engine.setProperty('rate', 220)  # Speed of speech
#     engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

#     # Convert the given text to speech
#     engine.say(text)

#     # Wait for the speech to finish
#     engine.runAndWait()

# t = ["Mithu","Cute", "Noob" ]
# for name in t:
#         text_to_speech(f"Hello, {name}.")

# News Api
# import requests
# import json
# query = input("In which type of new are you interested ? ")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2023-11-19&sortBy=publishedAt&apiKey=621f75c1a1384e45bbdeb882b830b20c"
# r = requests.get(url)
# # print(r.text)
# news = json.loads(r.text)
# # print(news, type(news))  #type -> dictionary
# for article in news["articles"]:
#     print(f"\n {article['title']} \n")
#     print(f"{article['description']} \n\n")

# Email validation using regex
# import re
# email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# email = input("Enteer your email address: ")
# if re.search(email_condition, email):
#     print("Thank you for coming")
# else:
#     print("Please enter valid email address")

# Phone number details
import phonenumbers
from phonenumbers import geocoder, timezone, carrier
Number = input("Enyter your phone number(+code): ")
phone = phonenumbers.parse(Number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
region = geocoder.description_for_number(phone, "en")
p = phonenumbers.can_be_internationally_dialled(phone)

if p == True:
    print(f"Details about the phone number {phone.national_number} : from timezone {time} {car} of {region} can be Internationally dialled")
else :
    print(f"Details about the phone number {phone.national_number} : from timezone {time} {car} of {region} can't be Internationally dialled")
