# EXCEPTION HANDLING
# Types of exceptions 

# SyntaxError; Raised when the syntax of the code is incorrect
# E.g. prin("Hello, world"), will raise SyntaxError because of the misspelled keyword 'print'

# TypeError; Raised when a function/operation is applied to an object of wrong type
# num_sum = 'joe' + 2

# NameError; Raised when a variable/function name is not found in the current scope
# print(num)

# IndexError; Raised when index of a data structure is out of bounds
# data = [1,2,34]
# print(data[3])

# KeyError; Raised when a key in a data structure is not found
# data1 = {'name': 'Joe', 'age': 44}
# print(data[height])

# ValueError; Raised when a method is called with a wrong argument or input.
# AttributeError; Raised when an attribute is not found on an object.
# IOError; Raised when an I/O operation fails dueto an input
# ZeroDivisionError; Raised when a number is divided by zero
# ImportError; Raised when an import statement fails to find a module

# Try-catch block to resolve exceptions
data2 = [45,56,67,78]
try:
    print(f'Third element = {data2[2]}')
    print(f'Fifth element = {data2[4]}') # Throws error since there are only four elements
except IndexError:
    print("IndexError: Index selected is out of bounds")
finally:
    print('Code is executed')
    

# FILE HANDLING
# First open the file with the open() function. It takes the name of the file and the purpose of opeing the file, as parameters
""" 
Different modes that are supported;
r:: open an existing file for a read operation
w:: open an existing file for a write operation. If data exists in the file, it will be overridden, otherwise a file will be created if missing
a:: open an existing file for append operation. It wont override exsiting data.
r+:: To read and write data in the file. Prevoius data will be overridden
w+:: towrite and read data. Will override existing data.
a+:: To append and read data in the file. Prevoius data wont be overridden
"""
import os
def file_read():
    file = open('file_text.txt', 'r')
    print(file.read())
    
def file_write():
    # We can use the written statement with the with() function
    with open('file_text.txt', 'w') as f:
        f.write("This is the second statement")
    
    file = open('file_text.txt', 'w')
    file.write("This is the first statement in the file!!")
    file.write('The write function allows us to write to the file.')
    file.close()

    
def file_append():
    file = open('file_text.txt', 'a')
    file.write('An added line in the file')
    file.close()

def read_write_file():
    with open('file_text.txt', 'r+') as f:
        f.read()
        f.write("Another added line in the file")
        f.close()
        
def write_read_file():
    with open('file_text.txt', 'w+')as f:
        f.write("Overriden text has been deleted!")
        f.close()
        
def file_rename():
    os.rename('file_text.txt', 'new_file_text.txt')
    print('file_text renamed to new_file_text successfully')

def file_delete():
    os.remove('new_file_text.txt')
    print('new_file_text successfully deleted!')

file_write()
file_append()
read_write_file()
write_read_file()
file_read()
file_rename()
file_delete()
    