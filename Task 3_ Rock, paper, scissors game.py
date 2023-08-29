# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:12:28 2023

@author: vc
"""

''' Task 3 : Rock, paper, scissors game
    Create a program that allows the user to play
    the classic game of rock, paper, scissors
    against the computer. '''
import random
    
class rock_paper_scissors_Game:
    #def __init__(self):
     #   self.ran_no = ran_no
        
    def play_game(self):
        print("Computer Turn:")
        ran_no = random.randint(1, 3)
        computer_turn = ran_no
        if ran_no == 1:
            computer_turn = 'r'
        elif ran_no == 2:
            computer_turn = 'p'
        elif ran_no == 3:
            computer_turn = 's'
        print("Enter one of these 'r' for Rock, 'p' for Paper, 's' for Scissor:")    
        your_turn = input("Your Turn:")
        if computer_turn == 'r' and your_turn == 'p':
            print("You win")
        elif computer_turn == 'r' and your_turn == 's':
            print("you lose")
        elif computer_turn == 'r' and your_turn == 'r':
            print("There is Tie")  
        
        if computer_turn == 'p' and your_turn == 's':
            print("You win")
        elif computer_turn == 'p' and your_turn == 'r':
            print("you lose")
        elif computer_turn == 'p' and your_turn == 'p':
            print("There is Tie")  
        
        if computer_turn == 's' and your_turn == 'r':
            print("You win")
        elif computer_turn == 's' and your_turn == 'p':
            print("you lose")
        elif computer_turn == 's' and your_turn == 's':
            print("There is Tie") 
        rpc.decision_of_game()    
    def decision_of_game(self):
        print("if you want to play again write 'p' and for quit the game write 'q':")  
        decide = input("play again or quit:")
        if decide.lower() == 'p':
            rpc.play_game()
        else:
            print("Thanks for playing")
        
        
        
            
            
rpc = rock_paper_scissors_Game()
rpc.play_game()
#rpc.decision_of_game()

