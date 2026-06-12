import random

# function to generate random numbers
def do_something(count, out_list):
    for i in range(count):
        out_list.append(random.random())   # add random number between 0 and 1

# create empty list
numbers = []

# how many random numbers we want
count = 5

# call the function
do_something(count, numbers)

# print the result
print("Random numbers list:")
print(numbers)