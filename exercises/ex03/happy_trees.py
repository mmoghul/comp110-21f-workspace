"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

y: int = int(input("What is the depth? ")) 
x: int = 1
while x <= y:
    print(TREE * x)
    x += 1
