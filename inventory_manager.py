import json
import os
inventory = int(0)
taxtotal = 0.0
error = int(0)
prompt = 0
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
    with open("inventory.json", "a"): #creates new file if doesn't exist and opens & close it to make sure
        pass
    print("inventory.json found.")
    print("Inventory loaded successfully.")
def display_all(): #option 1
    global inventory_list
    print("Current Inventory")
    print("-------------------------------------")
    with open("inventory.json", "r") as file: #open and load json
        inventory_list = json.load(file) #load json file into inventory_list as dictionary
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
    print("Add New Product")
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
            print(f"Name:", {inventory_list[ProductID]["name"]})
            print(f"Current Stock: {inventory_list[ProductID]["stock"]}")
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
display_all()
while True: 
    ProductName= input("Enter Product Name:").lower()
    if ProductName== "quit": #quit for ProductName
        generate_report(inventory, error)
        for order in inventory_list: #call function to save list into txt
            num, name, qty = order
            save_inventory(num, name, qty)
        break
    if ProductName in (item.lower() for item in order_list):
        prompt= get_valid_input(input("Enter Quantity:"))
        if prompt== "quit": #quit for quantity
            generate_report(inventory, error)
            for order in inventory_list:
                num, name, qty = order
                save_inventory(num, name, qty)
            break
        if prompt== "error":
            error+=1
            continue
        inventory= process_delivery(inventory, prompt)
        index = [item.lower() for item in order_list].index(ProductName)
        number = order_number[index]
        print("New Order Added:")
        print(number, order_list[index], prompt)
        print("\nOrders successfully saved to orders.txt")
        current_order = [number, order_list[index], prompt]
        inventory_list.append(current_order)
    else:
        print("Invalid Name")
        error+=1
        continue
