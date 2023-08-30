
"""
Created on Sun Aug 20 00:12:28 2023

@author: vc
"""

''' Task 3 : Rock, paper, scissors game
    Create a program that allows the user to play
    the classic game of rock, paper, scissors
    against the computer. 
'''

import random
# Function for Playing the game       
def play_game():
    print("Computer Turn:")
    # I have genarated random numbers 1, 2 or 3
    ran_no = random.randint(1, 3)
    # computer turn is equal random numbers
    computer_turn = ran_no
    # if random number = 1, then computer turn = 'r' means Rock
    if ran_no == 1:
        computer_turn = 'r' # r for Rock
    # if random number = 2, then computer turn = 'p' means Paper
    elif ran_no == 2:
        computer_turn = 'p' # p for Paper
    # if random number = 3, then computer turn = 's' means Scissor
    elif ran_no == 3:
        computer_turn = 's'
    print("Enter one of these 'r' for Rock, 'p' for Paper, 's' for Scissor:") 
    # Now computer have choosed its option, Now its our choice to choose one option   
    your_turn = input("Your Turn:")
    # These the possibilities for anyone win , lose or tie
    # if computer_turn = rock and your_turn = paper, then you win, bacause paper finish or wrap the rock 
    if computer_turn == 'r' and your_turn == 'p':
        print("You win")
    # if computer_turn = rock and your_turn = scissors, then you lose, bacause rock finish the scissor 
    elif computer_turn == 'r' and your_turn == 's':
        print("you lose")
    # if computer_turn = rock and your_turn = rock, then there is a tie
    elif computer_turn == 'r' and your_turn == 'r':
        print("There is Tie")  
        
    # if computer_turn = paper and your_turn = scissors, then you win, because scissor cut the paper 
    if computer_turn == 'p' and your_turn == 's':
        print("You win")
    # if computer_turn = paper and your_turn = rock, then you lose, bacause paper finish or wrap the rock 
    elif computer_turn == 'p' and your_turn == 'r':
        print("you lose")
    # if computer_turn = paper and your_turn = paper, then there is a tie
    elif computer_turn == 'p' and your_turn == 'p':
        print("There is Tie")  
        
    
    # if computer_turn = scissor and your_turn = rock, then you win, bacause rock finish the scissor
    if computer_turn == 's' and your_turn == 'r':    
        print("You win")
    # if computer_turn = scissors and your_turn = paper, then you lose, bacause scissor cut the paper 
    elif computer_turn == 's' and your_turn == 'p':
        print("you lose")
    # if computer_turn = scissors and your_turn = scissors, then there is a tie, bacause both are same
    elif computer_turn == 's' and your_turn == 's':
        print("There is Tie")  
    reset_game()       

# Function for reset or start the game
def reset_game():
    print("if you want to play again write 'p' and for quit the game write 'q':")  
    decide = input("play again or quit:")
    # if decicide = p means play again then we call the play function to play game again
    if decide.lower() == 'p':
        play_game()
    # Otherwise print the message Thanks for playing and exit the game
    else:
        print("Thanks for playing")
# Here we calling play function to play the game for first time when we run the program        
play_game()
       
        
            
            


