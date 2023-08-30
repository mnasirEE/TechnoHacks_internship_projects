# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:42:43 2023

@author: M.Nasir

"""

''' Task 4 : Tic Tac Toe Game
    Create a simple Tic Tac Toe game that can be
    played between two players or against the
    computer. 
'''
# importing random module used for generating random numbers     
import random  

# this function prints board of Tic Tok Toe game    
def tic_tok_toe_board(player_X,player_O,list_of_9_board_parts):
    
    # using a small variable for player X because it has been used too many times below
    p = player_X 
    # using a small variable for player O because it has been used too many times below
    t = player_O 
    # using a small variable for list of 9 board parts numbers because it has been used too many times below
    l = list_of_9_board_parts
    
    # These are all the conditions for tic toe game when two players choose there specific part of 9 parts of tic tok toe game board
    # if player x choose 1 then 1st part of game board replaced by 'X'
    if p == 1:
        l[0] = "X"
    # if player O choose 1 then 1st part of game board replaced by 'O'     
    elif t == 1:
        l[0] = 'O'
     
    # if player x choose 2 then 2nd part of game board replaced by 'X'
    if p == 2:
        l[1] = "X"
    # if player O choose 2 then 2nd part of game board replaced by 'O'      
    elif t == 2:
        l[1] = 'O' 
      
    # if player x choose 3 then 3rd part of game board replaced by 'X'
    if p == 3:
        l[2] = "X"
    # if player O choose 3 then 3rd part of game board replaced by 'O' 
    elif t == 3:
        l[2] = 'O'
     
    # if player x choose 4 then 4th part of game board replaced by 'X'
    if p == 4:
        l[3] = "X"
    # if player O choose 4 then 4th part of game board replaced by 'O' 
    elif t == 4:
        l[3] = 'O'    
      
    # if player x choose 5 then 5th part of game board replaced by 'X'
    if p == 5:
        l[4] = "X"
    # if player O choose 5 then 5th part of game board replaced by 'O'
    elif t == 5:
        l[4] = 'O'   
        
    # if player x choose 6 then 6th part of game board replaced by 'X'
    if p == 6:
        l[5] = "X"
    # if player O choose 6 then 6th part of game board replaced by 'O'
    elif t == 6:
        l[5] = 'O'
           
    # if player x choose 7 then 7th part of game board replaced by 'X'
    if p == 7:
        l[6] = "X"
    # if player O choose 7 then 7th part of game board replaced by 'O'
    elif t == 7:
        l[6] = 'O'
          
    # if player x choose 8 then 8th part of game board replaced by 'X'
    if p == 8:
        l[7] = "X"
    # if player O choose 8 then 8th part of game board replaced by 'O'
    elif t == 8:
        l[7] = 'O'
       
    # if player x choose 9 then 9th part of game board replaced by 'X'
    if p == 9:
        l[8] = "X"
    # if player O choose 9 then 9th part of game board replaced by 'O'
    elif t == 9:
        l[8] = 'O'
    
    # And finally these are the print statements to print our Tic Tok Toe Game Board
    # Using f strings, we have used variables in these print statements so that our game board change according to our need    
    
    print("=/=\=/=\=/=\=/=")
    print(f"  {l[0]} || {l[1]} || {l[2]}  ")
    print("====||===||====")
    print(f"  {l[3]} || {l[4]} || {l[5]}  ")
    print("====||===||====")
    print(f"  {l[6]} || {l[7]} || {l[8]}  ")
    print("=/=\=/=\=/=\=/=")
    
       
def check_win(list_of_9_board_parts, attempts_of_X, attempts_of_O):
    l = list_of_9_board_parts
    x = attempts_of_X
    o = attempts_of_O
   
    global condition_of_loop
    wins = [[l[0],l[1],l[2]],[l[3],l[4],l[5]],[l[6],l[7],l[8]],[l[0],l[3],l[6]],[l[1],l[4],l[7]],[l[2],l[5],l[8]],[l[0],l[4],l[8]],[l[2],l[4],l[6]]]

    for i in wins:
         
        if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
            print("X wins")
            print(" ")
            condition_of_loop = False
            break
            
        elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
            print("O wins")
            condition_of_loop = False
            break
        
    if (x == 4 and o == 5) or (x == 5 and o == 4):
        print("Match Draw")
        condition_of_loop = False

def Play_Game(): 
    # My Tic Tok Toe game board is divided into 9 parts
    # So I am initializing 9 variables with 1-9 values  
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9 
    # Then I am putting above variables in a list
    list_of_9_board_parts = [one,two,three,four,five,six,seven,eight,nine]
    # I am initializing player x value to zero so that I can use them as a global variable in my functions before taking any input from user
    player_X= 0
    # I am initializing player o value to zero so that I can use them as a global variable in my functions before taking any input from user
    player_O = 0
    # These are the number of chances when the starts for player x
    # As there are 9 boxes or parts of Game Board, if player x has a first chance, then it will has total 5 chances to win, lose or draw the game and player O will has total 4 chances.
    attempts_of_X = 0
    # These are the number of chances when the starts for player o
      # As there are 9 boxes or parts of Game Board, if player o has a first chance, then it has total 5 chances to win, lose or draw the game and player O will has total 4 chances.
    attempts_of_O = 0
    # I want that there will be random first chance of each player. Because I don't like that two player quarrel with each and it is not a sportsmanship
    # I am picking random value for first chance of each player 
    turn = random.randint(0, 1)
    # I am saying welcome to my players for playing "Tic Tok Toe Game" 
    print(" ")
    print("***** Welcome to 'Tic Tok Toe' Game *****\n")
    print(" ")
    print("##### Let's Play the Game #####")
    print(" ")
    # I am calling my Game Board to print board so that players see it and play game
    tic_tok_toe_board(player_X,player_O,list_of_9_board_parts)
    print("")
    # I am giving options to player_x
    print("Players Note: You can choose only one number from the list [1, 2, 3, 4, 5, 6, 7, 8, 9]")
    print("")
    # Here I am making a global variable of "condition of loop" because I want to use it in different functions
    # By global keyword, I make it a global variable so that I can use it in any functions and makes changes to it according to my choice and in any function      
    global condition_of_loop
    # I am starting while loop so that players play game continuosly
    while(condition_of_loop):

        # if turn = 1, then player x has first chance 
        if turn == 1:
            # Here I am saying to users that player x has a chance to turn
            print("@@@@@ 'X's Chance @@@@@\n")
            print(" ")
            # I am taking input decision of player x
            player_X = int(input("Player_X Turn:"))
            print(" ")
            # After taking player x turn, I am recording its chances
            attempts_of_X = attempts_of_X + 1
            # I am printing game board according to player x choice
            tic_tok_toe_board(player_X,player_O,list_of_9_board_parts)
            print(" ")
            # And I calling check_win function, whether anyone win or not
            check_win(list_of_9_board_parts,attempts_of_X,attempts_of_O)
            
            # if  condition_of_loop = false exit from the loop game over
            if condition_of_loop == False:
                break
            # I am taking input decision of player o
            player_O = int(input("player_O turn:"))
            print(" ")
            # After taking player o turn, I am recording its chances
            attempts_of_O = attempts_of_O + 1
            # I am printing game board according to player x choice
            tic_tok_toe_board(player_X,player_O,list_of_9_board_parts)
            print(" ")
        
        # if turn = 0, then player o has first chance     
        else:

           # Here I am saying to users that player x has a chance to turn 
           print("@@@@@ 'O's Chance @@@@@\n") 
           print(" ")
           # I am taking input decision of player o
           player_O = int(input("player_O turn:"))
           print(" ")
           # After taking player o turn, I am recording its chances
           attempts_of_O = attempts_of_O + 1
           # I am printing game board according to player x choice
           tic_tok_toe_board(player_X,player_O,list_of_9_board_parts)
           print(" ")
           # And I calling check_win function, whether anyone win or not
           check_win(list_of_9_board_parts,attempts_of_X,attempts_of_O)
           
            # if  condition_of_loop = false exit from the loop game over
           if condition_of_loop == False:
               break
           # I am taking input decision of player x
           player_X = int(input("player_X Turn:"))
           print(" ")
           # After taking player o turn, I am recording its chances
           attempts_of_X = attempts_of_X + 1
           # I am printing game board according to player x choice
           tic_tok_toe_board(player_X,player_O,list_of_9_board_parts)
           print(" ")
    # When game ended, I am calling restart function, lets explore it
    Restart_Game()
# Fuction of Restart Game or Reset game    
def Restart_Game():
    # Here I am making a global variable and why I am using I have already explained
    global condition_of_loop
    # if condition of loop is false then we reset game only 
    if condition_of_loop == False:
        # I am guiding my players what to do next, want to play or exit
        print(" @@@@@ Want to Play again write 'p' for play again @@@@@ \n ")
        print(" @@@@@ Want to exit write 'e' for exit @@@@@ \n")
        # Here I am recording my player decision
        restart = input("Enter 'p' to continue or enter 'e' to exit:  ")
        print(" ")
        # if player decision = 'p', restart the game
        if restart.lower() == 'p':
            condition_of_loop = True
            Play_Game()
        # else exit from the game     
        elif restart.lower() == 'e':
            print("**** Thanks for playing ****")
      
           
# Here I am initialing my while loop condition and its global variable because have used it in various functions 
condition_of_loop = True
# It is my function that actually start the game , my main function
Play_Game()




       
    
    
    
    
        
    