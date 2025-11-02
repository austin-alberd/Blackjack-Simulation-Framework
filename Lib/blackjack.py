import random
from Lib.player import Player
from Lib.history import History

class Blackjack:
    def __init__(self, num_decks = 1,num_players = 2):
        self._numDecks = num_decks
        self._numPlayers = num_players
        self._players = []
        self._shoe = [] # All of the cards. In casino it is technically called a shoe
        self._defaultDeck = ["a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3,4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
        self._history=[]

    def count_cards(self,hand):
        #All of the logic for adding the cards
        hand_type_flag = "err"
        ace_flag = False
        ace_count = 0
        total = 0
        for card in hand:
            if card == "a":
                ace_flag = True
                ace_count += 1
                hand_type_flag = "st"
            elif card != "a":
                total += card
        if ace_flag:
            for i in range(ace_count):
                if total+11 <= 21:
                    total += 11
                else:
                    total += 1
        else:
            hand_type_flag = "ht"
        return hand_type_flag, total


    def setup_game(self):
        #setup_game
        # Sets up the game. Creates the shoe,
        for i in range(self._numDecks):
            self._shoe.extend(self._defaultDeck)
        random.shuffle(self._shoe)

    def run_game(self):
        is_winner = False

        #initial deal
        for player in self._players:
            player.add_to_hand(self._shoe.pop())
            player.add_to_hand(self._shoe.pop())
            self._history.append(History(player.get_name(),"init","init",player.get_hand(),player.get_soft_total(),player.get_hard_total()))
        return self._history

    def add_player(self, player): self._players.append(player)


