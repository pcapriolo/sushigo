'''
This is the main class that manages the game
'''
from math import floor, ceil
from Deck import Deck
from Player import Player

class Game(object):
    
    '''Create Deck & Players'''
    def __init__(self, num_players):
        self.deck = Deck()
        self.players = []
        self.round = 0
        
        '''Set hand size based on number of players'''
        self.starting_hand_size = 12 - num_players
        
        '''HARDCODING HAND SIZE FOR TESTING'''
        self.starting_hand_size = 5
        
        for x in range(0,num_players):
            self.players.append(Player())
    
    '''Deal a hand'''
    def deal_cards(self):
        
        for x in range(0,self.starting_hand_size) :
            for y in range(0,len(self.players)) :
                self.players[y].hand.append(self.deck.cards.pop(0))

    ''' Dumb pick funciton for now '''
    def pick(self):
        
        for x in range(0,len(self.players)):
            self.players[x].picks.append(self.players[x].hand.pop(0))
            
    ''' Remove picked cards '''
    def end_round(self):
        
         for x in range(0,len(self.players)):
             self.players[x].hand = []
             self.players[x].picks = []   
    
    '''
    We need to calculate the score, lots of rules code in here
    Also depends on other players hand
    '''    
    def score_round(self):
        score= 0;
        
        maki_ctr = []
        for x in range(0,len(self.players)):
            
            ''' 2x Tempura = 5 '''
            self.players[x].score += 5 * floor(self.players[x].picks.count('Tempura') / 2)
        
            ''' 3x Sashimi = 10 '''
            self.players[x].score += 10 * floor(self.players[x].picks.count('Sashimi') / 3)
       
            ''' Count Maki '''
            maki_ctr.append(
                    self.players[x].picks.count('Maki 1') + 
                    2 * self.players[x].picks.count('Maki 2') +
                    3 * self.players[x].picks.count('Maki 3'))
        
            ''' Wasabi = 3x Next Nigiri '''
            ''' We hack a -nigiri value because we will sum it later '''
            ''' create loop to check for next nigiri, if found add (3+nigiri-nigiri) '''
            hand_len = len(self.players[x].picks)
            y = 0
            while y < len(self.players[x].picks):
                if self.players[x].picks[y] == 'Wasabi':
                    print('hunting for nigiri')
                    print(self.players[x].picks)
                    nigiri_found = 0
                    z = y
                    while nigiri_found == 0 and z < len(self.players[x].picks):
                        if self.players[x].picks[z] == 'Egg Nigiri':
                            self.players[x].score += 3
                            nigiri_found = 1
                            print ("SCORING A WASABI with eggy")
                        elif self.players[x].picks[z] == 'Salmon Nigiri':
                            self.players[x].score += 6
                            nigiri_found = 1
                            print ("SCORING A WASABI with salmon")
                        elif self.players[x].picks[z] == 'Squid Nigiri':
                            self.players[x].score += 9
                            nigiri_found = 1
                            print ("SCORING A WASABI with squid")
        
                        if nigiri_found == 1:
                            self.players[x].picks.pop(z)
                            
                        z += 1
        
                y += 1
                
            ''' Nigiri Scored at Face Value '''
            self.players[x].score += self.players[x].picks.count('Egg Nigiri')
            self.players[x].score += 2 * self.players[x].picks.count('Salmon Nigiri')
            self.players[x].score += 3 * self.players[x].picks.count('Squid Nigiri')

            ''' Dumpling Scored 1x = 1, 2x = 3, 3x = 6, 4x = 10, 5x = 15 '''
            dumpling_ctr = self.players[x].picks.count('Dumpling')
            if dumpling_ctr == 1:
                self.players[x].score += 1
            elif dumpling_ctr == 2:
                self.players[x].score += 3
            elif dumpling_ctr == 3:
                self.players[x].score += 6
            elif dumpling_ctr == 4:
                self.players[x].score += 10
            elif dumpling_ctr > 4:
                self.players[x].score += 15

            '''print ("Total Dumplings = "+str(dumpling_ctr))'''

            ''' Pudding Counted '''
            self.players[x].pudding_ctr += self.players[x].picks.count('Pudding')
        
        
        ''' Score Maki. Most Maki = 6, Second Most = 3 '''
                
        ''' copy maki_ctr, order copy of maki_ctr, 
        see if more than one person has most, find index of players in original
        maki_ctr, assign points '''
        copy_maki_ctr = maki_ctr.copy()
        copy_maki_ctr.sort()
        copy_maki_ctr.reverse()
        '''print ("SORTED MAKI")
        print (copy_maki_ctr)'''
        
        pts_maki_first = 0
        if copy_maki_ctr[0] > 0:
            num_maki_first = copy_maki_ctr.count(copy_maki_ctr[0])
            pts_maki_first = floor(6/num_maki_first)
        
        pts_maki_second = 0
        if copy_maki_ctr[1] > 0 and copy_maki_ctr[0] > copy_maki_ctr[1]:
            num_maki_second = copy_maki_ctr.count(copy_maki_ctr[1])
            pts_maki_second = floor(3/num_maki_second)
        
        for x in range(0,len(maki_ctr)):
            if maki_ctr[x] == copy_maki_ctr[0]:
                self.players[x].score += pts_maki_first
                '''print ("Awarding "+ str(pts_maki_first)+ " to player "+ str(x)+" for most maki")'''
            elif maki_ctr[x] == copy_maki_ctr[1]:
                self.players[x].score += pts_maki_second
                '''print ("Awarding "+ str(pts_maki_second)+ " to player "+ str(x)+" for 2nd most maki")'''

        if self.round == 3:
            '''score pudding'''
            pudding_list = []
            for x in range(0,len(self.players)):
                pudding_list.append(self.players[x].pudding_ctr)
            
            if pudding_list.count(pudding_list[0]) != len(pudding_list):
                pudding_list.sort()
                pts_pudding_last = 0
                if len(self.players) > 2:
                    pts_pudding_last = ceil(-6/pudding_list.count(pudding_list[0]))            

                pudding_list.reverse()
                pts_pudding_first = 0
                if pudding_list[0] > 0:
                    pts_pudding_first = floor(6/pudding_list.count(pudding_list[0]))

                for x in range(0,len(self.players)):
                    if pudding_list[0] == self.players[x].pudding_ctr:
                        self.players[x].score += pts_pudding_first
                        print ("Awarding "+ str(pts_pudding_first)+ " to player "+ str(x)+" for most pudding")
                    elif pudding_list[len(pudding_list)-1] == self.players[x].pudding_ctr:
                        self.players[x].score += pts_pudding_last
                        print ("Awarding "+ str(pts_pudding_last)+ " to player "+ str(x)+" for least pudding")

                
    
    '''For clean printing of game state'''
    def __str__(self):
        game_str = 'We are in round '+ str(self.round) +  ' with '\
                                          + str(len(self.players)) + ' players'
        game_str += "\r\n\r\n"
        
        for x in range(0,len(self.players)):
            game_str += 'Player '+str(x) + '\r\n'
            game_str += str(self.players[x])
            game_str += "\r\n"
        
        '''TODO:  print deck and players as individual function calls'''
        return game_str
