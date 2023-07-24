# FUNCTIONS

# def greet1():
#     print('Hello everyone')
    
# def greet2(name):
#     print('Hello ', name,'. You are welcome')
    
# greet1()
# greet2('Jane')

# def greet3(name, age = 20):
#     print(f"Hello {name}, Your age is {age}")
    
# greet3('Jane')

# def sum_all(*numbers):
#     sum = 0
#     for sum in numbers:
#         sum += 1
#         print(sum)
        
# sum_all(1,2,3,4)

# # Modules
# import module
# print(module.product(2,4))
# print(module.add(23,44))

# # We can use aliases here to shorten the names of modules
# from math import *
# import math as mtc

# x = mtc.sin(90)
# print(x)
# print(mtc.sqrt(36))


# # INPUT AND OUTPUT
# # example 1
# name = input('Enter your name: ')
# print(f"name: {name}")

# # example 2
# num = int(input('Enter a number: '))
# product = num *8
# print(product)

# multiple inputs
s, r, w = map(int, input('Enter your values: ').split())
print('The values are:',end = " ")
print(s,r)

# # capture input from a tuple
# w=(2,3,5,12)
# print('Current tuple')
# print(w)
# print(type(w))

# E = list(w)
# E.append(int(input('Enter your value: ')))
# w = tuple(E)
# print('Updated tuple:',w)

# myList = list(map(int, input("Enter your list value: ").split()))
# my_set = set(map(int, input("Enter your set value: ").split()))

# print(myList, type(myList))
# print(my_set, type(my_set))