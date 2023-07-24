# Arithmetic Operators 
# + Addition operator
a = 10 + 29
print(a)
# - Subtraction operator
b = 20 -13
print(b)
# * Multiplication operator
c = 38 * 0.5
print(c)
# / Divide operator
d = 58 / 15
print(d)
# // Divide operator; ==return the quotient without the remainder
e = 48 // 12
print(e)
# % Modulus operator; ==to get the remainder
f = 62 % 12
print(f)
# ** Exponentiation operator; ==raise a number to a power
g = 0.5 ** 0.5
print(g)


# -Comparison Operators
a = 20
b = 46
# == Equal to
print(a == b)
# != Not Equal to
print(a != b)
# > Greater than
if ( a > b ) : print("a is greater than b")
else : print("b is greater than a")
# < Less than
if ( a < b ) : print("a is less than b")
# <= Less than or equal to
if ( a <= b ): print("a is less than or equal to b")
# >= Greater than or equal to
if ( a >= b): print("a is greater than or equal to b")
else : print("b is greater than or equal to a")

# -Logical Operators
a = True
b = False
# Logical AND 'and'
if a and b: 
    print("Both are true") 
    print(a and b)
else: print("Both are false")
# Logical OR 'or'
if a or b: print(a or b)
# Logical NOT 'not'

# -Assignments Operators
c = 9
d = 8
# Assign value; '='
# Add value; '+'
# Add and assign value; '+='
d += c
print(d)
# Subtract and assign value; '-='
c -= d
print(c)
# Divide and assign value; '/='
d /= 2
print(d)

# -Memberships Operators
phones = ['Iphone', 'Samsung', 'Techno', 'Infinix', 'Xiaomi', 'Huawei']
print(phones)
# In; 'in' operator; checks if a value exists in a sequence
if 'Iphone' in phones:
    print('Iphone is a phone!')
# Not in; 'not in' operator; checks if a value doesnt exist in a sequence
if 'Hp' not in phones:
    print('Hp is not a phone!')

# -Identity Operators
# Is; 'is' operator; checks if two values are the same
# Is not; 'is not' operator; checks if two values are not the same
e = 23
f = 23
print(e is f)
print(e is not f)

# Bitwise operators; perform operations on individual bits of binary numbers
# Bitwise AND ('&&'); Performs a bitwise AND operation between the corresponding bits of two integers
# Bitwise OR ('||'); Performs a bitwise OR operation between the corresponding bits of two integers
# Bitwise XOR ('^'); Performs a bitwise XOR operation between the corresponding bits of two integers
# Bitwise NOT ('~'); Performs a bitwise NOT operation between the corresponding bits of two integers
# bitwise left shift ('<<'); Performs a bitwise left shift operation between the corresponding bits of two integers
#  Bitwise right shift ('<<'); Performs a bitwise right shift operation between the corresponding bits of two integers

