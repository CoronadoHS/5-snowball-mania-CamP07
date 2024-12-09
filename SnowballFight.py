''' 
    Name: Snowball-Mania
    Author: Cameron Powell
    Date: 12/3/2024
    Class: AP Computer Science Principles
    Python: 3.11.5
'''

import random
import time
from colorama import Fore


def main():
    # the main runner of the game
	  # welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    print("What is your name?")
    name = input()
    print(f'Great to have you here, {name}! Who do you want to play against?')
    opponent = input()

    players = []
    players.append(name)
    players.append(opponent)

    playersOut = []

    print("Are there any more opponents? If so, type them one at a time (or NONE) and press 'Enter'")
    nextPlayer = input()
    players.append(nextPlayer)
    
    while (nextPlayer != "NONE"):
        print("Are there any more opponents? If so, type them one at a time (or NONE) and press 'Enter'")
        nextPlayer = input()
        players.append(nextPlayer)
    players.remove("NONE")

    print(*players, sep=" vs. ")
        
    
    print("Do you want to choose who you throw the snowball at, or do you want it to be random? (Type YES or NO)")
    choice = input()

    gameplay(name, players, choice, playersOut)

    # randomly choose one person to throw a snowball at the other

   

def gameplay(name, players, manual, out):
      # randomly choose one person to throw a snowball at the other
      while (len(players) > 1):
        thrower = random.choice(players)
        if (thrower == name):
            if (manual == "YES"):  # manual mode
                print("It's your turn! Who do you want to throw a snowball at?")
                target = input()
            else:
                target = random.choice(players)   # randomly selects targets
                while target == thrower:
                    target = random.choice(players)      
        else:
                target = random.choice(players)   # randomly selects targets
                while target == thrower:
                    target = random.choice(players)
       
        if target in players:

            print(f'{thrower} threw a snowball at {target}!')
            
            # generate a random number to use as the hitNum
            hitNum = random.randint(1, 10)
            success = hitResult(hitNum)
            if success == True:
                print("It's a " + Fore.GREEN + "hit! " + Fore.RESET + target + " is down!\n")
                players.remove(target)
                out.append(target)
            else:
                print(f'{thrower} is trash at the game and {Fore.RED}missed!\n{Fore.RESET}')
        elif target in out:
            print(f'{thrower} threw a snowball at {target}, who was already out. That is {Fore.RED}not cool.{Fore.RESET}')
        else:
            print(f'{thrower} threw a snowball at a random passerby named {target}! They are {Fore.RED}not pleased.\n{Fore.RESET}')

        time.sleep(2)
    
      print(Fore.YELLOW + players[0] + Fore.RESET + " has won the snowball fight!")


def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if hitNum <= 3:
        return True
    else: 
        return False


main()
