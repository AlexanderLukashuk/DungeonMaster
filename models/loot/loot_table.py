from models.loot.loot_item import LootItem


class LootTable:
    def __init__(self, loot_items: list[LootItem]):
        self.loot_items = loot_items
    
    def roll(self):
        dropped_items = []
        for loot_item in self.loot_items:
            dropped_items.extend(loot_item.roll())
        return dropped_items