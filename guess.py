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
import random
from colourlist import red_list, orange_list, yellow_list, green_list, blue_list, purple_list, black_list, grey_list

colours = ["red", "yellow", "green", "blue", "purple", "black", "grey"]
colour_pick = (random.choice(colours))

def hints_choice():
    if colour_pick == "red":
        hints = red_list
    if colour_pick == "orange":
        hints = orange_list
    if colour_pick == "yellow":
        hints = yellow_list
    if colour_pick == "green":
        hints = green_list
    if colour_pick == "blue":
        hints = blue_list
    if colour_pick == "purple":
        hints = purple_list
    if colour_pick == "black":
        hints = black_list
    if colour_pick == "grey":
        hints = grey_list
    print(hints)


def giving_hints():
    colour_hints = (random.choice(black_list))
    print (colour_hints)







#take colour_pick, choose hints
#choose random hint from dicts
#give hint for colour_pic
#prompt guess
#if guess correct, points
#if guess incorrect -  
#Give next random hint, not giving ones given
#continue until 5 guesses
#if guess not in list - error
