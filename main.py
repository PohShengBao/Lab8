import json
from product import Product
from inventory import Inventory

FILENAME = "inventory.json"


def load_inventory(inventory, filename=FILENAME):
    try:
        with open(filename, "r") as f:
            for item in json.load(f):
                inventory.add_product(Product.from_dict(item))
        print(f"Loaded inventory from {filename}.")
    except FileNotFoundError:
        print("No saved inventory found. Starting empty.")
    except (json.JSONDecodeError, KeyError, ValueError):
        print("Inventory file is corrupted. Starting empty.")


def save_inventory(inventory, filename=FILENAME):
    with open(filename, "w") as f:
        json.dump([p.to_dict() for p in inventory.get_products()], f, indent=4)
    print(f"Inventory saved to {filename}.")


def show_menu():
    print("\n=== Inventory Management System ===")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Save inventory")
    print("6. Exit")


def ask_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None


def add_product_ui(inventory):
    product_id = input("Product ID: ").strip()
    name = input("Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        if price < 0:
            raise ValueError
        product = Product(product_id, name, price, stock)
    except ValueError:
        print("Invalid input. Product not added.")
        return
    if inventory.add_product(product):
        print(f"Added {name}.")
    else:
        print(f"A product with ID {product_id} already exists.")


def update_stock_ui(inventory):
    product = inventory.get_product(input("Product ID to update: ").strip())
    if product is None:
        print("Product not found.")
        return
    quantity = ask_int(f"New stock for {product.name} (currently {product.stock}): ")
    if quantity is None:
        print("Please enter a whole number.")
        return
    try:
        product.update_stock(quantity)
        print("Stock updated.")
    except ValueError as e:
        print(e)


def search_ui(inventory):
    results = inventory.search_product(input("Search by ID or name: ").strip())
    if not results:
        print("No matching products.")
    for p in results:
        p.display_information()


def main():
    inventory = Inventory()
    load_inventory(inventory)

    actions = {"1": inventory.display_all,
               "2": lambda: add_product_ui(inventory),
               "3": lambda: update_stock_ui(inventory),
               "4": lambda: search_ui(inventory),
               "5": lambda: save_inventory(inventory)}

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
