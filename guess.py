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

colours = ["red", "yellow", "green", "blue", "purple", "black", "grey"]
colour_pick = (random.choice(colours))

#take colour_pick, choose hints
#give hint for colour_pic
#prompt guess
#if guess correct, points
#if guess incorrect -  hint/prompt
#if guess not in list - error

def hints():
    pass
