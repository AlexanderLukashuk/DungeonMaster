import random


class LootItem:
    def __init__(self, item_factory, chance: float, min_qty=1, max_qty=1):
        self.item_factory = item_factory
        self.chance = chance
        self.min_qty = min_qty
        self.max_qty = max_qty

    def roll(self):
        if random.random() <= self.chance:
            return [
                self.item_factory()
                for _ in range(random.randint(self.min_qty, self.max_qty))
            ]
        return []