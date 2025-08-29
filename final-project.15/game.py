# Group: Anthony + Alvert
# Who worked on this class: Anthony + Alvert

from player import Player
from npc import NPC
from item import Item
from room import Room

import random

class Game:
    def __init__(self, name):
        self.player = Player(name)
        self.current_location = None

    def setup_world(self):
        """Create the game world"""
        town = Room("Town", "Starting Point")
        lab = Room("Lab", "Professor's Lab")
        forest = Room("Forest", "Trees with many pokemon in the area")
        gym = Room("Gym", "Gym Leader Kevin's Arena")
        mountain = Room("Mountain", "Rocky place where Giovanni might be")

        town.exits = {"north": lab, "east": forest}
        lab.exits = {"south": town}
        forest.exits = {"west": town, "north": gym}
        gym.exits = {"south": forest, "east": mountain}
        mountain.exits = {"west": gym}
        
        lab.add_npc(NPC("Prof. Maple", "A wise Pokemon professor."))
        gym.add_npc(NPC("Gym Leader Kevin", "Strong trainer who tests challengers."))
        mountain.add_npc(NPC("Team Rocket", "Villains led by Giovanni."))

        town.add_item(Item("Leftovers", "Restores health each turn."))
        forest.add_item(Item("Focus Sash", "Keeps Pokemon standing with 1 HP."))
        gym.add_item(Item("Life Orb", "Boosts power at a cost of health."))
        mountain.add_item(Item("Assault Vest", "Increases defense."))
        mountain.add_item(Item("Rocky Helmet", "Damages attackers on contact."))

        self.current_location = town

    
    def start_game(self):
        """Initialize the game"""
        print(f"Welcome {self.player.name} to Sunnyvale!")
        print("Type 'help' for a list of commands.")
        self.current_location.describe()

    
    def process_command(self, command):
        words = command.lower().split()
        if not words:
            print("Please type a command.")
            return

        action = words[0]

        # Movement
        if action in ["north", "south", "east", "west"]:
            next_room = self.current_location.get_exit(action)
            if next_room:
                self.current_location = next_room
                self.current_location.describe()
            else:
                print("You can't go that way.")

        # Take items
        elif action == "take" and len(words) > 1:
            item_name = " ".join(words[1:])
            item = self.current_location.remove_item(item_name)
            if item:
                self.player.take_item(item)
            else:
                print(f"No {item_name} here.")

        # Use items
        elif action == "use" and len(words) > 1:
            item_name = " ".join(words[1:])
            self.player.use_item(item_name)

        # Examine
        elif action == "look":
            self.current_location.describe()

        elif action == "examine" and len(words) > 1:
            item_name = " ".join(words[1:])
            for item in self.player.inventory:
                if item.name.lower() == item_name.lower():
                    item.examine()
                    return
            print(f"You don't have {item_name} to examine.")

        # Talk
        elif action == "talk" and len(words) > 1:
            npc_name = " ".join(words[1:])
            for npc in self.current_location.npcs:
                if npc.name.lower() == npc_name.lower():
                    npc.interact()
                    return
            print(f"No {npc_name} here.")

        # Show inventory
        elif action == "inventory":
            self.player.display_status()

        # Show help
        elif action == "help":
            self.show_help()

        # Quit
        elif action == "quit":
            print("Thanks for playing!")
            exit()

        else:
            print("Unknown command. Type 'help' for a list of commands.")


    def show_help(self):
        print("Available commands:")
        print("  north/south/east/west - move between rooms")
        print("  take <item> - pick up an item")
        print("  use <item> - use an item from inventory")
        print("  examine <item> - examine an item in your inventory")
        print("  talk <npc> - interact with a character")
        print("  look - examine the current room")
        print("  inventory - show your status and items")
        print("  help - show this help menu")
        print("  quit - exit the game")
    
    def check_victory(self):
        """Check if player has won the game"""
        if self.current_location.name == "Mountain":
            for npc in self.current_location.npcs:
                if npc.name == "Team Rocket" and any(item.name == "Focus Sash" for item in self.player.inventory):
                    print(f"{self.player.name} defeated Team Rocket and saved Sunnyvale!")
                    return True
        return False
    
    def run(self):
        """Main game loop"""
        self.setup_world()
        self.start_game()

        while True:
            command = input("> ")
            self.process_command(command)
            if self.check_victory():
                print("Congratulations! You win!")
                break
                
if __name__ == "__main__":
    name = input("Enter your name: ")
    game = Game(name)
    game.run()