class History:
    def __init__(self, player, action, result, hand, soft_total, hard_total):
        self.player = player
        self.action = action
        self.result = result
        self.hand = hand
        self.soft_total = soft_total
        self.hard_total = hard_total
    def __str__(self):
        return f"History entry for {self.player} with action {self.action} and result {self.result}. Soft total: {self.soft_total}. Hard total: {self.hard_total} Hand cards: {self.hand}"
    def __repr__(self):
        return {"player":self.player,"action":self.action,"result":self.result,"soft_total": self.soft_total,"hard_total": self.hard_total,"hand":self.hand}