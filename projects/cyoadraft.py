# prompt user to choose  path a (custom procedure call), path b (custom function call)

POINTS: int = 0
NAME: int = 2
PATH: int = 5
DEFEAT: int = 10
MUSH: int = 2 
PLAYER: str = ""
MUSHROOM: str = 'U0001F344'
    
def points(score: int) -> int: 
    points: int = 0 
    return score


def greet() -> None: 
    print("Greetings, welcome to the Enchanted Forest, a serene but spooky wonderland teeming with life- both pure and evil. Throughout your quest, your choces will determine which of these beings you will encounter and your fate at each step.")
    PLAYER = input("But first, please enter your name, brave explorer: ")
    POINTS += NAME 
    print("Currently, " + PLAYER + "you have" + str(POINTS) + "points for entering your name. Points are earned by successfully defeating wicked beasts and by claiming the magic mushrooms presented throughout your adventure. Entering your name is 2 points added, choosing a path is 5 points added, defeating your opponent is 10 points added, and accepting a mushroom prize is 2 points added. The maximum number of points, therefore, is 19. Choose one of the three paths below to begin your journey through the woods and earn points.")

def main() -> None: 
    greet()

x: str = input("type 'a' to enter the candid cave. type 'b' to enter the squalid swamp. type 'c' to enter the treacherous tunnel. type 'd' to end game. ")

if x == 'a': 
    print("you have now entered the candid cave. You reluctantly walk towards it and peer inside the cool interioir before stepping in. As you trek through, you hear your footsteps echoing and bats screeching. A strange chill floods over you, putting your hairs on end. A blood-curdling screech fills the cave. You step back, dazed. But it is too late. A billowing, shadowy figure emerges. You tremble in fear as Barefoot himself towers above you. What will you do?")
    POINTS += PATH 
    print("You have " + str(POINTS) + " points for entering the cave. ")
    print("You can turn around now and end the game, forgoing future points and a chance at completing your mission, guaranteeing death at the hands of the beast. Step up to challenge this monster, however, and you may survive and continue. What will it be?") 
    x: str = input("Type 'X' to run away or 'Y' to fight Bigfoot.")
    if x = 'X': 
        print("END OF GAME. Bigfoot caught you before you could escape. Your score was" + str(POINTS))
    elif x = 'Y':
        pathone: int = input("Excellent choice, courageous one. Select a number between 1 and 6 to recieve a weapon. ") 
            if pathone = 1:
                SWORD: str = '\U0002694'
                print(SWORD)
                use: str = input("You have recieved a sword to fight Bigfoot. Type 'go' to use")
                if use = "go":
                    print("A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")
            else: 
                if pathone = 2:
                    ARROW: str = '\U0001F3F9'
                    print(ARROW)
                    use: str = input("You have recieved an arrow to fight Bigfoot. Type 'go' to use")
                    if use = "go": 
                        print("A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")
                else: 
                    if pathone = 3:
                        BOMB: str = '\U0001F4A3'
                        print(BOMB)
                        use: str = input("You have recieved a bomb to fight Bigfoot. Type 'go' to use")
                        if use = "go":
                            print("A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")
                    else:
                        if pathone = 4:
                            DAGGER: str = '\U0001F5E1'
                            print(DAGGER)
                            use: str = input("You have recieved a dagger to fight Bigfoot. Type 'go' to use")
                            if use = "go":
                                print("A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")
                        else: 
                            if pathone = 5:
                                AXE: str = '\U0001FA93'
                                print(AXE)
                                use: str = input("You have recieved an axe to fight Bigfoot. Type 'go' to use")
                                if use = "go":
                                    print("A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")
                            else: 
                                if pathone = 6: 
                                    PISTOL: str = '\U0001F52B'
                                    print(PISTOL)
                                    use: str = input("You have recieved a pistol to fight Bigfoot. Type 'go' to use")
                                    if use = "go":
                                        print("A loud thud marks the end of Bigfoot. Hurray! You have slain the beast!")

    POINTS += DEFEAT
    print("You earned 10 points for defeating this evil lifeform. Your score is now " + str(POINTS)
    print str(MUSHROOM)
    choiceone: str = input("Would you like this mystical mushroom as a reward? Type 'yes' or 'no'. ")
    if choiceone = "yes":
        POINTS += MUSH
        print ("Wise choice. You now have" + str(POINTS) "points. Congratulations for defeating your opponnet. Your mission is complete. END OF GAME. ")
    else: 
        print("Very well. The game is now over. Your final score was (points)")
#_____________________________PATH B
    else: 
        if x = 'b': 
            print("you have now entered the squalid swamp. The slimy and frigid water tickles your toes as you stare into the murky liquid. Slowly, you wade into the algae- filled swamp. You grimace as you feel aquatic life move around your legs. You are hip- deep when you hear a loud roar. The muddy floor beneath your feet quivers and your eyes widden, giving you a full view of the enormous ogre that rises out of the water. What will you do? ") 
            POINTS += PATH
            print ("You have " + str(POINTS) + print " points for entering the swamp. ")
            print("You can turn around now and end the game, forgoing future points and a chance at completing your mission, guaranteeing death at the hands of the beast. Step up to challenge this monster, however, and you may survive and continue. What will it be?")
            x: str = input("Type 'x' to run away or 'y' to fight the ogre.")
            if x = 'X': 
                print("END OF GAME. The ogre caught you before you could escape. Your score was (points)")
            else: 
                if input = 'Y':
                    pathtwo: int= input("Excellent choice, courageous one. Select a number between 1 and 6 to recieve an element power. ") 
                    if pathtwo = 1:
                        WATER: str = '\U0001F30A'
                        print(WATER)
                        usee: str = input("You have recieved water powers to fight the ogre. Type 'go' to use")
                        if usee = "go":
                            print("A loud thud marks the end of the ogre. Hurray! You have slain the beast!")
                    else: 
                        if pathtwo = 2: 
                            AIR: str = '\U0001F32A'
                            print(AIR)
                            usee: str = input("You have recieved air powers to fight the ogre. Type 'go' to use")
                            if usee = "go":
                                print("A loud thud marks the end of the ogre. Hurray! You have slain the beast!")
                        else: 
                            if pathtwo = 3:
                                EARTH: str = '\U00026F0'
                                print(EARTH)
                                usee: str = input("You have recieved earth powers to fight the ogre. Type 'go' to use")
                                if usee = "go":
                                    print("A loud thud marks the end of the ogre. Hurray! You have slain the beast!")
                            else: 
                                if pathtwo = 4:
                                    FIRE: str = '\U0001F525'
                                    print(FIRE)
                                    usee: str = input("You have recieved fire powers to fight the ogre. Type 'go' to use")
                                    if usee = "go":
                                        print("A loud thud marks the end of the ogre. Hurray! You have slain the beast!")
                                else: 
                                    if pathtwo = 5:
                                        COMMET: str = '\U0002604'
                                        print(COMMET)
                                        usee: str = input("You have recieved a commet to fight the ogre. Type 'go' to use")
                                        if usee = "go":
                                            print("A loud thud marks the end of the ogre. Hurray! You have slain the beast!")
                                    else: 
                                        if pathtwo = 6: 
                                            LIGHTNING: str = '\U00026A1'
                                            print(LIGHTNING)
                                            usee: str = input("You have recieved lightning powers to fight the ogre. Type 'go' to use")
                                            if usee = "go":
                                                print("A loud thud marks the end of the ogre. Hurray! You have slain the beast!")

                POINTS += DEFEAT
                print("You earned 10 points for defeating this evil lifeform. Your score is now " + str(DEFEAT))
                print str (MUSHROOM)
                choicetwo: str = input("Would you like this mystical mushroom as a reward? Type 'yes' or 'no'. ")
                if choicetwo = "yes":
                    POINTS += MUSH
                    print("Wise choice. You now have" + str(POINTS) + "points. Congratulations for defeating your opponnet. Your mission is complete. END OF GAME. ")
                else: 
                    print("Very well. The game is now over. Your final score was (points)")
# _______________________________PATH C
    else: 
        if x = 'c': 
            print("you have now entered the treacherous tunnel. Thorns prickle your arms as twigs scratch your ankles. You crouch and gradually begin moving deeper into the tunnel, moving bushes and branches out of yor face. Suddenly, you hear a sinister laugh and turn to see a witch descend towards you on her broom. The blood drains from your face and your knuckles turn white. What will you do?")
            POINTS += PATH
            print ("You have " + str(POINTS) + " points for entering the tunnel. ")
            print("You can turn around now and end the game, forgoing future points and a chance at completing your mission, guaranteeing death at the hands of the beast. Step up to challenge this monster, however, and you may survive and continue. What will it be?")
            x: str = input("Type 'x' to run away or 'y' to fight the witch.")
            if x = 'X':      
                print("END OF GAME. The witch caught you before you could escape. Your score was (points)")
            else 
                if x = 'Y':
                    paththree: int = input("Excellent choice, courageous one. Select a number between 1 and 6 to recieve a magical power. ")   
                    if paththree = 1:
                        CRYSTALBALL: str = '\U0001F52E'
                        print(CRYSTALBALL)
                        useee: str = input("You have recieved a crystal ball to fight the witch. Type 'go' to use")
                        if useee = "go":
                            print("A loud thud marks the end of the witch. Hurray! You have slain the beast!")
                    else: 
                        if paththree = 2:
                            WAND: str = '\U0001FA84'
                            print(WAND)
                            useee: str = input("You have recieved a wand to fight the witch. Type 'go' to use")
                            if useee = "go":
                                print("A loud thud marks the end of the witch. Hurray! You have slain the beast!")
                        else: 
                            if paththree = 3:
                            GEM: str = '\U0001F48E'
                            print(GEM)
                            useee: str = input("You have recieved a gem to fight the witch. Type 'go' to use")
                                if useee = "go":
                                    print("A loud thud marks the end of the witch. Hurray! You have slain the beast!")
                            else:
                                if paththree = 4:
                                POTION: str = '\U0001F9EA'
                                print(POTION)
                                useee: str = input("You have recieved a potion to fight the witch. Type 'go' to use")
                                    if usee = "go":
                                        print("A loud thud marks the end of the witch. Hurray! You have slain the beast!")
                                else: 
                                    if paththree = 5:
                                        HYPNOSIS: str = '\U0001F300'
                                        print(HYPNOSIS)
                                        useee: str = input("You have recieved hypnosis powers to fight the witch. Type 'go' to use")
                                            if useee = "go":
                                                print("A loud thud marks the end of the witch. Hurray! You have slain the beast!")
                                    else: 
                                        if paththree = 6 
                                            SLEEP: str = '\U0001F4A4'
                                            print(SLEEP)
                                            useee: str = input ("You have recieved a sleep spell to fight the witch. Type 'go' to use")
                                                if useee = "go":
                                                    print("A loud thud marks the end of the witch. Hurray! You have slain the beast!")

                POINTS += DEFEAT
                print("You earned 10 points for defeating this evil lifeform. Your score is now ") + str(POINTS)
                choicethree: str = input("Would you like this mystical mushroom as a reward? Type 'yes' or 'no'. ")
                print str (MUSHROOM)
                if choicethree = "yes":
                    POINTS += MUSH
                    print ("Wise choice. You now have" + str(POINTS) "points. Congratulations for defeating your opponnet. Your mission is complete. END OF GAME. ")
                else: 
                    print ("Very well. The game is now over. Your final score was " + str(POINTS))
# __________________________PATH D  
 else: 
    if input = d:
    print ("You have left the enchanted forest. END OF GAME. Upon ending the game, your score was" + str(POINTS))

if __name__ == "__main__":
  main()
