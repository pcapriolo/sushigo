#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the main file for running a simulation of a game
@author: Paul Capriolo
"""
from Game import Game

def main():

    num_players = 2    
    game = Game(num_players)
    
    while (game.round < 3):
        game.round += 1
        game.deal_cards()
        
        for x in range(0,game.starting_hand_size):
            game.pick()

        print("Calulating Round "+str(game.round)+" Results")        
        game.score_round()
        print(game)
        game.end_round()

    ''' 
    Generate all possible hands and score them.
    '''
    '''tree = Tree(game.deck,num_players)'''

if __name__ == '__main__':
    main()
