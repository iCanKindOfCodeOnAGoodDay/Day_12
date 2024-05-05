"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 12
    May 04 2024

    ------
    Description:    Console Input/ Output Guessing Game - Difficulty Easy Medium or Hard *Restarts after win / lose
    ------
    
    ------
    Inputs:         Guess numbers between 1-100 in console ** error inputs are hanlded, user is prompted to type acceptable inputs if they make a typo .... so the program will not crash no matter what the input is
    ------
    
    ------
    Outputs:        Hints outputed to console: Guess too high, too low, game over, or winner
    ------
    
    ------
    Dependencies:   Random
    ------

    ------
    Assumptions:    Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

import random

console_art = """

ooooo      ooo                                .o8                          
`888b.     `8'                               "888                          
 8 `88b.    8  oooo  oooo  ooo. .oo.  .oo.    888oooo.   .ooooo.  oooo d8b 
 8   `88b.  8  `888  `888  `888P"Y88bP"Y88b   d88' `88b d88' `88b `888""8P 
 8     `88b.8   888   888   888   888   888   888   888 888ooo888  888     
 8       `888   888   888   888   888   888   888   888 888    .o  888     
o8o        `8   `V88V"V8P' o888o o888o o888o  `Y8bod8P' `Y8bod8P' d888b    
                                                                           
                                                                           
                                                                           
  .oooooo.                                                                 
 d8P'  `Y8b                                                                
888           oooo  oooo   .ooooo.   .oooo.o  .oooo.o  .ooooo.  oooo d8b   
888           `888  `888  d88' `88b d88(  "8 d88(  "8 d88' `88b `888""8P   
888     ooooo  888   888  888ooo888 `"Y88b.  `"Y88b.  888ooo888  888       
`88.    .88'   888   888  888    .o o.  )88b o.  )88b 888    .o  888       
 `Y8bood8P'    `V88V"V8P' `Y8bod8P' 8""888P' 8""888P' `Y8bod8P' d888b      
                                                                           
                                                                           
                                                                           

"""

def main():
    
    """
    
    Description -   Runs our number guessing game, recursive call to main to restart game
    ----------
    Input -         Console Game
    ----------
    Output -        Console game
    -------

    """
    
    print( console_art )
    
    difficulty, life_count = choose_difficulty()
    correct_number = pick_random_number() 
    player_win = False
    
    game_play( life_count, correct_number )

    main() # recursive call to main to start the game over, due to input functions this is okay.
        

def choose_difficulty():
    
    """
    
    Description -   Determines how many guesses the player will get before a game over
    ----------
    Input -         type easy, medium, hard - or get prompted type again if there is some other input
    ----------
    Output -        returns difficulty string and life count, prints text to console with life count
    -------

    """
    
    while True:
        difficulty = input( 'Choose Difficulty, Type: easy, medium, hard: ' )
        
        if difficulty == 'easy':
            print( 'You have 10 lifes! Guess the number: ' )
            life_count = 10
            return difficulty, life_count
        
        elif difficulty == 'medium':
            print( 'You have 7 lifes! Guess the number: ' )
            life_count = 7
            return difficulty, life_count
        
        elif difficulty == 'hard':
            print( 'You have 5 lifes! Guess the number: ' )
            life_count = 5
            return difficulty, life_count
        
        print( 'invalid entry' ) # restart loop if the input is not as expected
    
    
def pick_random_number():
    
    """
    
    Description -   Picks a random number between 1 and 100
    ----------
    Input -         None.
    ----------
    Output -        The random number
    -------

    """
    
    random_number = random.randint( 1, 100 ) # import random package
    
    return random_number


def guess_check( the_correct_number ): 
    
    """
    
    Description -   Prompts the user to guess a number, compares the guess to the actual number 
    ----------
    Input -         Pass in the correct number.... and get user input ( the guess ), modified input function that only accepts integers, any othe input is a handled exception and user is prompted to guess again
    ----------
    Output -        outputs hints to console, or tells user they won if they guessed the correct number
    -------

    """
    
    stop_asking = False # if user does not input int, don't except the input instead ask again
    while stop_asking == False:
        try:
            user_guess = int( input( 'guess the number' ) )
            if type( user_guess ) == int:
                stop_asking = True
        except:
            print( 'please type an integer.' )
    
    if user_guess == the_correct_number:
        print( f'winner, you guessed the correct number {the_correct_number}' )
        
    elif user_guess > the_correct_number:
        print( 'too high' )
        
    else:
        print( 'too low' )
    
    return user_guess


def game_play( life_count, correct_number ):
        
    """
    
    Description -   Asks for a guess until the user wins or runs out of guesses (loses)
    ----------
    Input -         life count based on difficulty selected, and the answer
    ----------
    Output -        After guess loop, outputs text in console to notify player if they won or lost
    -------

    """
    
    player_win = False
    
    while life_count > 0: 

        guess = guess_check( correct_number )       
        if guess == correct_number:
            player_win = True
            
            break # stop guessing and restart game below with the recursive call to main ( in main )
        life_count -= 1
        print( f'you have {life_count} lives left' )
        
    # No more guesses, game is over either way 
    if player_win == False:      
        print( f'Game Over! The correct number was {correct_number}' ) 
    else:
        print( 'Player win!' )
    
    
# run
if __name__ == '__main__':
    main()
