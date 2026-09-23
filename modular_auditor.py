inventory = int(0)
taxtotal = 0.0
error = 0
def get_valid_input(stock): #Handles the prompt, handles input validation, returns a valid integer or a "quit" signal
    entries= 0
    if stock == "quit":
        return("quit")
    if not stock.isdigit():
        entries += 1
        print("Error, pls use whole numbers only")
        return(entries)
    stock = int(stock)
    if  stock < 0:
        entries += 1
        print("Invalid Number, pls use whole numbers only")
        return(entries)
    return(stock)
def process_delivery(current_total, new_value): #Calculates the new total and returns it
    current_total+= new_value
    return(current_total)
def calculate_tax(amount): #Takes a delivery amount and returns the tax (10% of that specific delivery)
    tax= round(0.1*amount, 2)
    print("Tax amount for current stock:", tax)
    return(tax)
def generate_report(total_units, failed_attempts): #print the final summary
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print("Total Number of Units Processed=", total_units)
while inventory <= 500:
    prompt= get_valid_input(input("Enter Stock quantity:"))
    if prompt== "quit":
        generate_report(inventory, error)
        print("Total Tax Amount:", taxtotal)
        break
    taxtotal+= round(calculate_tax(prompt), 2)
    inventory= process_delivery(inventory, prompt)
if inventory > 500:
    print("Inventory Overloaded!!!")
