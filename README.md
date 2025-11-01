# Black-Jack-Simulation-Farmework
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A python program that is built to simulate games of blackjack and export them in various formats.

## Setup


### Setup: Defining The Game
```python
from Lib.blackjack import  Blackjack

game = Blackjack(num_decks=1,num_players=2)
```

This is the basic setup for a game. The passed in arguements are the defaults so `Blackjack()` would work just as good here.
Note: you must add a minimum of 2 players. 1 must be the dealer and any others can be anything.

### Setup: Defining Player Strategies
This is the hardest part of setting up this framework. If a player is not given a strategy they will be given the house strategy by default (Hit on anything lower than 16). Strategies are represented as dictionaries. Here is an example.

```json
{
  "soft_hit": [16,17,18],
  "hard_hit": [15,16,17,18],
  "soft_stand": [20,21],
  "hard_stand": [20,21]
}
```

`soft_hit` and `hard_hit` dictate what you will hit on and are short for soft total hit and hard total hit. `soft_stand` and `hard_stand` dictate when you stand and are short for soft total stand and hard total stand.

### Setup: Creating Players
