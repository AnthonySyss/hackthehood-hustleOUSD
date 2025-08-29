# Group: Anthony + Alvert
# Who worked on this class: Anthony + Alvert

import random

class Player:
    """Represents the player character."""
        
    def __init__(self, name, starting_room=None):
        """Required attributes, as well as any additional ones"""
        self.name = name
        self.health = 100
        self.inventory = []
        self.current_room = starting_room
        
        
def move(self, direction):
    """Move to a different room"""
    next_room = self.current_room.get_exit(direction)
    if next_room:
        self.current_room = next_room
        return next_room
    else:
        print("You can't go that way.")
        return self.current_room

def take_item(self, item_name):
    """Add an item to inventory"""
    if self.current_room:
        item = self.current_room.remove_item(item_name)
        if item:
            self.inventory.append(item)
            print(f"You picked up {item.name}.")
            return True
    print(f"No {item_name} here.")
    return False
                
    
    def use_item(self, item_name, item_use):
        """Use an item from inventory"""
        if item_name in self.inventory:
            print(f"You used {item_name}. (Effect TBD)")
            self.inventory.remove(item_name)
            return True
        else:
            print(f"You don't have {item_name}.")
            return False


    def examine_inventory(self):
        """Look at what items the player has"""
        if self.inventory:
            print("Inventory:", ", ".join(self.inventory))
        else:
            print("Inventory is empty.")


    def display_status(self):
        """Show the player's current health and inventory"""
        print(f"{self.name}'s Status:")
        print(f"  Health: {self.health}")
        if self.inventory:
            print("  Inventory:", ", ".join(self.inventory))
        else:
            print("  Inventory: empty")