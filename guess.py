import random
import colourlist 
import score
keep_adding_points = 0

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

def game_input(hints, colour_pick):
    guess_input_counter = 0
    i=0
    print("Try and guess the colour described in the following hint!")
    print (hints[i])
    guess_input = input("What is the colour? (red, organge, yellow, green, blue, purple, black, grey): ")
    while guess_input != colour_pick and i<4:
        guess_input_counter += 1
        i += 1
        print("Thats incorrect! Please try again!")
        print(hints[i])
        guess_input = input("What is the colour? (red, organge, yellow, green, blue, purple, black, grey): ")
    while guess_input != colour_pick and i == 4:
        print("Sorry, you're out of guesses!")
        play_again_fun()
    if guess_input == colour_pick:
        total_points = 5-int(guess_input_counter)
        print("You guessed the colour! Great job!")
        print ("You got", total_points,"/5 points!")
        score.point_counter(total_points)
        play_again_fun()
    else:
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
