import json
import os
from product import Product
from inventory import Inventory

FILENAME = "inventory.json"


def load_inventory(inventory):
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            data = json.load(file)
        for item in data:
            product = Product(item["product_id"], item["name"],
                              item["price"], item["stock"])
            inventory.add_product(product)
    else:
        # No file yet, so start with some default products
        inventory.add_product(Product("P001", "Laptop", 1200.00, 14))
        inventory.add_product(Product("P002", "Mouse", 25.50, 40))
        inventory.add_product(Product("P003", "Keyboard", 45.00, 25))


def save_inventory(inventory):
    with open(FILENAME, "w") as file:
        json.dump(inventory.get_products_as_dicts(), file, indent=4)


def show_menu():
    print("""
----------- MENU -----------
1. Display All Products
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit
----------------------------""")


inventory = Inventory()
load_inventory(inventory)

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.display_all()

    elif choice == "2":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        try:
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
        except ValueError:
            print("Invalid number. Product not added.")
            continue
        product = Product(product_id, name, price, stock)
        if inventory.add_product(product):
            print(f"Product '{name}' added successfully.")

    elif choice == "3":
        name = input("Enter product name to update stock: ")
        product = inventory.search_product(name)
        if product is None:
            print(f"Product '{name}' not found in inventory.")
        else:
            try:
                new_stock = int(input("Enter new stock quantity: "))
            except ValueError:
                print("Invalid number. Stock not changed.")
                continue
            if product.update_stock(new_stock):
                print(f"Stock for '{name}' updated to {new_stock}.")

    elif choice == "4":
        name = input("Enter product name to search: ")
        product = inventory.search_product(name)
        if product is None:
            print(f"Product '{name}' not found in inventory.")
        else:
            product.display_information()

    elif choice == "5":
        save_inventory(inventory)
        print("Inventory saved successfully.")

    elif choice == "6":
        save_inventory(inventory)
        print("Exiting the program. Inventory saved.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
