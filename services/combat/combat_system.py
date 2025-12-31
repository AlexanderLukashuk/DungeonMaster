from models.enemy import Enemy
from models.player import Player
from services.combat.actions.base_actions import Action
from services.combat.damage_context import DamageContext


class CombatSystem:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def attack(self, attacker, defender, action):
        base_damage = action.calculate_damage(attacker)
        context = DamageContext(attacker, defender, base_damage)

        self.pipeline.process(context)

        defender.take_damage(context.damage)
        return context
