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

""" """
