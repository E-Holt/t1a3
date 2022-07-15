# Import for the random choice and random shuffle modules used
import random
# Import for the hints that get shuffled and used
import colourlist 
# Import for the score keeping feature
import score
# The one global variable I couldn't get to work inside the function
keep_adding_points = 0

# This function chooses one of the colours listed randomly, then takes the list of hints associated with the colour and shuffles it.
# The shuffled hints list and chosen colour are then used in the next function, which is called at the end of this one. Part of the hints feature.
def guess_game():
    colours = ["red", "yellow", "green", "blue", "purple", "black", "grey"]
    colour_pick = (random.choice(colours))
    if colour_pick == "red":
        hints = colourlist.red_list
    if colour_pick == "orange":
        hints = colourlist.orange_list
    if colour_pick == "yellow":
        hints = colourlist.yellow_list
    if colour_pick == "green":
        hints = colourlist.green_list
    if colour_pick == "blue":
        hints = colourlist.blue_list
    if colour_pick == "purple":
        hints = colourlist.purple_list
    if colour_pick == "black":
        hints = colourlist.black_list
    if colour_pick == "grey":
        hints = colourlist.grey_list
    random.shuffle(hints)
    game_input(hints, colour_pick)

# This function is for the majority of the user input logic and contains the rest of the hints feature and part of the score keeping feature.
def game_input(hints, colour_pick):
    # Used for score keeping feature
    guess_input_counter = 0
    # Used for hints feature to continue loop with new hint.
    i=0
    print("Try and guess the colour described in the following hint!")
    # Part of hints feature.
    print (hints[i])
    guess_input = input("What is the colour? (red, organge, yellow, green, blue, purple, black, grey): ")
    while guess_input != colour_pick and i<4:
        # This decreases the potential score per wrong guess in a round with the total_points variable later.
        guess_input_counter += 1
        # This is used to move on to the next hint in the list per wrong guess.
        i += 1
        print("Thats incorrect! Please try again!")
        # Next hint per wrong guess
        print(hints[i])
        guess_input = input("What is the colour? (red, organge, yellow, green, blue, purple, black, grey): ")
    while guess_input != colour_pick and i == 4:
        # As i starts at zero, this means only 5 guesses allowed
        print("Sorry, you're out of guesses!")
        play_again_fun()
    if guess_input == colour_pick:
        # This gives the correct points in a round
        total_points = 5-int(guess_input_counter)
        print("You guessed the colour! Great job!")
        print ("You got", total_points,"/5 points!")
        # This gives the correct points per game, all rounds inclusive
        score.point_counter(total_points)
        play_again_fun()
    else:
        # Error handling
        print("Sorry, that isn't an option!")

def play_again_fun():
    play_again = input("Would you like to play again? (yes/no) ")
    while play_again == "yes":
        guess_game()
    if play_again == "no":
        print("Thanks for playing!")
        exit()
    else: 
        print("Sorry that's not an option!")
        play_again_fun()