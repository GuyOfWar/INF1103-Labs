inventory = int(0)
delivery= 0
stock= 0
entries = 0
while inventory <= 500:
    stock= input("Enter Stock quantity:")
    if stock == "quit":
        print("Total Number of Units Processed=", inventory)
        print("Number of Failed/Rejected Entries:", entries)
        break
    if not stock.isdigit():
        entries += 1
        print("Error, pls use whole numbers only")
        print("Number of Failed/Rejected Entries:", entries)
        continue
    stock = int(stock)
    if  stock < 0:
        entries += 1
        print("Invalid Number, pls use whole numbers only")
        print("Number of Failed/Rejected Entries:", entries)
    inventory+=stock
    print("Total Number of Units Processed=", inventory)
if inventory > 500:
    print("Inventory Overloaded!!!")
def get_valid_input(stock): #Handles the prompt, handles input validation, and returns a valid integer or a "quit" signal
def process_delivery(current_total, new_value): #Calculates the new total and returns it
def calculate_tax(amount): #Takes a delivery amount and returns the tax (10% of that specific delivery)
def generate_report(total_units, failed_attempts): #print the final summary

#main code
delivery= input("Enter Stock Quantity:")
get_valid_input(delivery)