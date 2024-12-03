''' 
    Name: Snowball-Mania
    Author: Cameron Powell
    Date: 12/3/2024
    Class: AP Computer Science Principles
    Python: 3.11.5
'''

import random


def main():
    # the main runner of the game
	  # welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    print("What is your name?")
    name = input()
    print(f'Great to have you here, {name}! Who do you want to play against?')
    opponent = input ()
    print(name + " vs. " + opponent)

    print("Are there any more opponents? If so, type them one at a time (or NONE) and press 'Enter'")
    nextPlayer = input()

    players = []
    players.append(name)
    players.append(opponent)
    
    while (nextPlayer != "NONE"):
        print("Are there any more opponents? If so, type them one at a time (or NONE) and press 'Enter'")
        nextPlayer = input()
        players.append(nextPlayer)
    players.remove("NONE")


    # randomly choose one person to throw a snowball at the other

    while (len(players) > 1):
        thrower = random.choice(players)
        target = random.choice(players)
        while target == thrower:
            target = random.choice(players)
        print (f'{thrower} threw a snowball at {target}!')
        
        # generate a random number to use as the hitNum
        hitNum = random.randint(1, 10)
        success = hitResult(hitNum)
        if success == True:
            print("It's a hit! " + target + " is down!")
            players.remove(target)
        else:
            print(f'{thrower} is trash at the game and missed!')




def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if hitNum <= 3:
        return True
    else: 
        return False


main()
