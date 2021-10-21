"""Finding duplicate letters in a word."""

__author__ = "123456789"

word: str = input("Enter a word: ") 

duplicate: bool = False 
x: int = 0 

while x < len(word):
    y: int = x + 1

    while y < len(word):

        if(not duplicate):
            duplicate = word[x] == word[y]

        y += 1
    x += 1
        
        
print("Found duplicate: " + str(duplicate))