# Group: Alvert + Anthony
# Who worked on this class: Alvert + Anthony

import random

class NPC:
    """Represents non-player characters"""
    
    def __init__(self, name, description):
        """Required attributes, as well as any additional ones"""
        self.name = name
        self.description = description
        self.dialogue = {
            "greeting": f"{self.name} nods at you politely.",
            "quest": f"{self.name} says: 'I might have something for you to do...'",
            "bye": f"{self.name} says: 'Safe travels.'"
        }
        self.inventory = []

    
    def talk(self, topic="greeting"):
        """Return dialogue response based on topic"""
        if topic in self.dialogue:
            print(self.dialogue[topic])
        else:
            print(f"{self.name} has nothing to say about that.")
    
    def give_item(self, item_name):
        """Give an item to the player"""
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                print(f"{self.name} gives you a {item.name}.")
                return item
        print(f"{self.name} doesn't have {item_name}.")
        return None
    
    def describe(self):
        """Return NPC's appearance"""
        print(f"You see {self.name}. {self.description}")

    
    def interact(self):
        """Main method for player-NPC interaction"""
        print(f"You approach {self.name}.")
        self.describe()
        choice = input("Do you want to talk or ask for an item? (talk/item/leave): ").lower()
        
        if choice == "talk":
            topic = input("Choose a topic (greeting/quest/bye): ").lower()
            self.talk(topic)
        elif choice == "item":
            item_name = input("What item do you ask for? ")
            self.give_item(item_name)
        else:
            print(f"You leave {self.name} alone.")
