#Hello function
#Print welcome
#menu - instructions, right to game, exit
#function game itself
#function score tracking

from fileinput import close
from os import system
import guess

def welcome_options():
    print("Welcome to the super awesome web dev logo and icon colour guessing game! Please see the below menu for options: ")
    print("1. Show instructions")
    print("2. Right to the game")
    print("3. Exit")
    opt = input("Select what you'd like to do: ")
    return opt

option=""
while option != "3":
    system('clear')
    option = welcome_options()
    system('clear')
    if option == "1":
        show_instructions()
        pass
    elif option == "2":
        guess.guess_game()
    elif option == "3":
        print("Thanks for playing!") 
        exit()
    else:
        print("Invalid option")
        
    input("press Enter to continue...")
    system('clear')

print("Thanks for playing!") 