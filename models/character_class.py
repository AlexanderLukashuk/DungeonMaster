from dataclasses import dataclass

from models.stats import Stats



@dataclass(frozen=True)
class CharacterClass:
    name: str
    base_stats: Stats

class Warrior(CharacterClass):
    @staticmethod
    def create() -> "Warrior":
        return Warrior(
            name="Warrior",
            base_stats=Stats(120, 30, 15, 2, 8, 4, 2)
        )
    
class Mage(CharacterClass):
    @staticmethod
    def create() -> "Mage":
        return Mage(
            name="Mage",
            base_stats=Stats(70, 120, 3, 18, 3, 3, 4)
        )
