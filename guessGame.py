# import tools

# Guess Game

"""
secret_word = "giraffe"
guess = ""
guess_count = 0
# guess_limit = 3
out_of_guesses = False

guess_limit = int(input("How many guess attempts would you like?"))

while guess != secret_word and not(out_of_guesses):
    print("Guesses left: " + str(guess_limit - guess_count) + "\n")
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
        # print(guess_limit - guess_count)
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")
"""

# For Loop

"""
# what are the pro's and cons to each type of loop style?

# let stands for letter. You can use any name for individual values of str
# inside the for loop condition
for let in "Ezekiel Ramirez":
    print(let)

friends = ["James", "Cameron", "Josh", "Mark", "Collin", "Zac", "Hovag"]
for friend in friends:
    print(friend)

for index in range(15):
    # the num provided in range is exclusive starting at 0
    # it will show nums 0 - 14 with range(15)
    # it will show nums 5 - 9 with range(5, 10)
    print(index)

for index in range(15):
    if index == 0:
        print("First iteration")
    else:
        print("other")
        
"""

# Exponent Function

""" 
# 2**3 = 2^3
print(2 ** 3)


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        # result = result * base_num
        result *= base_num
    return result


new_num = raise_to_power(3, 2)

print(new_num)
"""

# 2D lists and Nested Loops

""" 

# we can build a list of lists
num_grid = [
    [1, 2, 3],  # row 0 -- cols 0, 1, 2
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# num_grid[0][1] should return 2
print(num_grid[0][1])
print(num_grid[1][2])

for row in num_grid:
    # print("row:\t" + str(row))
    print(row)

row_sel = int(input("What row would you like to pick"))

# if row is bigger than size of grid then throw error
# len checks the size of many data types and data structures
# https://www.digitalocean.com/community/tutorials/find-the-length-of-a-list-in-python
if row_sel > len(num_grid):
    print("Your selection is too big")
else:
    print(num_grid[row_sel])

for row in num_grid:
    for col in row:
        print(col)

"""

# Build a translator

"""
Giraffe Language
vowels -> z

dog -> dzg
cat -> czt


# take in a word and read word letter by letter
# then when it finds a vowel, replace it with z
def translate(phrase):
    trans = ""      # trans will be the word we return after changing the vowel
    for let in phrase:
        # going letter by letter through word
        if let in "AEIOUaeiou":
            # if the letter is a vowel then make the change
            # don't forget to preserve capitals if possible
            if let.isupper():
                trans += "Z"
            else:
                trans += "z"
        else:
            # else keep the original letter
            trans += let
    return trans

print(translate(input("Enter a phrase please ")))
"""

# Comments
'''
It is recommended by python to use hashes 
for multi-line rather than quotations
'''
""" """

# Try Except

""" 
If we can forsee a situation where the code may break
we can use a Try Except to stop errors from halting the code


try:
    num = int(input("Enter a number: "))
    print(num)
except:
    # sometimes your catch requirements may be too general
    # you may want to focus on more specific errors
    print("Invalid Input")

# best practice is to use specific error cases
try:
    test = 10 / 0
    num = int(input("Enter a number: "))
    print(num)
except ZeroDivisionError as err:
    # err could be named anything
    # err corresponds to a string that states 'division by zero'
    print(err)
except ValueError:
    print("invalid response")
"""

# Reading Files

""" 
the open() command takes in a path or file name to
know which file to read data from


# here I will use the files name becuase the python file and
# data file are in the same folder/directory

# the second parameter for open has four options
# r   (Read) This allows the program to read only from the target file
# a   (Append) This only allows the program to add data to the end of the file,
#     you won't be able to modify existing data
# w   (Write) This allows the program to change existing information and/or add new data
# r+  (Read and Write)

# what kind of data type stores the opening of another .txt file?
employee_file = open("employees.txt", "r")

# print("Is the employee file readable?")
# print(employee_file.readable())

# the .read commands read the appropriate amount of lines then move the cursor
# to the next spot so be aware of the order of your read statements
# print(employee_file.readline())

# print(employee_file.read())

# this readlines file takes all lines and puts them in a list
# you can even ask for specific lines this way
# print(employee_file.readlines()[1])
# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)


# don't forget to close files you work with
employee_file.close()
"""

# Writing to Files

""" 

# writing (w) over writes everything in the target file, BE CAREFUL
# opening a file that doesn't exist will create that file. employees1.txt is an example
# you can even write an html file in python
employee_file = open("employees1.txt", "a")
# when adding to a file, make sure you know if you need a newline character or indents
# employee_file.write("\nKelly - Human Services")
# print(employee_file.read())
employee_file.close
"""

# Modules and Pip

""" 
modules are python files that we can call to use from another file location
there will be some import statements down here so we know what was used,
normally they would appear at the top of the python file

you can also find modules written by other programmers, experiment with new ones!!!


import tools
# import docx
print(tools.roll_dice(22))
# find the python resources for the list of modules I can import
# Make sure it is for the version of python you are using
# https://docs.python.org/3.7/py-modindex.html

# https://python-docx.readthedocs.io/en/latest/

# Pip is a package manager that handles the download of third party modules/installations
# my pip and python wouldn't run in the command prompt window
# when you add python for the first make sure you check that the path option is clicked ON
# https://www.geeksforgeeks.org/how-to-install-pip-on-windows/
"""

# Classes and Objects

""" 

from Student import Student
# read as 'from the student file, get the student class
Student1 = Student("Zeek", "Computer Science", 3.5, False)
# the class is like a template and the instance is an actual student
print("Name: " + Student1.name)
print("Major: " + Student1.major)
print("GPA: " + str(Student1.gpa))
print("Probation: " + str(Student1.probation))
"""

# Multiple Choice Quiz

""" 

from Question import Question

# here is the list of questions and the available responses
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# this list is taking the prompts and putting the values into an instance of the
# question and setting what answer is correct
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


# create a method to iterate through questions
# keep track of the player's score
# take in the list of questions and track their correct answers
def run_test(questions):
    score = 0
    for que in questions:
        answer = input(que.prompt)
        if answer == que.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)

# maybe I should try to make my own test
"""

# Object Functions

""" """
from Student import Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
