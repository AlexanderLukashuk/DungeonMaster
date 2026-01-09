class Merchant:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    
    def sell(self, item, player):
        price = item.price
        if player.gold>= price:
            player.gold -= price
            self.inventory.remove(item)
            player.inventory.add(item)
