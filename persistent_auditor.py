inventory = int(0)
taxtotal = 0.0
error = int(0)
prompt = 0
x = int(0)
ProductName = 0
order_number= ["1001", "1002", "1003", "1004"]
order_list= ["Wireless Mouse", "Keyboard", "USB Cable", "Laptop Stand"]
def load_inventory(): #load txt
    print("Current Orders:\n")
    with open("orders.txt", "r") as file:
        print(file.read())
def save_inventory(): #save to txt
    file = open("orders.txt", "w")
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
print("Available Order List:")
for x in range(4):
    print(order_number[x], order_list[x])
load_inventory()
while ProductName!= "quit" and prompt!= "quit":
    ProductName= input("Enter Product Name:").lower
    if ProductName in (item.lower() for item in order_list):
        prompt= get_valid_input(input("Enter Quantity:"))
        if ProductName== "quit" or prompt== "quit":
            generate_report(inventory, error)
            break
        if prompt== "error":
            error+=1
            continue
        inventory= process_delivery(inventory, prompt)
    else:
        print("Invalid Name")
        error+=1
        continue
