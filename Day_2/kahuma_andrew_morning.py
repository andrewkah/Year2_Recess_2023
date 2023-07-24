""" 
Control flow is a statement that allows you to control how a program should flow.
WE use conditional statements like (if-elif-else)
"""
# example code 1 
age = 19
if age < 18:
    print("You are underage!!")
elif age >= 18 and  age < 65:
    print("You are an adult!")
else:
    print("You are an elder!!")

num = int(29)
if num%2 != 0:
    print("You are odd!")
else:
    print("You are even!")

# Loops
cars = ["Benz", "Jaguar", "Ford", "Subaru", "Audi"]
for car in cars:
    print(car[0], car[3])
for i in range(0,10,3):
    print(i)

for i in range(10,0,-2):
    print(i)


# Exception handling (try, except, finally)
# Exercise
ratings = {
    1: "You are in very poor health, in need of immediate help!",
    2: "You are in poor health, in need of help!",
    3: "Your mental health is quite low, in need of help!",
    4: "Your mental health is low!",
    5: "Your mental health is average!",
    6: "Your mental health is just above average!",
    7: "Your mental health is quite good!",
    8: "Your mental health is good enough!",
    9: "Your mental health is very good!",
    10: "Your mental health is excellent, keep it up!"
}

try:
    scale = int(input("Please enter a scale from 1-10: \n"))
    if scale in range(1,10):
        print(ratings[scale])
    else:
        print("Invalid scale, please enter a scale from 1-10") 
                                               
except ValueError:
    print ("Invalid scale, please enter a correct number!")
    exit()