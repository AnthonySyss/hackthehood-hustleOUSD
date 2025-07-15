# Task 1
continue_checking = "yes"

while continue_checking == "yes":
    age = int(input("Enter the person's age: "))
    if age >= 18:
        print("They are eligible to vote!")
    else:
        print("They are NOT eligible to vote.")
    continue_checking = input("Do you want to check another age? (yes/no): ").lower()

# Task 2
numbers = [1, 2, 3, 4, 10, 24]

for num in numbers:
    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print(f"{num} is zero.")

# Task 3
inventory = ["coal", "dirt", "diamond", "gravel", "stone"]

for block in inventory:
    print(f"You found {block}.")
    if block == "diamond":
        print("Jackpot!")

# Bonus
while True:
    user_input = input("Enter age or type 'stop' to exit: ").lower()
    if user_input == "stop":
        break
    age = int(user_input)
    if age >= 18:
        print("Eligible to vote.")
    else:
        print("Not eligible to vote.")
