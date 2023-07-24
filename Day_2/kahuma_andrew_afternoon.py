# Dictionaries
# We store key/value pairs in dictionaries
# Example

myDict = {
    "name": "Lenovo",
    "model": "Thinkpad",
    "description": "This is a unqiue laptop with several useful features,......",
    "year": 2016
}
print(myDict)
# datatype and length of this dictionary
print("The datatype of this dictionary: " , type(myDict))
print("The length of this dictionary: " ,len(myDict))

# Accessing the dictionary
itemDescription = myDict["description"]
print("The description of the dictionary:", itemDescription)
y = myDict.get("name")
print(y)
w= myDict.keys()
print(w)

# loops
for x in myDict:
    print (myDict[x])

# adding an item to the dictionary
myDict["color"] = "gray"
print(myDict)

print("=========Start of Exercises ===========")
# EXERCISE ONE
# use the values()
itemvalues = myDict.values()
print(itemvalues)

# EXERCISE TWO
# check if the key does exist in the dictionary
if myDict["color"] == True:
    print("Color attribute does exist!")
    
# EXERCISE THREE
# How to change/update the dictionary
myDict["color"] = "black"
print(myDict["color"])

textDict = {
    "screen": "16inches",
    "RAM": "8024MB"
}
myDict.update(textDict)

# EXERCISE FOUR
# How to add to and remove from the dictionary
myDict["ROM"] = "500GB" # ROM size was added
print(myDict.keys)
# To remove an item, we can use pop() or popitem()
myDict.pop("screen")
print(myDict)

# EXERCISE FIVE
# Looping through and nesting dictionaries
for key, value in myDict.items():
    print(key, value)
# nesting dictionaries
newDict = {1 : myDict, 2 : {"name": "Hp","model": "Envy","year": 2020}}
print(newDict)

print("=======End of Dictionary Exercises =====")

# NUMBER
number = 20
# Converting from integer to float
numberFloat = float(number)
print(type(numberFloat))
print(numberFloat)
# Convert from float to complex number
compNumber = complex(numberFloat)
print(type(compNumber))
print(compNumber)

# CASTING
val = int("123456789")
print(type(val))

# STRINGS
# strings as an array
b = """Evening string"""
print(b[1])

# Removing whitespaces
c = "  Big numbers as an array  "
print(c.strip())

# Concatenating strings
d = "Good"
e = "boy"
f = d + e
print(f)

print("=========Start of String Exercises ===========")
# EXERCISE One
# length of a string
len(b)

# EXERCISE Two
# for loop of string
for i in b:
    print(i.upper())

# EXERCISE Three
# slicing of a string
print(b[2:9])

# BOOLEANS
print("=========Start of Boolean Exercises ===========")
# EXERCISE
# using booleans
num = (20>20)
if(num is True):
    print("The boolean is true")
else: 
    print("The boolean is false")