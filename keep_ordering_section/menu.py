import sys
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.\n")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
counter=0

while place_order:
    
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? \n")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: \n")
    #counter for tracking incorrect main menu entries
    #counter=0
    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category=int(menu_category)
            menu_category_name = menu_items[menu_category]
            # Print out the menu category name they selected
            print(f"\nYou selected {menu_category_name}\n")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?\n")
            i = 1
            submenu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        submenu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    submenu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Type menu number: \n")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection=int(menu_selection)
                #4. Check if the menu selection is in the menu items
                if menu_selection in submenu_items.keys():
                    # Store the item name as a variable
                    item_name=submenu_items[menu_selection]
                    print(f"You have selected {item_name["Item name"]}\n")
            
                    # Ask the customer for the quantity of the menu item
                    quantity = input(f'What is the quantity of {item_name["Item name"]} that you would like?')
                    # Check if the customer's input is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity=int(quantity)
                    else:
                         quantity=1
            
                    #Add the item to the order_list
                    #price_float = float("{:.2f}".format(float(price)))
                    order_list.append({"Item name":item_name["Item name"],"Price":float("{:.2f}".format(item_name["Price"])),"Quantity":quantity})
                    #Provide the customer with the latest order status
                    print("Your order list is as below:\n")
                    i=1; Price_total =[]
                    for item in order_list:
                        total_price = item["Quantity"] * item["Price"]
                        rounded_total_price = round(total_price, 2)  # Round to 2 decimal places
                        print(f'{i}:  Item name: {item["Item name"]}\n    Price: ${item["Price"]}\n    Quantity: {item["Quantity"]}')
                        Price_total.append(rounded_total_price)
                        #creating a variable for the price total to print as a float with 2 decimals
                        Price_total_print=float("{:.2f}".format(sum(Price_total)))
                        i += 1
                    print(f"\nYour Total Price is ${Price_total_print}")
                else:
                    print(f"Your sub menu selection is invalid, try again. ")
                    counter+=1
            
            else:
                print(f"Your sub menu selection is {menu_selection} which is an invalid input, try again.")
                counter+=1

                        # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option     
        else:
            print(f"{menu_category} is not a valid selection.")
            #break
            counter+=1
    
    else:
            # Tell the customer they didn't select a menu option
        print(f"{menu_category} is not a digit, please select a valid option.")
        counter+=1
    if counter == 3:
        print(f"You have reached the maximum number of incorrect inputs, the ordering process will terminate now.")
        break
    #Define a list for the valid inputs for any additional ordering!!
    valid_inputs=["y","Y","n","N"]   
    while True:
        #Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        #if the input is part of the valid_inputs list then only the prompt would exit from this while loop
        if keep_ordering in valid_inputs:
            break
    while True:
              
        if keep_ordering.upper() == 'N':   
            #This break statement gets you back to the Main Menu to start adding items to your order
            break 
        # This break statement exits out of the keep ordering loop.
        break    
    #This break statement exits out of the Main Menu Ordering
    if keep_ordering.upper() == 'N':
        break
       #Identify the maximum length of an Item Name string to dynamically adjust the column width
if len(order_list) > 0:
    max_value_length = max(len(str(value)) for item in order_list for value in item.values())
    itemname_spaces=max_value_length+2-len("item name")
    item_col_dashes=('-'*(max_value_length+2))
    #Begin print of the final table
    print("Thank you for your order.\nThis is what we are preparing for you.\n")
    print(f"{item_col_dashes}|-------------|----------|--------")
    print(f"Item name{' ' * itemname_spaces}| Unit Price  | Quantity |   Price")
    print(f"{item_col_dashes}|-------------|----------|--------")
    #To print the quantity total, the qty_total, pre_qty_space, post_qty_space are created
    qty_total=sum(item['Quantity'] for item in order_list)
    #The quantity column len is 10, so based on the total being 10 or lower the number of spaces have to be adjusted
    if qty_total > 9:
        pre_qty_space = ' '*4
        post_qty_space = ' '*4
    else:
        pre_qty_space = ' '*4
        post_qty_space = ' '*5
    #printing out the 4 columns - col1 for Item name, col2 for Unite Price, col3 for Quantity and col4 for Price
    for order in order_list:
        col1 = order["Item name"]
        col2 = order["Price"]
        col3 = order["Quantity"]
        #col4 is the total price column while col2 is unit price column
        col4 = float("{:.2f}".format(col2*col3))
        
        print(f"{col1}{' '*(max_value_length+2-len(str(col1)))}|${' '*(12-len(str(col2)))}{col2}|{' '* 4}{col3}{' '* 5}|${' '*(7-len(str(col4)))}{col4}")

    print(f"{item_col_dashes}|-------------|----------|--------")
    print(f"Total{' '*(max_value_length+2-len(('Total')))}|{' '*13}|{pre_qty_space}{qty_total}{post_qty_space}|${' '*(7-len(str(Price_total_print)))}{Price_total_print}")
    print(f'\nYour Total Price is: ${sum(Price_total):.2f}\n')
    
else:
    print("Exiting order as you did not enter any valid items")