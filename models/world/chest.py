from models.loot.loot_table import LootTable


class Chest:
    def __init__(self, loot_table: LootTable):
        self.loot_table = loot_table
        self.is_opened = False
    
    def open(self):
        if self.is_opened:
            return []
        
        self.is_opened = True
        return self.loot_table.roll()