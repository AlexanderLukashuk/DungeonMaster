class Item:
    def __init__(self, name: str, description: str, price: int):
        self.name = name
        self.description = description
        self.price = price
    
    def can_use(self, player) -> bool:
        return False
    
    def use(self, player):
        raise NotImplementedError
