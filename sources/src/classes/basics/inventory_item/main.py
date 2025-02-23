from src.classes import PillarObject

class InventoryItem(PillarObject):
    def __init__(self, data: dict):
        self.object_type = 'item'
        super().__init__(data)
        
        self.description = data.get('description', '')
        self.quantity = data.get('quantity', 1)
        
    def use(self):
        if self.quantity > 0:
            self.quantity -= 1

    def display_info(self):
        print(f"Description: {self.description}")
        print(f"Quantity: {self.quantity}")

    
