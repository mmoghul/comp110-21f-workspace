"""Hypemachine with inputs and strings"""

__author__ = "730317780"

l: int = int(input("What is x? "))
r: int = int(input("What is y? "))

print(str(l) + " > " + str(r) + " is " + str(l > r))
print(str(l) + " >= " + str(r) + " is " + str(l >= r))
print(str(l) + " == " + str(r) + " is " + str(l == r))
print(str(l) + " != " + str(r) + " is " + str(l != r))