class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.hand = []

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



