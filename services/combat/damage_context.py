class DamageContext:
    def __init__(self, attacker, defender, base_damange: float):
        self.attacker = attacker
        self.defender = defender
        self.base_damage = base_damange
        self.damage = base_damange
        self.is_evaded = False
        self.is_critical = False