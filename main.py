# IMPORTS HERE
from math import *

# print("Hello World")
# this hashtag mark makes a comment

"""
print("/___|")
print("   /|")
print("  / |")
# print()
print(" /  |")

print()

character_name = "Zeek"
character_age = "21"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age)

another_age = 41
# to print a number as a string try casting it to string format
print("I am printing " + str(another_age) + " which is an int rather than a string")

is_male = True
"""

# docstrings -> """ can create blocks of multi-line comments

"""

print("Giraffe\nAcademy")
phrase = "Zeek's Study Time"
print(phrase + "\nis well worth the effort\n")

print(phrase.lower() + "\t\t" + phrase.upper())

print(len(phrase))
print(phrase[0] + phrase[7] + phrase[13])
# this following print stmt is returning the
# location where the apostrophe is located in the string
print(phrase.index("'"))
print(phrase.index("Ti"))

# string.replace function
print("\n" + phrase.replace("Zeek's", "Cameron's"))
"""

# numbers

"""
print(-23.33)
print(3 + 7)
print(2 * 5)
print(12 / 3)

# modulo -> %. Read as "mod", divides a number and returns the remainder
# the following should return a 1.
print(15 % 2)

# python has the order of operations, notice the answer is 19 and not 27
print(4 + 5 * 3)
print((4 + 5) * 3)

my_num = 4
print(my_num)
# numbers can be converted to strings, useful when printing numbers with a string
print(str(my_num) + " this number rocks")

# math functions
# abs returns the absolute value of the number input
my_num = -5
print(abs(my_num))

# pow(base, exponent) == base^exponent
print(pow(3, 2))
print(pow(4, 3))

print(sqrt(64))

print(max(4, 7, 12))
print(min(4, 7, 12))

# find ways to adjust the rounding
print(round(3.2))
print(round(3.7))

print(floor(20.9))
print(ceil(20.9))
"""

# get input from users

"""
name = input("Enter your name here: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)
"""

# Build a calculator

"""
# getting input from user auto converts data to string, consider this when
# trying to get a number from a user
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# result = int(num1) + int(num2)
# the prev line assumes a user will enter only whole numbers
result = float(num1) + float(num2)

print(result)
"""

# mad libs 58:30        https://youtu.be/rfscVS0vtbw?t=3510

"""

"""
