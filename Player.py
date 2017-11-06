class Player(object):
    
    def __init__(self):
        self.hand = []
        self.picks = []
        self.pudding_ctr = 0
        self.score = 0

    def __str__(self):
        player_str = 'Hand: '
        player_str += str(self.hand)
        player_str += '\r\n'
        player_str += 'Picks: '
        player_str += str(self.picks)
        player_str += '\r\n'
        player_str += 'Score: '+str(self.score)
        player_str += '\r\n'
        player_str += 'Puddings: '+str(self.pudding_ctr)
        return str(player_str)