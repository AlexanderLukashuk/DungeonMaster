from services.combat.modifiers.base import DamageModifier


class DefenceModifier(DamageModifier):
    def apply(self, context):
        reduction = context.defender.current_stats.defence
        context.damage = max(0, context.damage - reduction)