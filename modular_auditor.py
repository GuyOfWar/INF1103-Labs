inventory = int(0)
taxtotal = 0.0
error = int(0)
prompt = 0
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
def calculate_tax(amount): #Takes a delivery amount and returns the tax (10% of that specific delivery)
    tax= round(0.1*amount, 2)
    print("Tax amount for current stock:", tax)
    return(tax)
def generate_report(total_units, failed_attempts): #print the final summary
    print("Total Number of Units Processed=", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
while prompt!= "quit":
    prompt= get_valid_input(input("Enter Stock quantity:"))
    if prompt== "quit":
        generate_report(inventory, error)
        taxtotal = round(taxtotal, 2)
        print("Total Tax Amount:", taxtotal)
        break
    if prompt== "error":
        error+=1
        continue
    taxtotal+= calculate_tax(prompt)
    inventory= process_delivery(inventory, prompt)
