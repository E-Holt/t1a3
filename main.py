# Import system module from os library for the clear command used below.
from os import system
# Import from the guess file for game play.
import guess
# import from the instruction file to show the instructions for option 1.
import instruction

# Menu function, this is displayed 
def welcome_options():
    print("Welcome to the super awesome web dev logo and icon colour guessing game! Please see the below menu for options: ")
    print("1. Show instructions")
    print("2. Right to the game")
    print("3. Exit")
    selection = input("Select what you'd like to do: ")
    return selection

# Menu function, this is the logic.
user_input = ""
while user_input != "3":
    system('clear')
    user_input = welcome_options()
    system('clear')
    if user_input == "1":
        instruction.show_instructions()
    elif user_input == "2":
        guess.guess_game()
    elif user_input == "3":
        print("Thanks for playing!") 
        exit()
    else:
        # Error handling
        print("That isn't an option! Please choose an option from the menu only.")
        
    input("press Enter to continue...")
    system('clear')
