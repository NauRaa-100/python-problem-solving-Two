#Reviewing 
#Strings + Slicing + Methods

sentence = "   Python is Powerful and Easy!   "

print(sentence.strip())#1
print(sentence.lower())#2
print(sentence.index('Powerful'))#3
print(sentence.strip().split(' '))#4
print(sentence.strip()[10:19])#5
print('#'*15)
#---------------------------------
#2 String Formatting
name = "Noura"
age = 24
language = "Python"

print(f"My name is {name}, I'm {age} and I love {language}.")
#--------------------------------
#3
user = "Noura"
score = 99.654321

print(f"Student {user} scored {round(score,2)}%")
#--------------------------------
#4 numbers & operators 
a = 17
b = 4
print(a%b)
print(a//b)
print(a**b)
#--------------------------------
#4 lists
names = ["Sara", "Noura", "Mona", "Noura", "Ali"]

names_copy=names.copy()
names_copy.remove('Sara')
names_copy.remove('Noura')
print(names_copy)
print(sorted(names ,reverse=False))
print('#'*10)
print(names.count(('Noura')))
names.append('Tamer')
print(names)

#-------------------------------------
#6 Tuples
colors = ("red", "blue", "green", "blue", "yellow")
print(colors.count('blue'))
print(colors.index('green'))
print(colors[1:4])
#-------------------------------------
#7 Set , Dict , Operators , input
#1
day1 = ["Noura", "Ali", "Mona", "Tamer"]
day2 = ["Mona", "Tamer", "Yasmine", "Ali"]

set_A=set(day1)
set_B=set(day2)
print(set_A.intersection_update(set_B))
print(set_A)
setU=set_A.union(set_B)
setU.add('Noura')
print(setU)
#----------------------------------------

#3 Dictionary
student = {
    "name": "Noura",
    "age": 24,
    "grades": [90, 85, 100]
}

student.setdefault('Passed',True)
def calc():
    average= sum(student["grades"])/len(student["grades"])
    if average >=60:
       print(f'Student {student['name']} is {student["age"]} years old. Average grade: {round(average ,2)}. Passed: {student['Passed']}')
calc()

#---------------------------------------
#4 input , set
#i= input('Plz insert sentence: ')
#if not i.isnumeric():
#    print(len(i))
#i_s= set(i)
#print(i_s)
#print(sorted(i_s))
#---------------------------------------
#5 Dictionary & Set

library = {
    "Python": {"Beginner", "Advanced"},
    "JavaScript": {"Beginner"},
    "AI": {"Advanced", "Research"},
}


library["JavaScript"].add('Intermediate')
print(library)
library["AI"].remove('Research')
print(library)
print(f'{library['Python']}, num:{len(library["Python"])} \n{library["JavaScript"]} ,num:{len(library["JavaScript"])}')
#-------------------------------------
#🌀 Control Flow + While + Else + Loop – While Trainings
#1
counter = 1
i=0
while i <=10:
    if i %2 !=0:
      print(i)
    i+=counter
#-------------------------------
#2
attempts = 3
correct_password = "python123"

#while attempts < 3:
#    inp = input("You have only 3 tries: ")
#    if inp == correct_password:
#        print("Access Granted!")
#        break
#    else:
#        print("Access Denied")
#        attempts += 1
#else:
#    print("You've tried 3 times. Access Blocked.")

#--------------------------------
#3
#bookmarks=[]

#while True:
#   links= input('Insert Ur link here: ')
#   bookmarks.append(links)
#   if links== 'exit' or links== 'EXIT' or links=='Exit':
#      break
#---------------------------------
print('#'*10)
#4 🔁 Loop – For, Nested, Break, Continue, Pass
nums = [1, 2, 3, 4, 5, 6, 7, 8]

for x in nums:
   if x > 3 :
      print(x)
   elif x %2 == 0:continue

#------------------------------
#5
names = ["Sara", "Ali", "Noura"]
marks = [90, 85, 100]

total=zip(names,marks)
for x , y in total:
   print(f"{x}:{y}")

#-------------------------------
#6
students = {
    "Sara": [85, 90, 100],
    "Ali": [70, 65, 60],
    "Noura": [95, 100, 100]
}
for key , value in students.items():
   
   average= sum(x for x in value)/len(value)
   if average >=90:
      print(f"{key}:{round(average ,2)} Excellent")

#---------------------------------
#7
def is_even(num):
   if num %2 ==0:
      return True
   else:
      return False
   
print(is_even(2))
#---------------------------------
#8
def say_hello(name):
    return f"Hello {name}, nice to meet you"

print(say_hello('NauRaa'))

#---------------------------------
#9 🧳 Function Parameters + Packing/Unpacking + Default
def print_items(*nums):
   for x in nums:
      print(x)
   

print_items(10 ,2 ,21)
#----------------------------------
#10
def display_info(name, age=20, country="Egypt"):
    print(f"Hi Your Data is: your name: {name} , your age: {age} and your country is {country}")



display_info('Nauraa')
#-----------------------------------
#11 💼 Function Keyword Packing + Scope + Recursion + Lambda

def recever(**kwargs):
   return kwargs

print(recever(name='noura' , age=20 )) 

#-------------------------------------
#12
x = 10
def outer():
    x = 5
    def inner():
        print(x)
    inner()
outer()
# 5 بسبب  print(x) in local scope
#-------------------------------------
#13
def func(num):
   if num <= 1:
      return 1
   return num * func(num -1)
print(func(5))
   
#----------------------------------
#14
nums=[1,2,3,4]
square= map(lambda x: x**2 , nums)
for x in square:
   print(x)

#----------------------------------
#🧠 general basics python
#1
name='Nauraa'
country='Egypt'
print(f"My name is {name} and I am from {country}")

#-----------------------------------
#2
my_string='Artificial Intelligence'

print(f"{my_string[0]}-{my_string[-1]}")
#----------------------------------
#3
#def recever():
#   inpo=input('Insert one word: ')
   
#   print(len(inpo))
#   if len(inpo)>=7:
#      print('Yes it has 7 or more')

#recever()
print('#'*10)
#---------------------------------
#4
my_string= "Data analysis and AI are amazing."
print(my_string.count('a'))
#----------------------------------
#4 Lists ,Tuples
items = ["apple", "banana", "cherry", "apple", "banana"]
my_set=set(items)
print(sorted(my_set))
#-------------------------
5
my_tuple=(1,2,3,4,5)
print(max(my_tuple))
print(min(my_tuple))
#------------------------
#6  Boolean, Conditions, Input
#def recever():
#   age = int(input('Plz insert ur age: '))
#   if age < 13:
 #     print('a child')
 #  elif age <= 19:
 #     print('a teenager')
#   else:
#      print('Adult')
#recever()

#-------------------------
#7
def recever_c(word):
   if word[0].isupper() and word.endswith('.'):
      print('Yes it starts with capital letter and ends with a dot')
   else:
      print('No')
recever_c('Noura.')

#-------------------------------
print('#'*10)
#8
#def recever():
#   inpo = input('insert here if u like programmin(y , n):   ')
#   if inpo=='y':
#      print('Welcome future Programmer')
#   else:
#      print('Ok')
#recever()
#-------------------------------
#9
students = {
    "Sara": [85, 90, 100],
    "Ali": [70, 65, 60],
    "Noura": [95, 100, 100]
}
for key,value in students.items():
   average=sum(value)/len(value)
   if average >=85:
      print(f'{key}: Excellent')
   elif average <60:
      print(f'{key}: Week')
   else:
      print(f'{key}: Good')
#-------------------------------
#10
#while True:
 #  inpo = input('insert a word or type "exit" to stop: ')
 #  if inpo == 'exit':
 #     break
 #  else:
#      print(inpo.upper())  # مثال على التعامل

#------------------------------
#11
#------------------------------
#12 functions
def greet(name):
   return f"Hello {name}!"
print(greet('NauRaa'))
#-----------------------------
#13
def area(x,y):
   return x * y
print(area(10,20))
#----------------------------
#14
def func(*args):
   return sum(args)/ len(args)
print(func(1 ,2 ,10 ,5))
#----------------------------
#15
def func(**kwargs):
   for key ,value in kwargs.items():
      print(f"{key}: --> {value}:")
func(name='NauRaa', age=25)
#لية لما عملت ريتيرن طلعلى اول واحدة بس الاسم 
#----------------------------
#16
def is_prime(n):
   if n <= 1:
      print("It's not a prime number")
      return
   for i in range(2, int(n**0.5)+1):
      if n % i == 0:
         print("It's not a prime number")
         return
   print("It's a prime number")
is_prime(8)

#-----------------------------
#17
def recever(n):
   if n == 1:
      return 1
   return n * recever(n-1)
print(recever(5))
#-----------------------------
#18
nums=[1, 2, 3, 4]
square= map(lambda x:x**2 ,nums)
nums_mapped=[]
for x in square:
   nums_mapped.append(x)
print(nums_mapped)

#----------------------------
for x in range(1, 11):
    print(f"{x}:", end=' ')
    is_prime(x)
#---------------------------
#Tasks about part one of OOP
#1
class Employee:
   company="TechCorp"


   def __init__(self,name ,salary):
      self.name= name
      self.salary= salary
   def get_info(self):
      return f"Employee:{self.name} | Salary:{self.salary} | Company:{Employee.company}"
      

my_class=Employee('NauRaa' , 10000)
print(my_class.get_info())
#------------------------------
#2
class Employee:
   company = "TechCorp"
   count = 0

   def __init__(self, name, salary):
       self.name = name
       self.salary = salary
       Employee.count += 1  # هنا بزود عدد الموظفين

   def get_info(self):
       return f"Employee: {self.name} | Salary: {self.salary} | Company: {Employee.company}"

   @classmethod
   def get_count(cls):
       return f'We have {cls.count} employees'  # نستخدم cls بدل Employee عشان الكود يبقى مرن

# Testing
e1 = Employee("Noura", 1000)
e2 = Employee("Ali", 2000)
print(Employee.get_count())  # → We have 2 employees

#------------------------------
#3
class Employee:
   @staticmethod
   def is_valid_salary(num):
      if num >= 3000:
         return 'Valid salary'
      else:
         return 'Invalid salary'

print(Employee.is_valid_salary(100))

#------------------------------
#4
class LibraryBook :

   def __init__(self,title,author):
      self.title=title
      self.author=author
   def __str__(self):
      return f"Book: {self.title} by {self.author}"
my_class= LibraryBook('Python Basics' , 'Elzero')

print(my_class)
#-----------------------------
#5
class LibraryBook :

   def __init__(self,title,author):
      self.title=title
      self.author=author
   def __str__(self):
      return f"Book: {self.title} by {self.author}"
   def __add__(self, other):
     return f"Combo: {self.title} + {other.title}"

my_class= LibraryBook('Python Basics' , 'Elzero')

b1 = LibraryBook("Python", "Elzero")
b2 = LibraryBook("OOP", "Ziad")
print(b1 + b2)

#-----------------------------
#6
class Company:
   def __init__(self, name, employees=None):
      self.name = name
      self.employees = employees if employees else []

   def add_employee(self, emp):
      self.employees.append(emp)

   def __len__(self):
      return len(self.employees)

   def __str__(self):
      return f"Company: {self.name}, Employees: {len(self.employees)}"

# Testing
c = Company("TechCorp")
c.add_employee("Noura")
c.add_employee("Ali")
print(c)              # → Company: TechCorp, Employees: 2
print(len(c))         # → 2

#-------------------------------
# OOP Part 1
#class Student:
 
 #  @classmethod
 #  def get_result(cls,name,grade):
 #     cls.name=name
 #     cls.grade=grade
 #     if grade>50:
 #        return 'Pass'
 #     else:
 #        return 'Fail'
#print(Student('Nauraa',96))

#حسب الكلام المسالة كتبت وطلعت غلط 
class Student:
   def __init__(self ,name ,grade):
      self.name=name
      self.grade=grade
   def get_result(self):

      if self.grade>50:
         return 'Pass'
      else:
         return 'Fail'

student_one= Student('Nauraa',96)
print(student_one.get_result())
#------------------------------------
#2
class Student:
   school_name='AI Academy'
   def __init__(self ,name ,grade):
      self.name=name
      self.grade=grade
   def get_result(self):

      if self.grade>50:
         return 'Pass'
      else:
         return 'Fail'
   
   def full_info(self):
      return f"Name: {self.name}, Grade: {self.grade}, School Name: {Student.school_name}"


student_one= Student('Nauraa',96)
print(student_one.get_result())
print(Student.full_info(student_one))
#----------------------------------
#3
class User:
   count=0
   def __init__(self,name):
      self.name=name
      User.count+=1
   @classmethod   
   def get_count(cls):
      return f"Number of users:{cls.count}"
user_one=User('Nauraa')
print(User.get_count())#1
user_two=User('Ahmed')
user_two=User('Ahmed')
user_two=User('Ahmed')
print(User.get_count())#4

#----------------------------------
#4
print('#'*10)

class Validator:
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

print(Validator.is_valid_email('nauraa_1009Gmailcom'))  # False
print(Validator.is_valid_email('nauraa_1009@mail.com'))  # True

print('#'*10)
#------------------------------------
#5
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @classmethod
    def from_square(cls, side):
        return cls(side, side)

r = Rectangle.from_square(5)
print(r.area())  # 25

#---------------------------------------
#6
class Movie:
   def __init__(self,title,year):
      self.t=title
      self.y=year

   def __str__(self):
      return f"Movie: {self.t}-{self.y}"
movie_one=Movie('interstellar' ,2010)
movie_Two=Movie('Witchers' ,2005)
print(movie_one)
print(movie_Two)
#--------------------------------------
#7
class Movie:
   def __init__(self,title,year):
      self.t=title
      self.y=year

   def __str__(self):
      return f"Movie: {self.t}-{self.y}"
   def __add__(self,other):
      return f"Double Feature:{ self.t + other.t}"
movie_one=Movie('interstellar' ,2010)
movie_Two=Movie('Witchers' ,2005)
print(movie_one)
print(movie_Two)
print(movie_one.t +' & '+ movie_Two.t)
print(Movie.__add__(movie_one , movie_Two))
#------------------------------------
#8
class Playlist:
   def __init__(self,songs=None):
      self.s=songs if songs else [] # السطر دا معناه اية 
   def add_song(self,name):
      self.s.append(name)
   def __len__(self):
      return len(self.s)
song=Playlist()
song.add_song('Feen Habiby')
song.add_song('A2olk B7bk')
print(len(song))
#---------------------------------------
#9
class BankAccount:
   bank_name='NauRaa Bank'
   def __init__(self,name,balance):
      self.name=name
      self.balance=balance

   def deposit(self,amount):
      return self.balance+amount
   def withdraw(self,amount):
      return self.balance - amount
   @staticmethod
   def is_valid_amount(amount):
      if amount <0:
         return False
      else:
         return True

bank_acc=BankAccount('NauRaa',10000)
#bank_acc.deposit(10000)
print(bank_acc.deposit(10))
print(BankAccount.is_valid_amount(-100))
#-----------------------------
#10
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.prod = []

    def add_product(self, product):
        self.prod.append(product)

    def total_price(self):
        return sum([p.price for p in self.prod])

    def __len__(self):
        return len(self.prod)

# إنشاء منتجات
apple = Product("Apple", 10)
banana = Product("Banana", 5)

# إنشاء سلة وإضافة منتجات
cart = Cart()
cart.add_product(apple)
cart.add_product(banana)

print(len(cart))            # 2
print(cart.total_price())   # 15

#---------------------------------
#keeping OOP
class Employee:
   company = 'OOpcorp'
   employee_count=0

   def __init__(self,name,salary):
      self.name=name
      self.salary=salary
      Employee.employee_count+=1
   @classmethod   
   def get_count(cls):
      return f"We have: {Employee.employee_count} employees"

e1 = Employee("Nour", 5000)
e2 = Employee("Ali", 4000)
print(Employee.get_count())  # We have 2 employees

#---------------------------------
#2

class Employee:
   company = 'OOpcorp'
   employee_count=0

   def __init__(self,name,salary):
      self.name=name
      self.salary=salary
      Employee.employee_count+=1
   @classmethod   
   def get_count(cls):
      return f"We have: {Employee.employee_count} employees"
   @staticmethod
   def is_valid_salary(salary):
      if salary > 3000:
         return "valid salary"
      else:
         return "Invalid salary"

e1 = Employee("Nour", 5000)
e2 = Employee("Ali", 4000)
print(Employee.get_count()) 
print(Employee.is_valid_salary(2500))  # Invalid salary
print(Employee.is_valid_salary(3500))  # Valid salary

#----------------------------------
#3
class Book:
   def __init__(self,title,author):
      self.title=title
      self.author=author
   def __str__(self):
      return self.title
   def __add__(self,other):
      return f"Combo Book: {self.title +' + ' + other.title}"
   
b1 = Book("Python", "Nour")
b2 = Book("OOP", "Ali")
print(b1 + b2)  # Combo Book: Python + OOP

#---------------------------------
#4
class Company:
   def __init__(self,name):
      self.name=name
      self.emp=[]
   def add_employee(self,employee):
      self.emp.append(employee)
   def __len__(self):
      return len(self.emp)

c = Company("Techie")
c.add_employee("Nour")
c.add_employee("Ali")
print(len(c))  # 2

#--------------------------------
#5
class Employee:
   def __init__(self,name,salary):
      self.name=name
      self.salary=salary
   def __gt__(self,other):
      if self.salary > other.salary:
         return True
      else:
         return False
   def __eq__(self, value):
      if self.salary == value.salary:
         return True
      else:
         return False
      
   
e1 = Employee("Nour", 6000)
e2 = Employee("Ali", 4000)
print(e1 > e2)  # True
print(e1 == e2)  # False
#-----------------------------
# inheritance OOP
#1
"""Base class"""
class Animal:
   def __init__(self):
      pass

   def speak(self):
      return 'This animal makes a sound'
   
"""Derived class"""
class Dog(Animal) :
   def speak(self):
      return 'The dog barks'
ed=Dog()
print(ed.speak())

#-------------------------------
#2 Multiple Inheritance OOP

"""Base1 Class"""
class Flyer:
   def __init__(self):
      pass

   def fly(self):
      return "I can fly"
   
"""Base2 Class"""
class Swimmer:
   def __init__(self):
      pass
   def swim(self):
      return' I can Swim'
   
"""Derived Class"""
class Duck(Flyer,Swimmer):
   def __init__(self):
      pass
   def __str__(self):
      return f"{ self.fly() } and {self.swim()}"

duck=Duck()
print(duck)
      
#--------------------------------     
#3 Method Overriding OOP
"""Base class"""
class Person:
   def __init__(self):
      pass
   def greet(self):
      return 'Hello'
   
"""Derived class"""

class Student(Person):
   def __init__(self):
      pass
   def greet(self):
      return "Hello, I’m a student"

std=Student()
print(std.greet())
#---------------------------------
#4 Polymorphism OOP

class Cat:
   def __init__(self):
      pass

   def speak(self):
      return 'Meow'
   
class Dog:
   def __init__(self):
      pass

   def speak(self):
      return 'Woof'
   
cl1=Cat()  
cl2=Dog()
animal=[]
animal.append(cl1.speak())
animal.append(cl2.speak())
animal.append(cl1.speak())
animal.append(cl2.speak())
animal.append(cl1.speak())
animal.append(cl2.speak())
for x in animal:
   print(x)

#---------------------------------
#5 Encapsulation OOP

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")

ac = Account('NauRaa', 10000)
ac.set_balance(99999)
print(ac.get_balance())  # 99999

#-----------------------------------
#6
class User:
    def __init__(self, password):
        self.__password = password
   
    def set_password(self, new_password):
        if len(str(new_password)) < 6:
            return 'WARNING: Password too short'
        self.__password = new_password

    def get_password(self):
        return self.__password

ac = User("1234")
print(ac.set_password("abc"))         # WARNING
print(ac.set_password("secure123"))   # None (تم التغيير بنجاح)
print(ac.get_password())              # secure123

#----------------------------------
#OOP
#1
class Book :
   def __init__(self,title ,author, price):
      self.title=title
      self.author= author
      self.price=price

   def description(self):
      return f"{self.title} By: {self.author} and Costs: {self.price}"

   def __str__(self):
         return f"{self.title} By: {self.author} and Costs: {self.price}"

ac=Book('Power','NauRaa',1000)
print(ac)
      
#---------------------------------
#2
class Employee:
   company_name='Tech Corp'
   def __init__(self,name,salary):
      self.name=name
      self.salary=salary

   def increased(self,amount):
     # percentage=(self.salary *100)/100
     # return percentage + 0.1 
     return self.salary +amount
ac=Employee('Nauraa',1000)
print(ac.increased(100))

#--------------------------------
#3
class Student:
   students_count=0

   def __init__(self,name,degree):
      self.name=name
      self.degree=degree
      Student.students_count+=1
ac1= Student('NauRaa',96)  
ac2= Student('Nau',9) 
print(Student.students_count) 
ac3= Student('Nauaa',6)  
print(Student.students_count) 

#------------------------------
print('#'*10)
#4
class Calculator:
  
   @staticmethod
   def add(num1,num2):
      return num1 + num2
   
   @staticmethod
   def multiple(num1,num2):
      return num1 * num2
   
   @staticmethod
   def divide(num1,num2):
      return round(num1 / num2)
   
   @staticmethod
   def subtr(num1,num2):
      return num1 - num2
   
print(Calculator.add(2,3))
print(Calculator.subtr(10,5))
print(Calculator.multiple(5,1))
print(Calculator.divide(5,1))
#----------------------------------
#5
class Vehicle:
   def __init__(self):
      pass
   def move(self):
      pass

class Car(Vehicle):
   def __init__(self):
      pass
   def move(self):
      print('Moving')
ac= Car()
ac.move()
#----------------------------------
#6
class Cat:
   def speak(self):
      return 'Meow'

class Dog:
   def speak(self):
      return 'Woof'

cat = Cat()
dog = Dog()

print(cat.speak())
print(dog.speak())

#-------------------------------
#7
class Account:
   def __init__(self,name,balance):
      self.name=name
      self.__balance=balance

   def get_balance(self):
      return self.__balance
   
   def deposit(self,amount):
      return self.__balance + amount
   
   def withdraw(self,amount):
      return self.__balance - amount
ac=Account('NauRaa',1000)
#ac.deposit(10000)
#ac.withdraw(12)
print(ac.deposit(1000))
# الجيت مش شغالة بتجيب الرصيد من غير زيادة او نقصان او تغيير

print('#'*10)

#----------------------------------
#8
from abc import ABC, abstractmethod

class User(ABC):
   @abstractmethod
   def show(self):
      pass

class Admin(User):
   def show(self):
      return "Admin Panel"

#----------------------------------
#9
class Point:
   def __init__(self,x,y):
      self.x=x
      self.y=y
      
   def __add__(self, other):
      return Point(self.x + other.x, self.y + other.y)

ac1 = Point(10, 20)
ac2 = Point(5, 5)
res = ac1 + ac2
print(res.x, res.y)

#----------------------------------
#10
class Person:
   def __init__(self,name,age):
      self.name=name
      self.age=age

      def __eq__(self, other):
         return self.name == other.name and self.age == other.age

   

ac=Person('NauRaa' , 31)
ac2 =Person('Ahmed',20)
print(ac.name == ac2.name) 
print(Person.__eq__(ac , ac2)) 


















































































































































































     
      



















      



























































      









