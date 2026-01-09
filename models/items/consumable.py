from models.items.base_item import Item


class Consumable(Item):
    def __init__(self, name, description, price, effect):
        super().__init__(name, description, price)
        self.effect = effect
    
    def can_use(self, player) -> bool:
        return True
    
    def use(self, player):
        self.effect(player)