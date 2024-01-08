# An ASCII art for the vending machine logo displaying "Easy Snacks"
vending_machine_logo = """
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄    ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄ ▄▄▄▄▄▄▄    
█       █      █       █  █ █  █  █       █  █  █ █      █       █   █ █ █       █   
█    ▄▄▄█  ▄   █  ▄▄▄▄▄█  █▄█  █  █  ▄▄▄▄▄█   █▄█ █  ▄   █       █   █▄█ █  ▄▄▄▄▄█   
█   █▄▄▄█ █▄█  █ █▄▄▄▄▄█       █  █ █▄▄▄▄▄█       █ █▄█  █     ▄▄█      ▄█ █▄▄▄▄▄    
█    ▄▄▄█      █▄▄▄▄▄  █▄     ▄█  █▄▄▄▄▄  █  ▄    █      █    █  █     █▄█▄▄▄▄▄  █   
█   █▄▄▄█  ▄   █▄▄▄▄▄█ █ █   █     ▄▄▄▄▄█ █ █ █   █  ▄   █    █▄▄█    ▄  █▄▄▄▄▄█ █   
█▄▄▄▄▄▄▄█▄█ █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█    █▄▄▄▄▄▄▄█▄█  █▄▄█▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█▄▄▄▄▄▄▄█   
"""
# code to display vending machine logo
print(vending_machine_logo)


# Vending Machine Menu with items, code, price and stock
items = {
    'Drinks': {
        'water': {'code': 'A1', 'price': 1.00, 'stock': 5},
        'Dew': {'code': 'A2', 'price': 1.50, 'stock': 7},
        'coke': {'code': 'A3', 'price': 1.50, 'stock': 7},
        'pepsi': {'code': 'A4', 'price': 1.50, 'stock': 7},
        'fanta': {'code': 'A5', 'price': 1.50, 'stock': 4}
    },
    'Snacks': {
        'lays': {'code': 'B1', 'price': 1.50, 'stock': 6},
        'Doritos': {'code': 'B2', 'price': 1.50, 'stock': 8},
        'Cheetos': {'code': 'B3', 'price': 1.50, 'stock': 3},
        'Takis': {'code': 'B4', 'price': 2.00, 'stock': 3},
        'cheetos': {'code': 'B5', 'price': 1.50, 'stock': 4},
        '7 days-croissant': {'code': 'B6', 'price': 2.00, 'stock': 5}
    },
    'Hot drinks': {
        'Tea': {'code': 'C1', 'price': 1.00, 'stock': 7},
        'Black Tea': {'code': 'C2', 'price': 1.00, 'stock': 7},
        'Coffee': {'code': 'C3', 'price': 2.00, 'stock': 6},
        'Black coffee': {'code': 'C4', 'price': 2.00, 'stock': 6},
        'Hot Chocolate': {'code': 'C5', 'price': 2.50, 'stock': 3},
    }
}

# Function to display the menu
def display_menu():
    print("Welcome to the Vending Machine!")
    print("Menu:")
    for category, products in items.items():
        print(f"\n{category}:")
        for product, info in products.items():
            print(f"{info['code']} - {product} (${info['price']}) [{info['stock']} available]")

# Function to process the user's selection
def select_item():
    code = input("\nEnter the code of the item you want to purchase(Enter 'QUIT' to exit): ")
    return code.upper()

# Function to handle purchase transactions
def purchase_item(code, money_inserted):
    for category, products in items.items():
        for product, info in products.items():
            if code == info['code']:
                if info['stock'] > 0 and money_inserted >= info['price']:
                    info['stock'] -= 1
                    change = money_inserted - info['price']
                    print(f"\nDispensing {product}. Enjoy your {product}!")
                    print(f"Your change: ${change:.2f}")
                    return change
                else:
                    print("Sorry, either item out of stock or insufficient funds.")
                    return money_inserted

# Function to suggest a item based on the user's purchase
def suggest_purchase(code):
    for category, products in items.items():
        for product, info in products.items():
            if code == info['code']:
                suggestion = ''
                if 'Coffee'in product:
                    suggestion = '7 days-croissant'
                elif 'Black coffee' in product:
                    suggestion = '7 days-croissant'
                elif 'Hot Chocolate' in product:
                    suggestion = '7 days-croissant'
                if suggestion:
                    print(f"Based on your purchase, you might also like {suggestion} to go with it.")

# Function to manage vending machine operation
def vending_machine():
    display_menu()
    while True:
        code = select_item()
        if code == 'QUIT':
            break
        elif code in [item['code'] for sublist in items.values() for item in sublist.values()]:
            money_inserted = float(input("Insert money ($): "))
            change = purchase_item(code, money_inserted)
            if change > 0:
                suggest_purchase(code)
        else:
            print("Invalid code. Please try again or type 'QUIT' to exit.")

# Code to run the vending machine
vending_machine()