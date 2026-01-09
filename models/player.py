from models.character_class import CharacterClass
from models.inventory.equipment_slots import EquipmentSlotrs
from models.inventory.inventory import Inventory
from models.stats import Stats


class Player:
    def __init__(self, nickname, character_class: CharacterClass):
        self.nickname = nickname
        self.character_class = character_class

        self.level = 1
        self.experience = 0

        self.base_stats: Stats = character_class.base_stats
        self.current_stats: Stats = self.base_stats

        self.current_hp = self.current_stats.max_health
        self.current_mana = self.current_stats.max_mana
        
        self.actions = []

        self.inventory = Inventory()
        self.equipment = EquipmentSlotrs()

        self.recalculate_stats()

    def take_damage(self, amount: float):
        # reduce_damage = max(0, amount - self.base_stats.defense)
        # self.current_hp = max(0, self.current_hp - reduce_damage)
        self.current_hp -= amount
        self.current_hp = max(0, self.current_hp)

    def heal(self, amount: float):
        max_hp = self.current_stats.max_health
        self.current_hp = min(self.current_hp + amount, max_hp)
    
    def is_alive(self) -> bool:
        return self.current_hp > 0
    
    def choose_action(self, target):
        print(f"\n--- Ход игрока {self.nickname} ---")
        for i, action in enumerate(self.actions):
            print(f"{i + 1}) {action.name}")
        
        while True:
            try:
                choice = int(input("Выберите действие: ")) - 1
                if 0 <= choice < len(self.actions):
                    return self.actions[choice]
            except ValueError:
                pass
            print("Неверный выбор, попробуйте еще раз.")
    
    def gain_experience(self, amount: float):
        self.experience += amount
        print(f"✨ Получено {amount} опыта!")

        threshold = self.level * 100
        while self.experience >= threshold:
            self.experience -= threshold
            self.level_up()
            threshold = self.level * 100
    
    def level_up(self):
        self.level += 1

        self.base_stats = self.current_stats.multiply(1.2)

        self.recalculate_stats()

        self.current_hp = self.current_stats.max_health
        self.current_mana = self.current_stats.max_mana

        print(f"УРОВЕНЬ ПОВЫШЕН! Теперь вы {self.level} уровня.")
    
    def recalculate_stats(self):
        equipment_bonus = self.equipment.total_stats()
        self.current_stats = self.base_stats + equipment_bonus

        self.current_hp = min(self.current_hp, self.current_stats.max_health)
        self.current_mana = min(self.current_mana, self.current_stats.max_mana)

    def equip_item(self, equipment):
        self.equipment.equip(equipment)
        self.recalculate_stats()
    
    def unequip_item(self, slot: str):
        self.equipment.unequip(slot)
        self.recalculate_stats()
    
    def __str__(self):
        return (
            f"--- {self.nickname} (Уровень {self.level}) ---\n"
            f"HP: {self.current_hp}/{self.current_stats.max_health}\n"
            f"MP: {self.current_mana}/{self.current_stats.max_mana}\n"
            f"ATK: {self.current_stats.attack_power} | "
            f"DEF: {self.current_stats.defense} | "
            f"AGI: {self.current_stats.agility} | "
            f"LUCK: {self.current_stats.luck}"
        )
