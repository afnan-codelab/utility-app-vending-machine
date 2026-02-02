# Vending Machine Program
# Developed by: Afnan Mohammed Ahmed Ali
# This program simulates a vending machine using Python

# Dictionary to store vending machine items
items = {
    "A1": {"name": "Coffee", "price": 5.0, "stock": 5, "category": "Hot Drinks"},
    "A2": {"name": "Tea", "price": 4.0, "stock": 5, "category": "Hot Drinks"},
    "B1": {"name": "Chips", "price": 3.0, "stock": 5, "category": "Snacks"},
    "B2": {"name": "Chocolate", "price": 4.0, "stock": 5, "category": "Snacks"}
}

def display_menu():
    print("\n--- VENDING MACHINE MENU ---")
    for code, item in items.items():
        print(f"{code} | {item['name']} | £{item['price']} | Stock: {item['stock']}")
    print("----------------------------")

def suggest_item(selected_item):
    if selected_item["category"] == "Hot Drinks":
        print("Suggestion: Would you like to add Chocolate?")
    elif selected_item["category"] == "Snacks":
        print("Suggestion: A hot drink would go well with this!")

def vending_machine():
    while True:
        display_menu()
        choice = input("Enter item code (or Q to quit): ").upper()

        if choice == "Q":
            print("Thank you for using the vending machine!")
            break

        if choice not in items:
            print("Invalid code. Please try again.")
            continue

        item = items[choice]

        if item["stock"] <= 0:
            print("Sorry, this item is out of stock.")
            continue

        try:
            money = float(input("Insert money (£): "))
        except ValueError:
            print("Invalid amount entered.")
            continue

        if money < item["price"]:
            print("Insufficient funds. Money refunded.")
            continue

        change = round(money - item["price"], 2)
        item["stock"] -= 1

        print(f"{item['name']} has been dispensed.")
        print(f"Your change is £{change}")

        suggest_item(item)

        again = input("Would you like to buy another item? (Y/N): ").upper()
        if again != "Y":
            print("Thank you for your purchase!")
            break

# Run the vending machine
vending_machine()
