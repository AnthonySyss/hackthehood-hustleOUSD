# arena.py

from hero import Hero
from ability import Ability
from armor import Armor

def main():
    # Iron Man's gear
    repulsor = Ability("Repulsor Beam", 70)
    unibeam = Ability("Unibeam", 100)
    nano_armor = Armor("Nano Armor", 60)

    # Captain America (just for fun!)
    shield_throw = Ability("Shield Throw", 50)
    vibranium_shield = Armor("Vibranium Shield", 70)

    # Create heroes
    iron_man = Hero("Iron Man", 250)
    cap = Hero("Captain America", 200)

    # Add abilities
    iron_man.add_ability(repulsor)
    iron_man.add_ability(unibeam)
    cap.add_ability(shield_throw)

    # Add armor
    iron_man.add_armor(nano_armor)
    cap.add_armor(vibranium_shield)

    # Print health
    print(f"{iron_man.name} Health: {iron_man.current_health}")
    print(f"{cap.name} Health: {cap.current_health}")

    # Iron Man attacks
    attack_val = iron_man.sum_of_attacks()
    print(f"{iron_man.name} attacks with {attack_val} total damage")

    # Captain America defends
    defense_val = cap.defend()
    print(f"{cap.name} defends with {defense_val} block")

    # Final health calculation
    final_damage = max(0, attack_val - defense_val)
    cap.current_health -= final_damage
    print(f"{cap.name}'s Health after attack: {cap.current_health}")

    # Winner
    if cap.current_health <= 0:
        print(f"{iron_man.name} wins the battle!")
    else:
        print(f"{cap.name} is still standing!")

    # Random battle
    iron_man.battle(cap)

if __name__ == "__main__":
    main()