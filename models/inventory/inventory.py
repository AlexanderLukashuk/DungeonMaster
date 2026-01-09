class Inventory:
    def __init__(self, size=20):
        self.items = []
        self.size = size
    
    def add(self, item):
        if len(self.items) >= self.size:
            return False
        self.items.append(item)
        return True
    
    def remove(self, item):
        self.items.remove(item)