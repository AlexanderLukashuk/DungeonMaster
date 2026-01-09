from models.stats import Stats


class EquipmentSlotrs:
    def __init__(self):
        self.slots = {
            "weapon": None,
            "armor": None,
            "ring": None,
        }
    
    def equip(self, equipment):
        self.slots[equipment.slot] = equipment
    
    def unequip(self, slot):
        self.slots[slot] = None
    
    def total_stats(self) -> Stats:
        total = Stats.zero()
        for item in self.slots.values():
            if item:
                total = total + item.stats_bonus
        return total
