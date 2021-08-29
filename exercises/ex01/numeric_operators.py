"""Hypemachine with inputs and strings"""

__author__ = "730317780"

l: str = input("What is x? ")
r: str = input("What is y? ")

print(l + " ** " + r + " is " + str(float(l) ** float(r)))
print(l + " / " + r + " is " + str(float(l) / float(r)))
print(l + " // " + r + " is " + str(float(l) // float(r)))
print(l + " % " + r + " is " + str(float(l) % float(r)))