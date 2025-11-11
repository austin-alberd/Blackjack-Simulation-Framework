#The driver/test file for the simulation

from Lib.blackjack import Blackjack
from Lib.player import Player

#Game Log
game_log =[]


#Initial Game Stuff
game = Blackjack()
game.setup_game()

#Add players
game.add_player(Player(name="player", strategy = {"soft_hit": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}))
game.add_player(Player(name="dealer",strategy = {"soft_hit": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}))

#get the results
result = game.run_game()
winners,loosers,pushers = game.determine_winners_and_loosers()

#add things to the game log
player_actions = []
dealer_actions = []

for i, entry in enumerate(result,start=0):
    if entry.player=="player":
        player_actions.append([entry.player,entry.action,entry.result,entry.hand,entry.soft_total,entry.hard_total,entry.game_ending_flag])
    elif entry.player == "dealer":




