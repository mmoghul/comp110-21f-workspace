from random import randint

points: int = 0
NAME: int = 2
PATH: int = 5
DEFEAT: int = 10
MUSH: int = 2 
player: str = " "
MUSHROOM = '\U0001F344' 

def greet() -> None: 
    global points
    print("Greetings, welcome to the Enchanted Forest, a serene but spooky wonderland teeming with life- both pure and evil. Throughout your quest, your choces will determine which of these beings you will encounter and your fate at each step.")
    player = input("But first, please enter your name, brave explorer: ")
    points += NAME 
    print("Currently, {player} you have {points} points for entering your name. points are earned by successfully defeating wicked beasts and by claiming the magic mushrooms presented throughout your adventure. Entering your name is 2 points added, choosing a path is 5 points added, defeating your opponent is 10 points added, and accepting a mushroom prize is 2 points added. The maximum number of points, therefore, is 19. Choose one of the three paths below to begin your journey through the woods and earn points.")

def dosmth(emoji, inputStr, goStr) -> None:
    # pathone: int = input("Excellent choice, courageous one. Select a number between 1 and 6 to recieve a weapon. ") 
    print(emoji)
    print(inputStr)
    print(goStr)

def a() -> None:
    global points
    points += PATH 
    print("you have now entered the candid cave. You reluctantly walk towards it and peer inside the cool interioir before stepping in. As you trek through, you hear your footsteps echoing and bats screeching. A strange chill floods over you, putting your hairs on end. A blood-curdling screech fills the cave. You step back, dazed. But it is too late. A billowing, shadowy figure emerges. You tremble in fear as Barefoot himself towers above you. What will you do?")
    print("You have {points} points for entering the cave. ")
    print("You can turn around now and end the game, forgoing future points and a chance at completing your mission, guaranteeing death at the hands of the beast. Step up to challenge this monster, however, and you may survive and continue. What will it be?") 
    x: str = input("Type 'X' to run away or 'Y' to fight Bigfoot.")
    if x == 'X': 
        print("END OF GAME. Bigfoot caught you before you could escape. Your score was {points}")
    elif x == "Y": 
        pathone: int = int(input("Excellent choice, courageous one. Select a number between 1 and 6 to recieve a weapon. "))
        if pathone == 1:
            
            dosmth("\U0001F4A4", "You have recieved a sword to fight Bigfoot.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")
        elif pathone == 2:
            dosmth("\U0001F3F9", "You have recieved an arrow to fight Bigfoot.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")  
        elif pathone == 3:
            dosmth("\U0001F4A3","You have recieved a bomb to fight Bigfoot.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!") 
        elif pathone == 4:
            dosmth("\U0001F5E1","You have recieved a dagger to fight Bigfoot.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")      
        elif pathone == 5:
            dosmth("\U0001FA93","You have recieved an axe to fight Bigfoot.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!") 
        elif pathone == 6:
            dosmth("\U0001F52B","You have recieved a pistol to fight Bigfoot.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!") 

def b() -> None:
    global points
    points += PATH 
    print("you have now entered the squalid swamp. The slimy and frigid water tickles your toes as you stare into the murky liquid. Slowly, you wade into the algae- filled swamp. You grimace as you feel aquatic life move around your legs. You are hip- deep when you hear a loud roar. The muddy floor beneath your feet quivers and your eyes widden, giving you a full view of the enormous ogre that rises out of the water. What will you do? ")
    print("You have {points} points for entering the swamp. ")
    print("You can turn around now and end the game, forgoing future points and a chance at completing your mission, guaranteeing death at the hands of the ogre. Step up to challenge this monster, however, and you may survive and continue. What will it be?") 
    x: str = input("Type 'X' to run away or 'Y' to fight the ogre.")
    if x == 'X': 
        print("END OF GAME. the ogre caught you before you could escape. Your score was {points}")
    elif x == "Y": 
        print("Excellent choice, courageous one. An element power is being summoned for you")
        pathone: int = randint(1,6)
        if pathone==1:
            dosmth("\U0001F30A","You have recieved a water power to fight  the ogre.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")
        elif pathone == 2:
            dosmth("\U0001F32A","You have recieved an air power to fight the ogre.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")  
        elif pathone == 3:
            dosmth("\U0001F30E","You have recieved an earth power to fight the ogre.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!") 
        elif pathone == 4:
            dosmth("\U0001F525","You have recieved a fire power to fight the ogre.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")      
        elif pathone == 5:
            dosmth("\U00002604","You have recieved a comet power to fight the ogre.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!") 
        elif pathone == 6:
            dosmth("\U000026A1","You have recieved a lightning power to fight the ogre.", "A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!") 

def c() -> None:
    global points
    points += PATH 
    print("you have now entered the candid cave. You reluctantly walk towards it and peer inside the cool interioir before stepping in. As you trek through, you hear your footsteps echoing and bats screeching. A strange chill floods over you, putting your hairs on end. A blood-curdling screech fills the cave. You step back, dazed. But it is too late. A billowing, shadowy figure emerges. You tremble in fear as Barefoot himself towers above you. What will you do?")
    print("You have {points} points for entering the cave. ")
    print("You can turn around now and end the game, forgoing future points and a chance at completing your mission, guaranteeing death at the hands of the witch. Step up to challenge this monster, however, and you may survive and continue. What will it be?") 
    x: str = input("Type 'X' to run away or 'Y' to fight the witch.")
    if x == 'X': 
        print("END OF GAME. the witch caught you before you could escape. Your score was {points}")
    elif x == "Y": 
        available: int = availableWeapons(points)
        pathone: int = int(input("Excellent choice, courageous one. Select a number between 1 and {available} to recieve a weapon. "))

        while pathone > available:
            pathone = int(input("Select a number between 1 and {available} to recieve a weapon. "))
        if pathone == 1:
            dosmth("\U0001F52E","You have recieved a crystalball to fight the witch.", "A loud thud marks the end of the witch. Hurray! You have slain the beast!")
        elif pathone == 2:
            dosmth("\U0001FA84","You have recieved a wand to fight the witch.", "A loud thud marks the end of the witch. Hurray! You have slain the beast!")  
        elif pathone == 3:
            dosmth("\U0001F48E","You have recieved a gem to fight the witch.", "A loud thud marks the end of the witch. Hurray! You have slain the beast!") 
        elif pathone == 4:
            dosmth("\U0001F9EA","You have recieved a potion to fight the witch.", "A loud thud marks the end of the witch. Hurray! You have slain the beast!")      
        elif pathone == 5:
            dosmth("\U0001F300","You have recieved a hypnosis power to fight the witch.", "A loud thud marks the end of the witch. Hurray! You have slain the beast!") 
        elif pathone == 6:
            dosmth("\U0001F4A4","You have recieved a sleep spell to fight the witch.", "A loud thud marks the end of the witch. Hurray! You have slain the beast!") 

def availableWeapons(points) -> int:
    if points<=0:
        return 3
    elif points <=10:
        return 5
    elif points <= 25:
        return 6
        
def main() -> None: 
    global points
    global MUSHROOM
    greet()

    x: str = input("type 'a' to enter the candid cave. type 'b' to enter the squalid swamp. type 'c' to enter the treacherous tunnel. ")
    while x!= "q":
        if x=="a":
            a()
        elif x=="b":
            b()
        elif x == "c": 
            c()
        else:
            print("bad input ending")
            break
        points += DEFEAT
        print("You earned 10 points for defeating this evil lifeform. Your score is now {points}")
        print(MUSHROOM)
        choiceone: str = input("Would you like this mystical mushroom as a reward? Type 'yes' or 'no'. ")
        if choiceone == "yes":
            points += MUSH
            print ("Wise choice. You now have {points} points. Congratulations for defeating your opponnet.")
        else: 
            print("Very well. The game is now over. Your final score was {points}")
        x: str = input("type 'a' to enter the candid cave. type 'b' to enter the squalid swamp. type 'c' to enter the treacherous tunnel. Type 'q' to quit, else choose another path. ")
    print ("Very well. The game is now over. Your final score was {points}")    


if __name__ == "__main__":
    main()