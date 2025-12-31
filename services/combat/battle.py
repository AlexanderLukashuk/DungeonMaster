class Battle:
    def __init__(self, combat_system, turn_manager):
        self.combat = combat_system
        self.turn_manager = turn_manager

    def start(self, player, enemy):
        while player.is_alive() and enemy.is_alive():
            turn_order = self.turn_manager.determine_order([player, enemy])

            for actor in turn_order:
                if not player.is_alive() or not enemy.is_alive():
                    break
                    
                target = enemy if actor is player else player
                action = actor.choose_action(target)

                self.combat.attack(actor, target, action)
