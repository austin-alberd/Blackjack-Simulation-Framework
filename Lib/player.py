from dataclasses import dataclass


@dataclass
class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.hand = []
