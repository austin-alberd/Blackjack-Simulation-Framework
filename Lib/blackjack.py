import random
from player import Player

class Blackjack:



    def __init__(self, num_decks = 1,num_players = 2):
        self._numDecks = num_decks
        self._numPlayers = num_players
        self._players = []
        self._shoe = [] # All of the cards. In casino it is technically called a shoe
        self._defaultDeck = ["a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3,4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

    def setup_game(self):
        #setup_game
        # Sets up the game. Creates the shoe,
        for i in range(self._numDecks):
            self._shoe.extend(self._defaultDeck)
        random.shuffle(self._shoe)

    def run_game(self):
        pass


