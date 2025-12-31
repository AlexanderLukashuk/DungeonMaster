from models.character_class import CharacterClass


class Player:
    def __init__(self, nickname, character_class: CharacterClass):
        self.nickname = nickname
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.base_stats = character_class.base_stats
        self.current_stats = self.base_stats # поставил как заглушку на данный момент
        self.current_hp = self.current_stats.max_health
        self.current_mana = self.current_stats.max_mana

    def take_damage(self, amount: float):
        reduce_damage = max(0, amount - self.base_stats.defense)
        self.current_hp = max(0, self.current_hp - reduce_damage)

    def heal(self, amount: float):
        max_hp = self.current_stats.max_health
        self.current_hp = min(self.current_hp + amount, max_hp)
    
    def is_alive(self) -> bool:
        return self.current_hp > 0
