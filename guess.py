#hints stored somehow?
#guess 1-5

#ranomly choose colour, store variable in chosen_color
#provide randomly chosen hint
#ask player guess, store as guess_input
#error for guess input not in colours
#If correct, print, add points
#if incorrect, print, give another hint
#until 5 guesses total
#after 5 guesses print "Sorry, you're out of guesses!"
#give total score
#print ("Would you like to play again? (yes/no): ")
#yes, continue game adding additional points. 
#no, print("Thank you for playing!"), back to menu
from ast import Return
from os import system
import random
import colourlist 
import main
#import score 
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
        play_again = input("Would you like to play again? (yes/no) ")
        if play_again == "yes":
            guess_game()
        if play_again == "no":
            print("Thanks for playing!")
            exit()
    total_points = 5-int(guess_input_counter)
    if guess_input == colour_pick:
        print("You guessed the colour! Great job!")
        print ("You got", total_points,"/5 points!")
        point_counter(total_points)
        play_again = input("Would you like to play again? (yes/no) ")
        if play_again == "yes":
            guess_game()
        if play_again == "no":
            print("Thanks for playing!")
            exit()

def point_counter(total_points):
    global keep_adding_points
    keep_adding_points = keep_adding_points + total_points
    print("Your total points are", keep_adding_points,"!")








#take colour_pick, choose hints
#choose random hint from dicts
#give hint for colour_pic
#prompt guess
#if guess correct, points
#if guess incorrect -  
#Give next random hint, not giving ones given
#continue until 5 guesses
#if guess not in list - error
