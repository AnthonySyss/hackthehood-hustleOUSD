# ability.py
import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a random value between 0 and max_damage'''
        return random.randint(0, self.max_damage)

# testing
if __name__ == "__main__":
    repulsor = Ability("Repulsor Beam", 70)
    print(repulsor.attack())