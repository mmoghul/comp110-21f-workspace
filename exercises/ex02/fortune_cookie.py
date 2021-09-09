"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730317780"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

from random import randint
print(randint(0, 50))
x = randint(0, 50)
print(x)

# Begin your solution here... 

if x < 20:
    print("A")
else:
    if x > 30:
        print("B")
    else: 
        if x <= 27:
            print("C")
        else: 
            print("D")

print("Your fortune cookie says...")

print("you will do well on your next comp sci quiz!")

print("Now, go spread positive vibes!") 
