# Python OOP Concepts: Classes, Objects, Encapsulation, Inheritance, Polymorphism, Abstraction
# 1. Classes
# class Car:
#     def __init__(self, make, model,year):
#         self.make = make
#         self.model = model
#         self.year = year
        
#     def start_engine(self):
#         print('Engine started')
        
#     def stop_engine(self):
#         print('engine stopped')
        
# my_car = Car('Toyota', 'Corolla', 2002)
# my_car.start_engine()
# my_car.stop_engine()

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def calculate_area(self):
#         return self.width* self.height
    
#     def calculate_perimeter(self):
#         return 2*(self.width+self.height)
    
# my_rect = Rectangle(15,25)
# print(my_rect.height)
# print(my_rect.width)
# # Calculate the area and perimeter of the rectangle
# print(my_rect.calculate_area())
# print(my_rect.calculate_perimeter())

# class Student:
#     def __init__(self, name, year, course):
#         self.name = name
#         self.year = year
#         self.course = course
        
#     def display_details(self):
#         print('name:', self.name, '\nyear:', self.year, '\ncourse:',self.course)
        
# my_student = Student('Joe', 2019, 'BSSE')
# my_student.display_details()


# # 2.Objects
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def greet(self):
#         print ("Hello, my name is", self.name)
#         print("I am", self.age, "years old")

# # Create a  Person object
# my_p1 = Person('John', 29)
# my_p2 = Person('Jane', 30)
# my_p1.greet()


# # Exercise 1; Calculate the area of a circle

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def calculateArea(self):
#         return 3.14 * self.radius^2
    
#     def calculate_circumference(self):
#         return 2 * 3.14 * self.radius
    
# my_circle = Circle(76)
# print(my_circle.radius)
# print(my_circle.calculate_circumference())
# print(my_circle.calculateArea())

# Exercise 2; Calculate and display the employee's bonus
# class EmployeeBonus:
#     def __init__(self, id ,salary):
#         self.id = id
#         self.salary = salary
        
#     def calculate_employee_bonus(self):
#         return int(0.15 * self.salary)

# employee1 = EmployeeBonus('12006',150000)
# employee2 = EmployeeBonus('12017',230000)

# print('The bonus for employee',employee1.id,'is', employee1.calculate_employee_bonus())
# print('The bonus for employee',employee2.id,'is', employee2.calculate_employee_bonus())


# # 3. Encapsulation
# # Key goals of encapsulation
# """ 
# 1. To hide the implementation details of an object
# 2. To protect the object from changes
# 3. To protect the object from external changes
# """
# # Examples

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number # Encapsulates the account number attribute
#         self._balance = balance # Encapsulates the balance attribute
        
#     def deposit(self, amount):
#         self._balance += amount # Encapsulates the deposit amount attribute
        
#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#         else:
#             print('Insufficient funds to withdraw.')
        
#     def get_balance(self):
#         return  self._balance
    
# my_account = BankAccount(123343, 232100)
# my_account.deposit(2000)
# print(my_account._balance)
# my_account.withdraw(100)
# print(my_account._balance)

# # Exercise 2; convert 37 Celsius degress to Fahrenheit
# class Temperature:
#     def __init__(self, temp):
#         self.__temp = temp
        
#     def temperature_F(self):
#         return (self.__temp * 9/5) + 32
    
# temp_F = Temperature(37)
# # temp_F.__temp = 29
# print(temp_F.__temp)
# print('37 degress celsius is',temp_F.temperature_F(),'degrees Fahrenheit') 

# Assignment; Show encapsulation with employee information to give a pay incrementation (Salary with employee information to new_salary) e.g from 850000 to 1000000  
class Employee():
    def __init__(self, payment):
        self._payment = payment
        
    def increment_salary(self, increment = 150000):
        print("Increment to new salary:", (self._payment + increment))
        
new_salary = Employee(850000)
new_salary.increment_salary()
