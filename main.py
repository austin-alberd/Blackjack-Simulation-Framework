#The driver/test file for the simulation

from Lib.blackjack import Blackjack

game = Blackjack()

game.setup_game()

print(game.shoe)