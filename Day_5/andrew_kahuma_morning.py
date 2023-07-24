import math as mtc
from abc import ABC, abstractmethod
# # Inheritance
# class Animal():
#     def __init__(self, name):
#         self.name = name
    
#     def eat(self):
#         print(f"{self.name} is eating ...")
        
# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} is barking...!!")

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} is meowing...!!")
        
# animal = Animal("Generic Animal")
# dog = Dog("Spot")
# cat = Cat("Fluffy")

# # Invoke Call Eat method 
# animal.eat()
# dog.bark()
# cat.meow()

# # Example 2; Demonstrating Inheritance 
# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
        
#     def display_info(self):
#         print("Brand:", self.brand)
#         print("Color:", self.color)
    
#     def move(self):
#         print("Moving the vehicle...")
        
# class Car(Vehicle):
#     def __init__(self, brand, color, num_wheels):
#         super().__init__(brand, color)
#         self.num_wheels = num_wheels
        
#     def display_info(self):
#         super().display_info()
#         print("Number of wheels:", self.num_wheels)
        
#     def honk(self):
#         print("Honking the horn...")
    
# # Create a Car Object
# my_car = Car("Toyota", "Red",4)

# # Access and modify car attributes
# print("Brand:", my_car.brand)
# my_car.color = 'Blue'

# # Invokr the car methods
# my_car.display_info()
# my_car.move()
# my_car.honk()

# # Exercise 1
# # Demonstrate using inheritance, calculate the area and perimeter of a circle and rectangle
# class Shape:
#     def __init__(self, length):
#         self.length = length
    
        
# class Circle(Shape):
#     def __init__(self, length):
#         super().__init__(length)
    
#     def display_radius(self):
#         print("Radius of the circle: ", self.length)
    
#     def calculate_area(self):
#         print(f"Area of the circle is {self.length**2 *mtc.pi}")
    
#     def calculate_circumference(self):
#         print(f"Circumference of the circle is {2*mtc.pi*self.length}")
        
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__(length)
#         self.width = width
    
#     def calculate_area(self):
#         print(f"Area of the rectangle is {self.width * self.length}")
        
#     def calculate_perimeter(self):
#         print(f"Perimeter of the rectangle is {(2*self.width) + (2*self.length)}")
        
# circle_inst = Circle(12)
# rectangle_inst = Rectangle(23,45)

# circle_inst.display_radius()
# circle_inst.calculate_area()
# circle_inst.calculate_circumference()
# rectangle_inst.calculate_perimeter()
# rectangle_inst.calculate_area()
        
# # Example 3
# # Multiple Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def eat(self):
#         print(f"{self.name} is eating...")
        
# class Flyable:
#     def fly(self):
#         print(f"{self.name} is flying...")
        
# class Bird(Animal, Flyable):
#     def __init__(self, name, species):
#         super().__init__(name)
#         self.species = species
        
#     def display_info(self):
#         print(f"Species: {self.species}")
#         print(f"Name: {self.name}")
        
# # Create a Bird object
# my_bird = Bird("Pigeon","Bird")

# # Invoke the Bird methods
# my_bird.eat()
# my_bird.fly()
# my_bird.display_info()

# # METHOD OVERRIDING
# class Animal:
#     def make_sounds(self):
#         print("Animal is making sounds")
        
# class Dog(Animal):
#     def make_sounds(self):
#         print("Dog is making sounds")
        
# class Cat(Animal):
#     def make_sounds(self):
#         print("Cat is making sounds")
        
# def make_animal_sounds(animal):
#     animal.make_sounds()
    
# animal = Animal()
# dog = Dog()
# cat = Cat()

# # Calling make_animal_sounds function
# make_animal_sounds(animal)
# make_animal_sounds(cat)
# make_animal_sounds(dog)

# # POLYMORPHISM; Allows you to write code that can woork with different objects
# # Method overriding
# # Method overloading

# # Example 4
# class Shape:
#     def calculate_area(self):
#         pass
    
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
        
#     def calculate_area(self):
#         return self.length * self.width
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
        
#     def calculate_area(self):
#         return self.radius * self.radius * 3.14
    
#     def calculate_circumference(self):
#         return 2 * 3.14 * self.radius
    
# rectangle = Rectangle(5, 5)
# circle = Circle(5)

# # Calculate display area
# print("Rectangle area:", rectangle.calculate_area())
# print("Circle area:", circle.calculate_area())

# # Overloading functions

# class Calculator:
#     def add(self, x, y):
#         return x + y
    
#     def add(self, x, y, c):
#         return x + y + c
    
# calculator = Calculator()

# # Display output
# # print(calculator.add(1, 2))  This raises an TypeError of a missing argument
# print(calculator.add(1, 2, 3))

# ABSTRACTION

# Exercise 2; Demonstrate abstraction using calculating area of a circle and rectangle
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return self.radius**2 * mtc.pi
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length * self.width
    
my_circle = Circle(34)
my_rect = Rectangle(23, 45)

print("Area of the circle:", my_circle.calculate_area())
print("Area of the rectangle:", my_rect.calculate_area())


# ASSIGNMENT
# RECEIPT PRINTING PROGRAM

import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from ttkthemes import ThemedTk


class ReceiptBook:
    def __init__(self, master_window):
        self.master_window = master_window
        self.master_window.title("Receipt Book")
        self.master_window.geometry("600x400")
        self.entries = []

        self.create_widgets()

    def create_widgets(self):
        instructions = "Enter the item, description, price, and quantity:"
        instruction_label = ttk.Label(self.master_window, text=instructions)
        instruction_label.pack(pady=10)

        form_container = ttk.Frame(self.master_window)
        form_container.pack()

        labels = ["Item:", "Description:", "Price:", "Quantity:"]
        variables = [tk.StringVar() for _ in range(4)]

        for i in range(len(labels)):
            label = ttk.Label(form_container, text=labels[i])
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entry = ttk.Entry(form_container, textvariable=variables[i])
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.entries.append(entry)

        create_receipt_button = ttk.Button(
            self.master_window, text="Create Receipt", command=self.create_receipt
        )
        create_receipt_button.pack(pady=10)

    def create_receipt(self):
        items = [entry.get() for entry in self.entries]
        if any(item == "" for item in items):
            messagebox.showerror("Error", "Please fill all the fields")
            return

        item, description, price, quantity = items
        total = float(price) * int(quantity)

        receipt = f"""
        Item: {item}
        Description: {description}
        Price: {price}
        Quantity: {quantity}
        Total: {total}
        """

        messagebox.showinfo("Receipt", receipt)

        for entry in self.entries:
            entry.delete(0, "end")

    def run(self):
        self.master_window.mainloop()


if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = ReceiptBook(root)
    app.run()

