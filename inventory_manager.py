import json
inventory = int(0)
taxtotal = 0.0
error = int(0)
prompt = 0
x = int(0)
ProductName = 0
order_number= ["1001", "1002", "1003", "1004"]
order_list= ["Wireless Mouse", "Keyboard", "USB Cable", "Laptop Stand"]
inventory_list=[]
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
    print("Current Inventory")
    print("-------------------------------------")
    with open("inventory.json", "r") as file: #open and load json
        inventory = json.load(file)
    for item_id, details in inventory.items(): #loop and print
        print(
        f"ID: {item_id} | Name: {details['name']} | Price: ${details['price']:.2f} | Stock: {details['stock']}"
        )
    print("-------------------------------------")

#def add_product(): #option 2
#def update_stock(): #option 3
#def search_product(): #option 4
def save_inventory(number, name, quantity): #option 5, save to json
    with open("orders.txt", "a") as file:
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
