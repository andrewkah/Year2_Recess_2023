# EXERCISES 
# Lists
# Qn-1
First_name = ['Joe', 'John','Suzan','Eddie', 'Bryan']
print (First_name)
print (First_name[1])
# Qn-2; Change the first item
First_name[0]= "Frank"
print (First_name[0])

# Qn-3; Add the sixth item
First_name.append('Marrian')
print(First_name)

# Qn-4; Add the Bathel as the 3rd item
First_name.insert(2, 'Bathel')

# Qn-5; Remove the 4th item
First_name.pop(3)
print(First_name)

# Qn-6; Use negative indexing
print(First_name[-1])
print(First_name[-2])

# Qn-7; Use range of indices to print the third, fourth and fifth items.
num_items = [1, 23, 34, 12, 37, 42, 93]
print(num_items[2:5])

# Qn-8; list of countries and copy it
countries = ['US', 'Sudan', 'Britain', 'Uganda', 'Kenya']
countryCopy = countries.copy()

# Qn-9; loop through list of countries
for country in countries:
    print(country)

# Qn-10; Animal name list, sort them in descending and ascending order
animals = ['cow', 'dog', 'pig', 'lion', 'cat', 'sheep']
print(animals)
print("This is a sorted list of Animals: ",sorted(animals))
print(sorted(animals, reverse=True))

# Qn-11; animal names with 'a' in them
for i in animals: 
    if 'a' in i.lower():
        print(i)

# Qn-12; two lists, One for first names and other for second names. Join them
first = ['Joe', 'John', 'Faith', 'Jane']
second = ['Apim', 'Omona','Lyada']
full_names = [first + ' ' + second for first, second in zip(first, second)]
print(full_names)

# Exercise two; Tuples(like arrrays)
# Qn-1; output favorite brand
x = ("samsung","Iphone","techno","redmi")
print(x[3])

# Qn-2; using negative indexing
print(x[-2])

# Qn-3; update iphone to itel
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(x)

# Qn-4 add 'Huawei' to the list
x_list = list(x)
x_list.append("Huawei")
x= tuple(x_list)
print(x)

# Qn-5; loop through the tuple
for item in x:
    print(item)

# Qn-6; Remove the first item from the 
x_list = list(x)
del x_list[0]
x = tuple(x_list)
print(x)

# Qn-7; Create a new tuple using the constructor
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbale"])
print(cities)

# Qn-8; Unpack the tuple elements
P1, P2, P3, P4 = x
print(P1)
print(P2)
print(P3)
print(P4)

# Qn-9; Print a range
print(cities[1])
print(cities[2])
print(cities[3])

# Qn-10; join two tuples
first = ['Joe', 'John', 'Faith', 'Jane']
second = ['Apim', 'Omona','Lyada']
Join_tuple = first + second
print(Join_tuple)

# Qn-11; multiply 3 tuples
colors = ('red', 'green', 'blue', 'orange')
new_colors = colors*3
print(new_colors)

# Qn-12; number of times an element appears in the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
eight = thistuple.count(8)
print(eight)


# Exercise Three
# Sets
# Qn-1; set of three beverages
fav_beverages = set(['coffee', 'juice', 'tea'])
print(fav_beverages)

# Qn-2; add two items to the set
fav_beverages.add('soda')
fav_beverages.add('water')
print(fav_beverages)

# Qn-3; checking if an item is present in the set
mySet = {'Oven', 'kettle', 'microwave', 'refrigerator'}
if 'microwave' in mySet:
    print('Microwave is present in the set')
else:
    print('Microwave is not present in the set')

# Qn-4; Remove an item
mySet.remove('kettle')
print(mySet)

# Qn-5; loop through a set
for item in mySet:
    print(item)
    
# Qn-6; Add items to the set
myList = [12, 15]
mySet1 = {2, 4, 6, 7}
mySet1.update(myList)
print(mySet1)

# Qn-7; Joining two sets
ages = {3, 4, 5, 21}
names = {'joe', 'jack', 'janet', 'jethro'}
joinedSet = ages.union(names)
print(joinedSet)

# Exercise Four
# Strings
# Qn-1; Concatenate string and integer
int_var = 80 
str_var = "World"
conc = str(int_var)+str_var
print(conc)

# Qn-2; Remove spaces at the beginning and end of a string
text = "  Hello, Uganda!  "
stripped_text = text.strip()
print(stripped_text)

# Qn-3; Convert string to uppercase
text_uppercase = stripped_text.upper()
print(text_uppercase)

# Qn-4; replace characters
text_replace = stripped_text.replace('U', 'V')
print(text_replace)

# Qn-5; return the range of characters
y = "I am proudly Ugandan"
range = y[1:4]
print(range)

# Qn-6; 
# x = "All "Data Scientists" are cool!"
correct_x = 'All "Data Scientists" are cool!'
print(correct_x)

# Exercise Five
# Dictionaries
# Qn-1; return a value from the dictionary
shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print("The shoe size is: ",shoes['size'])

# Qn-2; change a value in the dictionary
shoes["brand"] = "Puma"
print('brand: ',shoes['brand'])

# Qn-3; add a new key/value pair to the dictionary
shoes['type'] = "sneakers"
print("Update: ",shoes)

# Qn-4; return the keys of the dictionary
keys = list(shoes.keys())
print('keys: ',keys)

# Qn-5; return the values of the dictionary
values = list(shoes.values())
print('values: ',values)

# Qn-6; check for size for the dictionary
if 'size' in shoes:
    print('The key, "size" exists in the dictionary')
else:
    print('The key, "size" does not exist in the dictionary')
    
# Qn-7; loop through the dictionary
for key, value in shoes.items():
    print('key: ',key, ', value: ',value)

# Qn-8, remove the color key
shoes.pop('color')
print(shoes)

# Qn-9; empty the dictionary
shoes.clear()
print('empty dictionary; ', shoes)

# Qn-10; makea copy of the dictionary
new_dict = {
    'int': 21,
    'strings': 'Hello',
    'double': 22.5,
}
dict_copy = new_dict.copy()
print(dict_copy)

# Qn-11; nested dictionary
dict_nested = {
    'shoes': {
    "brand": "Nick",
    "color": "black",
    "size": 40
    },
    'new_dict' : {
        'int': 21,
        'strings': 'Hello',
        'double': 22.5,
    }
}

