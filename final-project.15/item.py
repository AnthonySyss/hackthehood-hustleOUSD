# Group: Alvert + Anthony
# Who worked on this class: Alvert + Anthony

import random

class Item:
    """Represents objects players can interact with"""
    
    def __init__(self, name, description, usable=True, effect=None):
        self.name = name
        self.description = description
        self.usable = usable
        self.effect = effect

    
    def use(self):
        """What happens when the item is used"""
        if self.usable:
            if self.effect:
                print(f"You use the {self.name}. {self.effect}")
            else:
                print(f"You use the {self.name}, but nothing special happens.")
        else:
            print(f"The {self.name} cannot be used right now.")

    
    def examine(self):
        """Detailed description when player examines item"""
        print(f"{self.name}: {self.description}")
        