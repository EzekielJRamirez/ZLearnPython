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

""" """

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
