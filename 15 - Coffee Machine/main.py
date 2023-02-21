MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_on = True

def get_report():
    """Reports the remaining resources in the coffee machine and profits made."""
    print("Resources report: ")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${profit:.2f}")

def is_resource_sufficient(order_ingredients):
    """Return False if there is not enough resources to make drinnk, True if there is."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True
        
def process_coins():
    """Returns total amount of currency based off user input."""
    print("Please insert coins:")
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.10
    total += float(input("How many nickels?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return true if money received is greater than drink cost, otherwise return False."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """Reduces resources by order ingredient amount."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

def refill_resources():
    """Refills the coffee machine so it can continue to make coffee."""
    resources["water"] += 300
    resources["milk"] += 200
    resources["coffee"] += 100 
    print("Resources have been refilled! Enjoy your coffee.")

def withdraw_profit():
    global profit
    profit = 0
    print("The coffee machine profits have been transferred to your bank account.")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        get_report()
    elif choice == "refill":
        refill_resources()
    elif choice == "withdraw":
        withdraw_profit()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])