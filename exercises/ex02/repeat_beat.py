"""Repeating a beat in a loop."""

__author__ = "730317780"


# Begin your solution here...

x: str = str(input("What beat do you want to repeat? "))
y: int = int(input("How many times would you like to repeat it?"))
if y <= 0: 
    print("No beat...")

result: str = ("")

while y > 0:
    y = y - 1
    result = result + x + " "

print(result[:len(result) - 1])