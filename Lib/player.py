# The player class. Stores all of the data for the player
class Player:
    def __init__(self, name,strategy):
        if strategy is None:
            strategy ={"soft_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"hard_hit": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],"soft_stand": [17,18,19,20,21],"hard_stand": [17,18,19,20,21]}
        self.name = name
        self.strategy = strategy
        self.hand = []
        self.soft_total = 0
        self.hard_total = 0

    def validate_strategy(self):
        try:
            soft_hit = self.strategy["soft_hit"]
            hard_hit = self.strategy["hard_hit"]
            soft_stand = self.strategy["soft_stand"]
            hard_stand = self.strategy["hard_stand"]
        except:
            raise ValueError("Strategy formatting is invalid")
        for v in soft_hit:
            if v < 0 or v > 21:
                raise ValueError("soft_hit is invalid")
        for v in hard_hit:
            if v < 0 or v > 21:
                raise ValueError("hard_hit is invalid")
        for v in soft_stand:
            if v < 0 or v > 21:
                raise ValueError("soft_stand is invalid")
        for v in hard_stand:
            if v < 0 or v > 21:
                raise ValueError("hard_stand is invalid")

    def add_to_hand(self, card): self.hand.append(card)
    def clear_hand(self):
        self.hand.clear()

    def set_soft_total(self, value):
        self.soft_total = value
    def set_hard_total(self, value):
        self.hard_total = value

    def reset(self):
        self.hand.clear()
        self.hard_total=0
        self.soft_total=0

    def get_hand(self):return self.hand
    def get_soft_total(self):return self.soft_total
    def get_hard_total(self):return self.hard_total
    def get_name(self):return self.name
    def get_strategy(self):return self.strategy


