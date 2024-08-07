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
print(menu)
menu.items()

#new_menu={}
# i=1
# for key, value in menu.items():
#     print("\nMenu Headings:",key)
#     print(key,value)
#     new_dict=dict.fromkeys(menu)
#     print(new_dict)
#     new_menu.update({i:key}) # type: ignore
#     i+=1
#print(new_menu)

#Using a counter (i)show the main headings
i=1
menu_main_headings={}
for key,value in menu.items():
    print(f"{i}:{key}")
    menu_main_headings.update({i:key})
    i+=1
#Get user input for menu selection

user_input=int(input("\nWhat would you like to order? Please press the corresponding number from the menu.\n"))
print(user_input)
print(menu_main_headings)

#validate user_input before moving ahead
if menu_main_headings.get(user_input):
    print("hooray")
else:
    print("Please enter a number between 1 and 4")
#### Complete above condition to break out if user enters wrong input multiple times
#Capture the main menu selection in a variable
user_main_menu_selection=menu_main_headings.get(user_input)
#print(user_main_menu_selection)
print(menu.get(user_main_menu_selection))

#capture the sub_menu in a new directory
sub_menu=(menu.get(user_main_menu_selection))
print(type(sub_menu))
print(sub_menu)

#sub_menu keys list

for key in sub_menu:
    print(key)