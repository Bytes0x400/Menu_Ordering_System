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
        print("Row85 first condition of digit passed")
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            print("Passed row 87 if condition of int being in menu_items")
            menu_category=int(menu_category)
            menu_category_name = menu_items[menu_category]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}\n")

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
                if menu_selection in submenu_items.keys():
                    #Check if the menu selection is in the menu items
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
                    order_list.append({"Item name":item_name["Item name"],"Price":float(item_name["Price"]),"Quantity":quantity})
                    #Provide the customer with the latest order status
                    print("Your order list is as below:\n")
                    i=1; Price_total=[]
                    for item in order_list:
                        print(f'{i}:  Item name: {item["Item name"]}\n    Price: {item["Price"]}\n    Quantity:{item["Quantity"]}')
                        Price_total.append({item["Quantity"] * item["Price"]}); print(f'Your Total Price is :{Price_total[-1]}\n')
                        i+=1
                    #while True:
    #     # Ask the customer if they would like to order anything else
    #     keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
    #     print(keep_ordering)
    #     if keep_ordering.upper == 'N':
    #         break
                else:
                    print(f'You selected {menu_selection} which is an invalid input')  
                    #break  

            else:
                print(f"Your selection is {menu_selection} which is an invalid input, try again ")

                        # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option

        
    
            
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
            counter+=1
            if counter == 3:
                print("You have reached the maximum number of incorrect inputs, the ordering process will terminate now (row172)")
                break
    else:
        print(f'{menu_category} is not a valid selection (row 170)')
        #counter to terminate ordering process after 3 wrong inputs    
        counter+=1
        if counter == 3:
            print("You have reached the maximum number of incorrect inputs, the ordering process will terminate now (row 178)")
            break
        # Tell the customer they didn't select a number
            #print("You didn't select a valid number.")

    # 
    #     # 5. Check the customer's input3


                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
