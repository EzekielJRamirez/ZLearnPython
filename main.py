# IMPORTS HERE
from math import *

"""
print("Hello World")
# this hashtag mark makes a comment

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
print("Roses are red")
print("Violets are blue")
print("Today is sunny")
print("My favorite song is \"What she wants\"")
print("I love you\n")

color = input("Enter a color: ")
p_noun = input("Enter a plural noun: ")
weather = input("Enter a weather condition: ")
song = input("Enter your favorite song: ")
celeb = input("Enter a celebrity: ")

print()
print("Roses are " + color)
print(p_noun + " are blue")
print("Today is " + weather)
print("My favorite song is " + song)
print("I love " + celeb)
"""

# Lists

"""
# lists can be a mix of values
# lists are zero indexed
mix = [True, "James", 22]
friends = ["James", "Cameron", "Josh", "Mark", "Collin"]
nums = [0, 5, 10, 15, 20, 25, 30]

# to get the index starting from the back of the list, use a negative number
# in reverse the index begins at -1
print(friends)
print()
print(friends[0] + "\n")
print(friends[-1] + "\n")
# to exclude a value use the colon in brackets
print(friends[2:])
# to use a range of values use two numbers with a colon, the second value is exclusive.
# this means the values provided as borders won't be included. Otherwise it would be inclusive
print()
print(friends[3:5])
print(friends[1:3])

# modify only certain index of list
friends[1] = "Chris"
# the prev line changed Cameron to Chris
print(friends)
"""

# list functions

""" 
mix = [True, False, "Zac", "James", 15, 22]
friends = ["James", "Cameron", "Josh", "Mark", "Collin", "Zac", "Hovag"]
nums = [0, 5, 10, 15, 20, 25, 30, 35, 40]

# to append, add, to a list use the .extend function
# friends.extend(nums)
# friends.append("Tyler")
# difference between extend and append below
# https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend

# insert value at certain location and push the rest of the values by one
# friends.insert(1, "Kevin")
# friends.remove("Josh")
# print(friends)

# clear eliminates all values from the list
# friends.clear()
# print(friends)

# pop removes the last element from the list, useful in automating a list
# friends.pop()
# print(friends)

# to search list for specific value, provide the value in parenthesis and the list
# will return the index where that value is located, otherwise it will throw an error
print(friends.index("Mark"))

# to count how many times a value is in a list use count method
# print(friends.count("Mark"))
# print()
# friends.append("Mark")
# friends.append("Mark")
# print(friends.count("Mark"))

# to organize a list use sort
friends.sort()
print(friends)

# reverse the current order of list with .reverse method
friends.reverse()
print(friends)

# copy a list with the .copy method
friends2 = friends.copy()
print(friends2)
"""

# tuples

""" 
# tuples are immutable, they can't be changed or modified
coords = (2, 5, 7, 19)
# try to change tuple, should throw error
# coords[1] = 11
print(coords[0])

# Try making a list of tuples and experiment with that
"""

# Functions

"""
# name, age, and booly are params that are passed in to make the fxn more dynamic
def say_hi(name, age, booly):
    print("Hello " + name + " you are " + str(age))
    print("This sentence is... " + str(booly))
    print()
    # conventional naming in python functions is to use underscore on longer names
    # all code that is indented is considered part of the function

print("Top")
say_hi("Zeek", 21, True)
say_hi("Elijha", 20, False)
say_hi("Levi", 12, True)
print("Bottom")
"""

# return statement 1:34:17

""" 
def cube(num):
    # no code will work in a function after a return stmt
    return num*num*num;

base = 4
result = cube(base)
print(result)

def name(nm):
    print(nm + " is the name of the programmer")
    print("bannana mo-mana fee fi fo fanna\nBannana!")
    # nm.upper
    print(nm[0] + "annana")
    return nm[0] + "annana"

b_name = "Ezekiel"
b_name = name(b_name)
print("My new name is ")
print(b_name)
"""

# If Statements

""" """
