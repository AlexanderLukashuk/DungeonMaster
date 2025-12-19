from dataclasses import dataclass

@dataclass
class Stats:
    max_health: int
    max_mana: int
    attack_power: int # ближний бой
    magic_power: int # урон от магии
    defense: int # уменьшение урона
    agility: int # шанс уклониться / скорость атаки в будущем
    luck: int # шанс критического удара, шанс хорошей добычи