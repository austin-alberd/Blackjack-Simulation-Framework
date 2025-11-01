#The driver/test file for the simulation

from Lib.blackjack import Blackjack
from Lib.player import Player

game = Blackjack()

game.setup_game()

strategy = {
  "soft_hit": [16,17,18],
  "hard_hit": [15,16,17,18],
  "soft_stand": [20,21],
  "hard_stand": [20,21]
}

player = Player(name="player", strategy=strategy)

player.validate_strategy()