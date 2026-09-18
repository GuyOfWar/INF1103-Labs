delivery= 0
def get_valid_input(stock):
    inventory = int(0)
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

get_valid_input(delivery)
    