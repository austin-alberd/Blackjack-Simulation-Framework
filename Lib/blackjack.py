import random
from Lib.history import History
class Blackjack:
    def __init__(self, num_decks = 1):
        self._numDecks = num_decks
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

            self._history.append(History(player.get_name(),"init","init",player.get_hand().copy(),player.get_soft_total(),player.get_hard_total(),False))

    def play_rounds(self):
        for player in self._players:
            is_bust = False
            is_stand = False
            break_loop = False
            game_ending_flag = False
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
                        game_ending_flag = True
                else:
                    total = player.get_hard_total()
                    if total in player.get_strategy()["hard_hit"]:
                        action = "hit"
                        player.add_to_hand(self._shoe.pop())
                        _, total = self.count_cards(player.get_hand())
                        player.set_hard_total(total)
                    elif total in player.get_strategy()["hard_stand"]:
                        action = "stand"
                        game_ending_flag = True
                        is_stand = True

                #calculate the final stuff
                if "a" in player.get_hand():
                    total = player.get_soft_total()
                else:
                    total = player.get_hard_total()

                if total > 21:
                    is_bust = True
                    result = "bust"
                    game_ending_flag = True
                elif total == 21:
                    break_loop = True
                    result = "blackjack"
                    game_ending_flag = True

                #write this to history
                self._history.append(History(player.get_name(),action, result, player.get_hand().copy(), player.get_soft_total(),player.get_hard_total(),game_ending_flag))

    def run_game(self):
        self._history.clear()
        self.initial_deal()
        self.play_rounds()
        return self._history

    def get_end_game(self):
        game_end_states = []
        for entry in self._history:
            if entry.game_ending_flag:
                game_end_states.append(entry)
        return game_end_states

    def determine_winners_and_loosers(self):
        winners = []
        loosers = []
        pushers = []
        dealer = "a"
        end_game_states = self.get_end_game()

        #we must first find the dealer
        for i,entry in enumerate(end_game_states, start=0):
            if entry.player=="dealer":
                dealer = entry
                end_game_states.pop(i)

        #Now we process the win states of the players
        #busted players
        for i, entry in enumerate(end_game_states,start=0):
            if entry.result == "bust":
                loosers.append(entry)
                end_game_states.pop(i)

        #process dealer blackjack
        if dealer.result == "blackjack":
            for i, entry in enumerate(end_game_states,start=0):
                if entry.result == "blackjack":
                    pushers.append(entry)
                    end_game_states.pop(i)
                else:
                    loosers.append(entry)
                    end_game_states.pop(i)

        #process dealer bust
        if dealer.result == "bust":
            for i, entry in enumerate(end_game_states,start=0):
                if entry.result == "bust":
                    loosers.append(entry)
                    end_game_states.pop(i)
                else:
                    winners.append(entry)
                    end_game_states.pop(i)

        #process push and loss for no blackjack or push
        dealer_total=0
        if "a" in dealer.hand:
            dealer_total = dealer.soft_total
        else:
            dealer_total = dealer.hard_total


        if dealer.action =="stand":
            for i, entry in enumerate(end_game_states,start=0):
                player_total = 0
                if "a" in entry.hand:
                    player_total = entry.soft_total
                else:
                    player_total = entry.hard_total

                if player_total > dealer_total:
                    winners.append(entry)
                    end_game_states.pop(i)
                elif player_total < dealer_total:
                    loosers.append(entry)
                    end_game_states.pop(i)
                else:
                    pushers.append(entry)
                    end_game_states.pop(i)

        return winners, loosers, pushers


    #getters
    def get_shoe_size(self): return len(self._shoe)
    def get_player_count(self): return len(self._players)

    def add_player(self, player): self._players.append(player)
