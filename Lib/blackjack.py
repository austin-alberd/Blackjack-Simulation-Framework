import random
from player import Player

class Blackjack:



    def __init__(self, num_decks = 1,num_players = 1):
        self.numDecks = num_decks
        self.numPlayers = num_players
        self.players = []
        self.decks = []
        self.defaultDeck = ["a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3,4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

    def setup_game(self):
        for i in range(self.numDecks):
            self.decks.extend(self.defaultDeck)
        random.shuffle(self.decks)

    def run_game(self):
        pass


