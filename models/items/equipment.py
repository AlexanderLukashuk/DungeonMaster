from models.items.base_item import Item
from models.stats import Stats


class Equipment(Item):
    def __init__(self, name, description, price, stats_bonus: Stats, slot: str):
        super().__init__(name, description, price)
        self.stats_bonus = stats_bonus
        self.slot = slot