from xmlrpc.client import Boolean

from player import Player

class Blackjack:

    defaultDeck = ["a",2,3,4,5,6,7,8,9,10,10,10,"a",2,3,4,5,6,7,8,9,10,10,10,"a",2,3,4,5,6,7,8,9,10,10,10,"a",2,3,4,5,6,7,8,9,10,10,10]

    def __init__(self, num_decks = 1,num_players = 1):
        self.numDecks = num_decks
        self.numPlayers = num_players
        self.players = []
        self.decks = []

    def shuffle_deck(deck):
        pass

    def setup_game(self):
        pass

    def run_game(self):
        pass


