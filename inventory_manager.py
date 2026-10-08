import json
import os
prompt = int(0)
inventory_list={}
def title_display(): #print out title
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
def menu_display(): #print out menu
    print("\n------------MENU------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
def load_inventory(): #load json
    global inventory_list
    # If file doesn't exist or is empty, create it with an empty dictionary {}
    if not os.path.exists("inventory.json") or os.path.getsize("inventory.json") == 0:
        with open("inventory.json", "w") as file:
            json.dump({}, file)
    with open("inventory.json", "r") as file: #open and load json
            try:
                inventory_list = json.load(file) #load json file into inventory_list as dictionary
            except json.JSONDecodeError:
                inventory_list = {}  # Fallback if the file is corrupted
    print("\ninventory.json found.")
    print("Inventory loaded successfully.")

def display_all(): #option 1
    global inventory_list
    print("Current Inventory")
    print("-------------------------------------")
    for item_id, details in inventory_list.items(): #loop and print
        print(
        f"ID: {item_id} | Name: {details['name']} | Price: ${details['price']:.2f} | Stock: {details['stock']}"
        )
    print("-------------------------------------")
    
def add_product(): #option 2
    print("\nAdd New Product")
    while True: #check for duplicate product id when adding new product
        Pid= input("Product ID: ").capitalize()
        if Pid in inventory_list:
            print("Error. Product ID already exists! Choose a different Product ID.")
        else:
            break
    Pname= input("Product Name: ").title()
    while True:
        try: #converts input to float without crashing if it fails by jumping to except block
            Price = float(input("Price: "))
            if Price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            break  # Exit loop if input is valid
        except ValueError: #when input is not numbers
            print("Invalid input! Please enter a valid number.")
    while True:
        try: #converts input to int without crashing if it fails by jumping to except block
            Quantity = int(input("Stock Quantity: "))
            if Quantity < 0:
                print("Stock cannot be negative. Please try again.")
                continue
            break  # Exit loop if input is valid
        except ValueError: #when input is not numbers
            print("Invalid input! Please enter a valid whole number.")
    print("\nProduct added successfully!\n")
    inventory_list[Pid]= {"name": Pname, "price": Price, "stock": Quantity}

def update_stock(): #option 3
    print("\nUpdate Stock")
    while True: #check if product id is in inventory_list
        ProductID= input("Enter Product ID:").capitalize()
        if ProductID in inventory_list: 
            print("\nProduct Found:")
            print(f"Name: {inventory_list[ProductID]['name']}")
            print(f"Current Stock: {inventory_list[ProductID]['stock']}")
            break
        else:
            print("Product ID not found. Try again.")
    while True:
            try: #converts input to int without crashing if it fails by jumping to except block
                stock= int(input("\nNew Stock Quantity:"))
                if stock < 0:
                    print("Stock cannot be negative. Please try again.")
                    continue
                break  # Exit loop if input is valid
            except ValueError: #when input is not numbers
                print("Invalid input! Please enter a valid whole number.")    
    inventory_list[ProductID]["stock"]= stock
    print("\nStock updated successfully!")

def search_product(): #option 4
    while True: #check if product id is in inventory_list
        ProductID= input("Enter Product ID:").capitalize()
        if ProductID in inventory_list: 
            print("\nProduct Found")
            print("-------------------------------------")
            print("ID:", ProductID)
            print(f"Name: {inventory_list[ProductID]['name']}")
            print(f"Price: ${inventory_list[ProductID]['price']:.2f}")
            print(f"Stock: {inventory_list[ProductID]['stock']}")
            print("-------------------------------------")
            break
        else:
            print("Product not found.")
            break

def save_inventory(): #option 5 & 6, save to json and dump the dictionary into it
    with open('inventory.json', 'w') as file:
        json.dump(inventory_list, file, indent=4)
#main
title_display()
load_inventory()
menu_display()
while True: 
    prompt= input("\nEnter Option:")
    if prompt== "1":
       display_all()
    elif prompt== "2":
       add_product()
    elif prompt== "3":
        update_stock()
    elif prompt== "4":
        search_product()
    elif prompt== "5":
        print("\nSaving inventory...")
        save_inventory()
        print("Inventory saved successfully to inventory.json.")
    elif prompt== "6":
        print("Saving Inventory before exit...")
        save_inventory()
        print("Inventory saved successfully.")
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break #exits program
    else:
        print("Invalid Option. Please key in the numbers 1-6.")
