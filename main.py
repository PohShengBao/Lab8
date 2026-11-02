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