class Shoe:
    """Represents a shoe with country, code, cost and quantity."""
    
    def __init__(self, country, code, product, cost, quantity):
        """Initializing the shoes attributes."""
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)
        
    def get_cost(self):
        """Return the cost of the shoes."""
        return self.cost
    
    def get_quantity(self):
        """Return the quantity of the shoes."""
        return self.quantity
    
    def __str__(self):
        """Return a string representation of the shoe."""
        return (f"Country: {self.country}, Code: {self.code}, "
                f" Product: {self.product}, Cost: {self.cost}, "
                f"Quantity: {self.quantity}")


# List to store shoe objects
shoe_list = []

def read_shoes_data():
    """Read shoes data from a file and create shoe objects."""
    try:
        with open("inventory.txt", "r") as file:
            next(file) # Skip the header line
            for line in file:
                # Read each line and create a shoe object
                data = line.strip().split(",")
                shoe = Shoe(*data)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("The file inventory.txt does not exist.")
    except Exception as e:
        print(f"Error reading the file: {e}")
        

def capture_shoes():
    """Capture new shoe data from the user and add it to the list."""
    country = input("Please enter the country: ")
    code = input("Please enter the shoe code: ")
    product = input("Please enter the product name: ")
    cost = input("Please enter the cost of the shoe: ")
    quantity = input("Please enter the quantity of the shoes: ")
    
    # Create a new shoe object and append it to the shoe list
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

    # Optionally, add the new shoe to the file
    with open("inventory.txt", "a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}\n")
    
    
def view_all():
    """Print the details of all shoes in the shoe list."""
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    """Find the shoe with the lowest quantity and re-stock it."""
    shoe_to_restock = min(shoe_list, key=lambda x: x.get_quantity())
    print(f"The shoe with th lowest quantity is: {shoe_to_restock}")
    
    add_qty = int(input(f"How many {shoe_to_restock.product}s would you"
                    f" like to add? "))
    shoe_to_restock.quantity += add_qty

    # Update the file with new quantity
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
    
    with open("inventory.txt", "w") as file:
        for line in lines:
            data = line.strip().split(",")
            if data[1] == shoe_to_restock.code:
                data[4] = str(shoe_to_restock.quantity)
            file.write(",".join(data) + "\n")


def search_shoe():
    """Search for a shoe by its code and print its details."""
    code = input("Please enter the shoe code to search for: ")
    found_shoes = [shoe for shoe in shoe_list if shoe.code == code]
    
    if found_shoes:
        for shoe in found_shoes:
            print(shoe)
    else:
        print("Shoe with this code not found.")
        

def value_per_item():
    """Calculate and print the total value for each shoe item 
    (cost * quantity)"""
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Total value of {shoe.product}: {value}")
    
    
def highest_qty():
    """Find and print the shoe with the highest quantity in stock."""
    shoe_with_highest_qty = max(shoe_list, key=lambda x: x.get_quantity())
    print(f"The shoe with the highest quantity is:"
          f" {shoe_with_highest_qty}")
    

def menu():
    """"Display a menu for a user to choose an option."""
    while True:
        print("\nShoe Inventory Management")
        print("Please select an option on the options provided below!")
        print("1. Read shoes data from file")
        print("2. Capture new shoe data")
        print("3. View all shoes")
        print("4. Re-stock shoes")
        print("5. Search for a shoe")
        print("6. View value per item")
        print("7. View highest quantity shoe")
        print("8. Exit")
        
        option = input("Please enter your option: ")
        
        if option == "1":
            read_shoes_data()
        elif option == "2":
            capture_shoes()
        elif option == "3":
            view_all()
        elif option == "4":
            re_stock()
        elif option == "5":
            search_shoe()
        elif option == "6":
            value_per_item()
        elif option == "7":
            highest_qty()               
        elif option == "8":
            print("Exiting the program!")
            break
        else:
            print("Invalid choice, please try again.")

# Calling the menu function to start the program
if __name__ == "__main__":
    menu()
    