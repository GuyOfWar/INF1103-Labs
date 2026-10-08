import json
import os
inventory = int(0)
taxtotal = 0.0
error = int(0)
prompt = int(0)
x = int(0)
ProductName = 0
ProductID = 0
order_number= ["1001", "1002", "1003", "1004"]
order_list= ["Wireless Mouse", "Keyboard", "USB Cable", "Laptop Stand"]
inventory_list={}
product_data = [ #dictonary of products
    {"id":"P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id":"P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id":"P003", "name": "Keyboard", "price": 45.00, "stock": 25},
    {"id":"P004", "name": "Monitor", "price": 299.99, "stock": 10}
]
def title_display(): #print out title
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
def menu_display():
    print("------------MENU------------")
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
    print("inventory.json found.")
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
    global inventory_list
    Pid= 0
    Pname= 0
    Price= 0
    Quantity= int(0)
    print("\nAdd New Product")
    while True: #check for duplicate product id when adding new product
        Pid= input("Product ID: ").capitalize()
        if Pid in inventory_list:
            print("Error. Product ID already exists! Choose a different Product ID.")
        else:
            break
    Pname= input("Product Name: ").title()
    Price= float(input("Price: "))
    Quantity= int(input("Stock Quantity: "))
    print("\nProduct added successfully!\n")
    inventory_list[Pid]= {"name": Pname, "price": Price, "stock": Quantity}

def update_stock(): #option 3
    global inventory_list
    print("\nUpdate Stock")
    while True: #check if product id is in inventory_list
        ProductID= input("Enter Product ID:").capitalize()
        if ProductID in inventory_list: 
            print("\nProduct Found:")
            print(f"Name: {inventory_list[ProductID]['name']}")
            print(f"Current Stock: {inventory_list[ProductID]['stock']}")
            break
        else:
            print("Product ID not found.Try again")
    inventory_list[ProductID]["stock"]= input("\nNew Stock Quantity:")
    print("\nStock updated successfully!")
#def search_product(): #option 4
def save_inventory(number, name, price, quantity): #option 5, save to json
    with open("inventory.json", "a") as file:
        file.write(f"{number}, {name}, {quantity}\n")
def get_valid_input(stock): #Handles the prompt, handles input validation, returns a valid integer or a "quit" signal
    if stock == "quit":
        return("quit")
    if not stock.isdigit():
        print("Error, pls use whole numbers only")
        return("error")
    stock = int(stock)
    if  stock < 0:
        print("Invalid Number, pls use whole numbers only")
        return("error")
    return(stock)
def process_delivery(current_total, new_value): #Calculates the new total and returns it
    current_total+= new_value
    return(current_total)
def generate_report(total_units, failed_attempts): #print the final summary
    print("Total Number of Units Processed=", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

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
    else:
        print("Invalid Option. Please key in the numbers 1-6.")
