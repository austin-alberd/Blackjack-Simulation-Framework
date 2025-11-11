#The driver/test file for the simulation

from Lib.blackjack import Blackjack
from Lib.player import Player
import csv
#Game Log
game_log =[]

j = 0
while j<100:
    #Initial Game Stuff
    game = Blackjack(num_decks=6)
    game.setup_game()

    #Add players
    game.add_player(Player(name="player", strategy = {"soft_hit": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}))
    game.add_player(Player(name="dealer",strategy = {"soft_hit": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}))

    while game.get_shoe_size() > 10:
        #get the results
        result = game.run_game()
        winners,loosers,pushers = game.determine_winners_and_loosers()

        #add things to the game log
        player_actions = []
        dealer_actions = []

        for entry in result:
            if entry.player=="player":
                player_actions.append([entry.player,entry.action,entry.result,entry.hand,entry.soft_total,entry.hard_total,entry.game_ending_flag])
            elif entry.player == "dealer":
                dealer_actions.append([entry.player,entry.action,entry.result,entry.hand,entry.soft_total,entry.hard_total,entry.game_ending_flag])

        game_log.append({
            "playerTotal":player_actions[0][4] if "a" in player_actions[0][3] else player_actions[0][5],
            "playerAction":player_actions[1][1],
            "dealerTopCard":dealer_actions[0][3][0],
            "result":"push" if len(pushers)>0 else "lose" if len(loosers)>0 else "win"
        })

    print(game_log)
    print(len(game_log))

    #print it to a CSV

    with open("DataAnalysis/res.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for entry in game_log:
            writer.writerow([entry["playerTotal"],entry["playerAction"],entry["dealerTopCard"],entry["result"]])
    j+=1