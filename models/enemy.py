from models.stats import Stats


class Enemy:
    def __init__(self, name: str, stats: Stats, loot_table=None, experience=50):
        self.name = name
        self.current_stats = stats
        self.current_hp = stats.max_health
        self.actions = []
        self.loot_table = loot_table
        self.experience = experience

    def take_damage(self, amount: float):
        # reduce_damage = max(0, amount - self.stats.defense)
        # self.current_hp = max(0, self.current_hp - reduce_damage)
        self.current_hp -= amount
        self.current_hp = max(0, self.current_hp)

    def is_alive(self) -> bool:
        return self.current_hp > 0
    
    def __repr__(self):
        return f"<Enemy {self.name} HP={self.current_hp}/{self.current_stats.max_health}>"
    
    def choose_action(self, target):
        import random
        return random.choice(self.actions)
    
    def drop_loot(self):
        if not self.loot_table:
            return []
        return self.loot_table.roll()
    
    def __str__(self):
        return (f"--- {self.name} (Уровень ) ---\n"
                f"HP: {self.current_hp}/{self.current_stats.max_health}\n"
                # f"MP: {self.current_mana}/{self.current_stats.max_mana}"
                )
