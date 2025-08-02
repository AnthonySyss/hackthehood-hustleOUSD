# hero.py
import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def sum_of_attacks(self):
        return sum(ability.attack() for ability in self.abilities)

    def defend(self):
        return sum(armor.block() for armor in self.armors)

    def battle(self, opponent):
        winner = random.choice([self.name, opponent.name])
        print(f"The winner is: {winner}")

# test
if __name__ == "__main__":
    iron_man = Hero("Iron Man", 250)
    print(iron_man.name)           # Iron Man
    print(iron_man.current_health) # 250