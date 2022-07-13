#track score across multiple games/guesses
#give total score at end of each roung
import guess
import main
from os import system

def _try_counter():
    while guess_input_counter <5 and guess.guess_input != guess.colour_pick:
        print("That's incorrect, please try again!")
    
    if guess_input_counter == 5:
        print("Sorry, you're out of guesses!")
        play_again = input("Would you like to play again? (yes/no)")
        if play_again =="yes":
            main.welcome_options()
        if play_again =="no":
            print("Thanks for playing!")
            system('clear')

    def point_counter():
        point_count = 5 - guess_input_counter
        point_count = total_score
        while play_again == "yes":
            total_score += point_count
        print (total_score)
        return total_score
