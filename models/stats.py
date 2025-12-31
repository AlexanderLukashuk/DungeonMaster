from dataclasses import dataclass

@dataclass(frozen=True)
class Stats:
    max_health: float
    max_mana: float
    attack_power: float # ближний бой
    magic_power: float # урон от магии
    defence: float # уменьшение урона
    agility: float # шанс уклониться / скорость атаки в будущем
    luck: float # шанс критического удара, шанс хорошей добычи

    def add(self, other: "Stats") -> "Stats":
        return Stats(
            max_health=self.max_health + other.max_health,
            max_mana=self.max_mana + other.max_mana,
            attack_power=self.attack_power + other.attack_power,
            magic_power=self.magic_power + other.magic_power,
            defence=self.defence + other.defence,
            agility=self.agility + other.agility,
            luck=self.luck + other.luck
        )
    
    def multiply(self, factor: float) -> "Stats":
        return Stats(
            max_health=self.max_health * factor,
            max_mana=self.max_mana * factor,
            attack_power=self.attack_power * factor,
            magic_power=self.magic_power * factor,
            defence=self.defence * factor,
            agility=self.agility * factor,
            luck=self.luck * factor
        )
    
    def __add__(self, other: "Stats") -> "Stats":
        return self.add(other)
    
    def __mul__(self, factor: float) -> "Stats":
        return self.multiply(factor)

    @staticmethod
    def zero() -> "Stats":
        return Stats(
            max_health=0,
            max_mana=0,
            attack_power=0,
            magic_power=0,
            defence=0,
            agility=0,
            luck=0
        )

