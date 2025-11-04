#The driver/test file for the simulation

from Lib.blackjack import Blackjack
from Lib.player import Player

game = Blackjack()
game.setup_game()

#strategy = {"soft_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}


game.add_player(Player(name="player1", strategy = {"soft_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}))
game.add_player(Player(name="dealer",strategy = {"soft_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}))

result = game.run_game()

for result in result:
    print(result)

print("_____________________________________________________________")
winners,loosers,pushers = game.determine_winners_and_loosers()

print("Looser")
for looser in loosers:
    print(looser)

print("Winner")
for winner in winners:
    print(winner)


print("Push")
for push in pushers:
    print(push)