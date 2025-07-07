# CRUD Activity - Anthony Su

# crud_activity.py

cookbook = []

def create(recipe):
    cookbook.append(recipe)
    print(recipe, "has been added to the cookbook.")

def read(index):
    if index >= 0 and index < len(cookbook):
        print("Recipe at index", index, "is:", cookbook[index])
    else:
        print("That index does not exist.")

def update(index, recipe):
    if index >= 0 and index < len(cookbook):
        print("Updating", cookbook[index], "to", recipe)
        cookbook[index] = recipe
    else:
        print("That index does not exist.")

def destroy(index):
    if index >= 0 and index < len(cookbook):
        removed = cookbook.pop(index)
        print(removed, "has been removed from the cookbook.")
    else:
        print("That index does not exist.")

def list_all_recipes():
    if len(cookbook) == 0:
        print("The cookbook is empty.")
    else:
        print("Here are all the recipes:")
        for i in range(len(cookbook)):
            print(i, ":", cookbook[i])

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = int(input("Enter the index of the recipe to read: "))
            read(index)
        elif choice == "3":
            index = int(input("Enter the index of the recipe to update: "))
            recipe = input("Enter the new recipe name: ")
            update(index, recipe)
        elif choice == "4":
            index = int(input("Enter the index of the recipe to delete: "))
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()

