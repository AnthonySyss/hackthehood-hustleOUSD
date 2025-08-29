# Group:
# Who worked on this class:

import random

class Room:
    """Represents different locations in the your world"""
    
    def __init__(self, name, description):
        """Required attributes, as well as any additional ones"""
        ### YOUR CODE HERE ###
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.npcs = []
        self.visited = False

    
    def describe(self):
        """Display room description and contents (items, NPCs)"""
        if not self.visited:
            print(f"== {self.name} ==")
            print(self.description)
            self.visited = True
        else:
            print(f"You are back in {self.name}.")

        if self.items:
            print("Items here:", ", ".join([item.name for item in self.items]))
        if self.npcs:
            print("You see:", ", ".join([npc.name for npc in self.npcs]))
        if self.exits:
            print("Exits:", ", ".join(self.exits.keys()))  

    
    def add_item(self, item):
        """Add an item to the room"""
        self.items.append(item)

    def remove_item(self, item_name):
        """Remove an item from the room"""
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return item
        return None

    def get_exit(self, direction):
        """Return the room connected in that direction"""
        return self.exits.get(direction, None)

    def add_npc(self, npc):
        """Add an NPC to this room"""
        self.npcs.append(npc)