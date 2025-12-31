from services.combat.actions import Action


class MagicAttack(Action):
    def __init__(self, name: str, multiplier: float, mana_cost: float):
        self.name = name
        self.multiplier = multiplier
        self.mana_cost = mana_cost
    
    def calculate_damage(self, attacker) -> float:
        attacker.current_mana -= self.mana_cost
        return attacker.current_stats.magic_power * self.multiplier