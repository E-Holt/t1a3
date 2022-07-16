# T1A3 Terminal App Assignment

## Functionality
    - The purpose of this app is entertainment and to test how well users know commonly used logos and icons for programming languages and frameworks. 

## Installation
    - In order to run this app you will need to install Python3, installation instructions can be found here: https://www.python.org/downloads/
    - You then open your terminal on your computer and type in the following:
    ```./src/executegg.sh help``` for how to install and play this game.
    ```./src/executegg.sh``` to go to the main menu and play the game!

## How to play
    - You can view the logos and icons used in this game in the README file in the folder containing the game.
    - This game is played by following the prompts. 
    - In the menu, please type in the relevant number and press the enter key. 
    - If you've chosen to view the instructions you can then press enter again to return to the menu. 
    - If you've chosen to play the game, the game will give you a hint then prompt you for a colour name. 
    - Please type in the colour name in lower cased letters, then press enter. 
    - If you type in the incorrect colour or any other word that is not the colour, it will count as an incorrect guess and you'll be given a new hint for the same colour.
    - Remember you only have five guesses! 
    - If you don't guess correctly within those five guesses, you'll be asked if you want to play again. 
    - Please type in “yes” or “no” and press enter. 
    - If you guessed correctly, you'll be given a score based on how many guesses it took and will be asked if you'd like to play again. 
    - If you guess correctly in multiple rounds, you'll be shown your total score for all the rounds you've played if you haven’t exited the game. 
    - When you're done playing, you can choose "no" to playing again, or exit the terminal at any point. 
    - Thanks for playing the game!

## My repository can be found at:
    [Repository](https://github.com/E-Holt/t1a3)

## Styling Conventions
    - I used the Python variable naming convention snake case for naming variables and functions (Python Variable Names, 2022).

## Features
### 1. Menu feature
    - The menu feature is a basic menu that allows the user to choose what they'd like to do. It has some error handling capabilities for inputs that aren't a menu option and uses imported data to connect with other files used in the program, as well as an imported module to allow the screen to be cleared. It also uses a while loop and conditional statements to allow the user to choose options efficiently and with minimal risk of breaking if something goes wrong. 
    ![Menu example image](./docs/menu_function.png)

### 2. Hints feature
    - The hints freature is spread across a couple files and a couple functions to allow the program to choose a random colour and shuffle the related hints list in order to give hints that wont be in the same order on any given round. This involves using a list relevant to each colour, multiple if statments in order to correctly choose the list, an imported random module to randomise the colour choice and shuffle the hints list, as well as a while loop for giving the hints dependant on if the input was correct or not. The hints feature is mostly not interacted with by the user, but does have some error handling capabilities with the rest of the game_input function when the user inputs something that isn't usable.
    ![Hints example image](./docs/game_proper.png)
    ![Hints list example image](./docs/hints_list_example.png)

### 3. Scoring keeping feature
    - The scoring feature if found in the  game_input function and the point_counter function. It uses a variable that starts at zero and calculated the points in a round based on how many guesses were input before a correct guess, if a correct guess is given. Additionally, the point_counter function tracks those points and adds them together each round to give a total game score which is reset when the program is exited. The scoring feature is involved in a while loop along with the hints function mentioned above as well as conditional statements dependant on whether the input was a correct guess or not. The scoring feature itself doesn't have error handling function, but utilises the error handling in the game_input function when an incorrect guess is given. 
    ![Scoring function example](./docs/score_function.png)

## Implementation Plan
    - I used Trello to keep track and what I was working on and what needed to be done by a certain date.
### Menu feature
- List menu options
- Link menu options with relevant functions
- Figure out how to quit program
- Create error response 
- Test menu function
### Hints feature
- List hints in an accessible manner
- Create function for randomly choosing colour
- Create function for randomly choosing hints
- Get functions working together
- Test performance of hints system
### Score Keeping feature
- Create relevant scoring system
- Create function for keeping score across games
- Connect score functions with main game functions
- Create error handling
- Test score keeping function

## Design
    - Accurately describe how to use and install the application.
- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application

## Reference List:

W3schools.com. 2022. Python Variable Names. [online] Available at: <https://www.w3schools.com/python/gloss_python_variable_names.asp> [Accessed 15 July 2022].