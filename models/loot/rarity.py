from enum import Enum


class Rariry(Enum):
    COMMON = ("Commot", 1.0)
    UNCOMMON = ("Uncommon", 1.2)
    RARE = ("Rare", 1.5)
    EPIC = ("EPIC", 2.0)
    LEGENDARY = ("Legendary", 3.0)

    def __init__(self, title: str, stat_multiplier: float):
        self.title = title
        self.stat_multiplier = stat_multiplier