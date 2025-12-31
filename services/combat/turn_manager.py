import random


class TurnManager:
    def determine_order(self, entities):
        return sorted(
            entities,
            key=lambda e: e.current_stats.agility + random.random(),
            reverse=True
        )