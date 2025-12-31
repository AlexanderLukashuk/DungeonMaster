from services.combat.actions.base_actions import Action


class PhysicalAttack(Action):
    def __init__(self, name: str, multiplier: float):
        self.name = name
        self.multiplier = multiplier

    def calculate_damage(self, attacker) -> float:
        return attacker.current_stats.attack_power * self.multiplier