#Task 1 
def cat_greeting():
    print("Cat says meow")
cat_greeting()

#Task 2 
def generate_superhero_power():
    name = "John"
    power = "Flying"
    print(name + power)

#Task 3
def generate_superhero_power1():
    power = "Flying"
    return power
print("generate_superhero_power1")

#Task 4
def generate_superhero_power2(user_name, super_power):
    print(user_name + super_power)
print(generate_superhero_power2("Anthony", "Timestop"))

#Task 5
def cat_greetings_loop():
    for i in range(5):
        print("Meow!")
cat_greetings_loop()

#Task 6
def generate_multiple_powers(list_of_powers):
    for x in list_of_powers:
        print(x)
list_of_powers =  ["Flying","Invisibility", "Super Strength", "Timestop"]
generate_multiple_powers(list_of_powers)