import random
from services.combat.modifiers.base import DamageModifier


class EvasionModifier(DamageModifier):
    def apply(self, context):
        chance = context.defender.current_stats.agility * 0.01
        if random.random() < chance:
            context.damage = 0
            context.is_evaded = True