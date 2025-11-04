#The driver/test file for the simulation

from Lib.blackjack import Blackjack
from Lib.player import Player

game = Blackjack()
game.setup_game()

#strategy = {"soft_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}


game.add_player(Player(name="player1", strategy = {"soft_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}))
game.add_player(Player(name="dealer",strategy = {"soft_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}))


while game.get_shoe_size() > 10:
    result = game.run_game()
    winners,loosers,pushers = game.determine_winners_and_loosers()