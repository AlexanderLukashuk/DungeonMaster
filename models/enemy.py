from models.stats import Stats


class Enemy:
    def __init__(self, name: str, stats: Stats):
        self.name = name
        self.stats = stats
        self.current_hp = self.stats.max_health

    def take_damage(self, amount: float):
        reduce_damage = max(0, amount - self.stats.defense)
        self.current_hp = max(0, self.current_hp - reduce_damage)

    def is_alive(self) -> bool:
        return self.current_hp > 0
    
    def __repr__(self):
        return f"<Enemy {self.name} HP={self.current_hp}/{self.stats.max_health}>"