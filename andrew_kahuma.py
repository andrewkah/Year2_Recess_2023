# Exercise 1; Sets
groceries = {'banana', 'pears', 'cakes', 'tomatoes', 'eggs'}
print(groceries)
# Length of the Set
print("There are", len(groceries), "groceries.")

# Datatype of the Set items
print("The groceries set contains; ", type(groceries))

# Accessing the set items
print("These are the items; ",)
for item in groceries:
    print(item)

# Adding items to the set
print("We are adding cabbage to the set")
groceries.add("cabbage")
print("This is the new set; ", groceries)
# Adding two items to the set
print("We are adding two items to the set")
groceries.update(["salt", "masala"])
print("This is the new set; ",groceries)

