import random
from Lib.history import History
class Blackjack:
    def __init__(self, num_decks = 1,num_players = 2):
        self._numDecks = num_decks
        self._numPlayers = num_players
        self._players = []
        self._shoe = [] # All the cards. In casino, it is technically called a shoe
        self._defaultDeck = ["a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3,4, 5, 6, 7, 8, 9, 10, 10, 10, "a", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
        self._history=[]

    def count_cards(self,hand):
        #All the logic for adding the cards
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
        # Sets up the game. Creates the shoe
        for i in range(self._numDecks):
            self._shoe.extend(self._defaultDeck)
        random.shuffle(self._shoe)

    def initial_deal(self):
        for player in self._players:
            player.clear_hand()
            player.add_to_hand(self._shoe.pop())
            player.add_to_hand(self._shoe.pop())

            hand_type_flag, total = self.count_cards(player.get_hand())

            if hand_type_flag == "st":
                player.set_soft_total(total)
            else:
                player.set_hard_total(total)

            self._history.append(History(player.get_name(),"init","init",player.get_hand().copy(),player.get_soft_total(),player.get_hard_total()))

    def play_rounds(self):
        for player in self._players:
            is_bust = False
            is_stand = False
            break_loop = False
            while not is_bust and not is_stand and not break_loop:
                action = "none"
                result = "none"
                if "a" in player.get_hand():
                    total = player.get_soft_total()
                    if total in player.get_strategy()["soft_hit"]:
                        action = "hit"
                        player.add_to_hand(self._shoe.pop())
                        _, total = self.count_cards(player.get_hand())
                        player.set_soft_total(total)
                    elif total in player.get_strategy()["soft_stand"]:
                        action = "stand"
                        is_stand = True
                else:
                    total = player.get_hard_total()
                    if total in player.get_strategy()["hard_hit"]:
                        action = "hit"
                        player.add_to_hand(self._shoe.pop())
                        _, total = self.count_cards(player.get_hand())
                        player.set_hard_total(total)
                    elif total in player.get_strategy()["hard_stand"]:
                        action = "stand"
                        is_stand = True

                #calculate the final stuff
                if "a" in player.get_hand():
                    total = player.get_soft_total()
                else:
                    total = player.get_hard_total()

                if total > 21:
                    is_bust = True
                    result = "bust"
                elif total == 21:
                    break_loop = True
                    result = "blackjack"

                #write this to history
                self._history.append(History(player.get_name(),action, result, player.get_hand().copy(), player.get_soft_total(),player.get_hard_total()))

    def run_game(self):
        self._history.clear()
        self.setup_game()
        self.initial_deal()
        self.play_rounds()
        return self._history

    def add_player(self, player): self._players.append(player)
