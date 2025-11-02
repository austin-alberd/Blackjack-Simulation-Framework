#The driver/test file for the simulation

from Lib.blackjack import Blackjack
from Lib.player import Player

game = Blackjack()

game.setup_game()

strategy = {
  "soft_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
  "hard_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
  "soft_stand": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
  "hard_stand": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
}

player = Player(name="player", strategy=strategy)

player.validate_strategy()