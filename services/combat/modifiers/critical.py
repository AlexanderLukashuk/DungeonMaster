import random
from services.combat.modifiers.base import DamageModifier


class CriticalModifier(DamageModifier):
    def apply(self, context):
        chance = context.attacker.current_stats.luck * 0.02
        if random.random() < chance:
            context.damage *= 1.5
            context.is_critical = True