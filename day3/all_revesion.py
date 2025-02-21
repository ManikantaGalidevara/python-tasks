numbers = 145
numbers2 = 66

print(numbers+numbers2)

print(type(numbers2))

strings = "hello python world"
print(strings[6])
print(strings[0])
print(strings[2])
print(strings[-1])
print(strings[-5])

print(type(strings))

print(strings[1:6])
print(strings[-1 : -8 : -1])
print(strings[::2])

#data types 
# numeric -- int, float, complex, bool
#sequence -- list, tuple, string, range
# set
#dictionary
#none

#complex
complex11 = 2 + 5j
complex1 = 4 + 10j
print(type(complex11))
print(complex11 + complex1)
print(complex11 ** complex1)

#boolean -- true or false

print(2>3)
print(2<3)

print(int(True))
print(int(False))

#sequences
list1 = [1, 2, 3, 4, 5, 10,-1, 'String', True, [1, 2, 6]]
print(list1[4])
temp = list1[9]
print(temp[2])
print(list1[9][2])

for i in list1:
    print(i)

tup1 = (1, 2, True, "Str1", 0.9)
tup1 = (1,3)
print(tup1)

print(list(range(0, 101)))

#operators
#arthematic operators -- +, -, *, /, %, //, **
#relational operator---- =, <=, >=, <, >, !=
#assignment operator----  +=, -=, =, *=, /=, %=, //=, **=
#logical operator---  and, or, not
#bitwise operators--- &, |, ^, >>, <<, ~


int_numbers = 60
int_numbers2 = 40

#assignment operators
print(int_numbers + int_numbers2)
print(int_numbers - int_numbers2)
print(int_numbers * int_numbers2)
print(int_numbers / int_numbers2)
print(int_numbers % int_numbers2)
print(int_numbers ** int_numbers2)
print(int_numbers // int_numbers2)

int_numbers = int_numbers + 20
print(int_numbers)
print(int_numbers + int_numbers2)
int_numbers += 1
int_numbers -= 2
int_numbers *= 2
int_numbers /= 2
print(int_numbers)

#relational operators
greater_number = 6
greater_number2 = 10

print(greater_number > greater_number2)
print(greater_number < greater_number2)
print(greater_number == greater_number2)
print(greater_number != greater_number2)
print(greater_number <= greater_number2)
print(greater_number >= greater_number2)

#logical operators
print(True and True)
print(False and True)
print(True and False)
print(False and False)
print(1 and [])
print('' and True)
print(-1 and -2)
print(2 and 3)
print(0 and 2)

#Or gate
print(False or False)
print(True or False)
print(False or True)
print(True or True)
print(2 or 3)
print(3 or 2)
print(0 or 2)
print(2 or 0)
print('' or True)
print(1 or [])
print(-1 or -2)

#Not operator.

print(not True)
print(not False)


#bitwise operators
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)  # 1 (0101 & 0011 = 0001)
print(a | b)  # 7 (0101 | 0011 = 0111)
print(a ^ b)  # 6 (0101 ^ 0011 = 0110)
print(~a)     # -6 (~0101 = -0110)
print(a << 1) # 10 (0101 << 1 = 1010)
print(a >> 1) # 2  (0101 >> 1 = 0010)
#conditional statement-if,else, elseif
#if
x = 10
if x > 5:
    print("x is greater than 5")
#else
x = 2
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
#elseif
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is less than or equal to 5")
#loop-while,for
# Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#while
# Print numbers from 0 to 4
x = 0
while x < 5:
    print(x)
    x += 1  # Increment x
#jump statement-continue,break
# Using break to exit a loop
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
#continue
# Using continue to skip an iteration
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)
#functions-define,calling, return statement
#def function_name(parameters):
    # Function code
    # Return a value (optional)
def greet():
    print("Hello, welcome to Python functions!")

greet()  # Calling the function
#parameter and arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30)  # Passing arguments
#return statement
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
#inbuild functions
#print()
print("Hello, world!")
#len()
name = "Alice"
print(len(name))  # Length of the string
#type()
x = 10
print(type(x))  # Type of x
#int(),flost(),str()
x = "25"
y = int(x)  # Convert string to integer
print(type(y))  # Output: <class 'int'>
#sum()
numbers = [1, 2, 3, 4]
print(sum(numbers))  # Sum of numbers in the list
#min and max()
numbers = [10, 20, 30, 5]
print(min(numbers))  # Output: 5
print(max(numbers))  # Output: 30
#function literables-range
#range()
numbers = [10, 20, 30, 5]
print(min(numbers))  # Output: 5
print(max(numbers))  # Output: 30
#sorted-it is arrange the asscending order
numbers = [10, 20, 30, 5]
print(min(numbers))  # Output: 5
print(max(numbers))  # Output: 30
#reverse()
numbers = [1, 2, 3, 4]
print(list(reversed(numbers)))  # Reversed list
#filter()
numbers = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))  # Output: [2, 4, 6]