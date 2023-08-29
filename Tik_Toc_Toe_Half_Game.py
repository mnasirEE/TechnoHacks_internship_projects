# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:30:51 2023

@author: vc
"""


''' Task 4 : Tic Tac Toe Game
    Create a simple Tic Tac Toe game that can be
    played between two players or against the
    computer. '''
    
import random  
  
def tic_tok_toe_board(player_X,player_O,list_of_9_board_parts):
    
    p = player_X
    t = player_O 
    l = list_of_9_board_parts
    
    if p == 1:
        l[0] = "X"
    elif t == 1:
        l[0] = 'O'
     
    if p == 2:
        l[1] = "X"
    elif t == 2:
        l[1] = 'O' 
      
    if p == 3:
        l[2] = "X"
    elif t == 3:
        l[2] = 'O'
     
    if p == 4:
        l[3] = "X"
    elif t == 4:
        l[3] = 'O'    
      
    if p == 5:
        l[4] = "X"
    elif t == 5:
        l[4] = 'O'   
        
    if p == 6:
        l[5] = "X"
    elif t == 6:
        l[5] = 'O'
           
    if p == 7:
        l[6] = "X"
    elif t == 7:
        l[6] = 'O'
          
    if p == 8:
        l[7] = "X"
    elif t == 8:
        l[7] = 'O'
       
    if p == 9:
        l[8] = "X"
    elif t == 9:
        l[8] = 'O'
      
    print(f" {l[0]} | {l[1]} | {l[2]}")
    print(f" {l[3]} | {l[4]} | {l[5]}")
    print(f" {l[6]} | {l[7]} | {l[8]}")    
       
def check_win(list_of_9_board_parts, attempts_of_X, attempts_of_O):
    l = list_of_9_board_parts
    x = attempts_of_X
    o = attempts_of_O
   
    global condition_of_loop
    wins = [[l[0],l[1],l[2]],[l[3],l[4],l[5]],[l[6],l[7],l[8]],[l[0],l[3],l[6]],[l[1],l[4],l[7]],[l[2],l[5],l[8]],[l[0],l[4],l[8]],[l[2],l[4],l[6]]]

    for i in wins:
         
        if i[0] == 'X' and i[1] == 'X' and i[2] == 'X':
            print("X wins")
            condition_of_loop = False
            break
            
        elif i[0] == 'O' and i[1] == 'O' and i[2] == 'O':
            print("O wins")
            condition_of_loop = False
            break
        
    if (x == 4 and o == 5) or (x == 5 and o == 4):
        print("Match Draw")
        condition_of_loop = False
            

condition_of_loop = True
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9 

list_of_9_board_parts = [one,two,three,four,five,six,seven,eight,nine]
player_X= 0
player_O = 0
attempts_of_X = 0
attempts_of_O = 0
turn = random.randint(0, 1)

print("***** Welcome to 'Tic Tok Toe' Game *****\n")
tic_tok_toe_board(player_X,player_O,list_of_9_board_parts)
print("")

while(condition_of_loop):

 
    if turn == 1:
        
        print("@@@@@ 'X's Chance @@@@@\n")
        print(" ")
        player_X = int(input("Player_X Turn:"))
        attempts_of_X = attempts_of_X + 1
        tic_tok_toe_board(player_X,player_O,list_of_9_board_parts)
        print(" ")
        check_win(list_of_9_board_parts,attempts_of_X,attempts_of_O)
        
        
        if condition_of_loop == False:
            break
        player_O = int(input("player_O turn:"))
        print(" ")
        attempts_of_O = attempts_of_O + 1
        tic_tok_toe_board(player_X,player_O,list_of_9_board_parts)
        print(" ")
    
        
    else:
        
       print("@@@@@ 'O's Chance @@@@@\n") 
       print(" ")
       player_O = int(input("player_O turn:"))
       attempts_of_O = attempts_of_O + 1
       tic_tok_toe_board(player_X,player_O,list_of_9_board_parts)
       print(" ")
       check_win(list_of_9_board_parts,attempts_of_X,attempts_of_O)
       
       
       if condition_of_loop == False:
           break
       player_X = int(input("player_X Turn:"))
       attempts_of_X = attempts_of_X + 1
       tic_tok_toe_board(player_X,player_O,list_of_9_board_parts)
       print(" ")
       
    
    
    
    
        
    