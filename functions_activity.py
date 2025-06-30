menu = {
    "Pizza": 2.99,
    "Burger": 3.99,
    "Hot dog": 1.99,
    "Cheese": 0.59,
    "Ice cream": 1.49,
    "Churro": 0.79,
    "Soda": 0.89
}

def total_price(item1, item2):
    if item1 in menu and item2 in menu:
        total = menu[item1] + menu[item2]
        return f"The total price of {item1} and {item2} is ${total:.2f}"
    else:
        return "One or both items are not on the menu."

print(total_price("Pizza", "Burger"))

def price_difference(item1, item2):
    if item1 in menu and item2 in menu:
        difference = abs(menu[item1] - menu[item2])
        return f"The difference between {item1} and {item2} is ${difference:.2f}"
    else:
        return "One or both items are not on the menu."

print(price_difference("Pizza", "Burger"))

def total_price_multiple(*items):
    total = 0
    missing_items = []
    for item in items:
        if item in menu:
            total += menu[item]
        else:
            missing_items.append(item)
    if missing_items:
        return f"These items are not on the menu: {', '.join(missing_items)}"
    return f"The total price of {', '.join(items)} is ${total:.2f}"

print(total_price_multiple("Pizza", "Cheese", "Soda"))
print(total_price_multiple("Pizza", "Steak", "Hot dog"))

def inflation(item1, multi):
    if item1 in menu:
        menu[item1] = round(menu[item1] * multi, 2)
        return menu 
    else:
        return f"{item1} is not on the menu."

print("Updated menu after inflation:", inflation("Pizza", 1.1))

def deflation(item1, multi):
    if item1 in menu:
        menu[item1] = round(menu[item1] / multi, 2)
        return menu 
    else:
        return f"{item1} is not on the menu."

print("Updated menu after deflation:", deflation("Pizza", 1.1))

def items_with_99_cents():
    result = []
    for item, price in menu.items():
        price_str = f"{price:.2f}"
        if price_str.endswith(".99"):
            result.append(item)
    return result

print("Items with 99 cents:", items_with_99_cents())