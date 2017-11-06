from random import shuffle, choice

class Deck(object):
 
    CARD_DATA = (('Tempura',14),
                 ('Sashimi',14),
                 ('Dumpling',14),
                 ('Maki 1', 6),
                 ('Maki 2', 12),
                 ('Maki 3', 8),
                 ('Salmon Nigiri',10),
                 ('Squid Nigiri',5),
                 ('Egg Nigiri',5),
                 ('Pudding',10),
                 ('Wasabi',6),
                 ('Chopsticks',4))
    
    def __init__(self):
        print ("Initializing Deck")
        self.cards = []
        for x in range(0,len(self.CARD_DATA)):
            self.card_type = self.CARD_DATA[x]
            print (self.card_type)
            
            for y in range(0,self.card_type[1]):
                self.cards.append(self.card_type[0])

        print ("Total cards = "+ str(len(self.cards)))
        shuffle(self.cards)
        print (self.cards)
        print ('\r\n\r\n')
