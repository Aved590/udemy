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



def show_ingredients():
    print(f"Water: {menu['water']}ml")
    print(f"Milk: {menu['milk']}ml ")
    print(f"Coffee: {menu['coffee']}g")
    print(f"Money: ${menu}")


def chg_resources(order_ingredients):
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]


def chk_resources(order_ingredients):
    ''' Returns true if order can be made, false if not'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def accept_coins():
    '''Returns total calculated from coins inserted'''
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .1
    total += int(input("How many nickles?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total



def show_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml ")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")



is_on = True

while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        show_resources()
    else:
        drink = MENU[choice]
        if chk_resources(drink["ingredients"]):
            payment = accept_coins()
            if payment < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif payment < drink["cost"]:
                profit += payment
                chg_resources(drink["ingredients"])
                print("Enjoy your drink")
            else:
                profit += payment
                chg_resources(drink["ingredients"])
                print(f"Here is ${payment - drink['cost']} dollars in change.")
                print("Enjoy your drink")






    elif choice == "espresso":
        drink = MENU[choice]
        print(drink)
        if chk_resources(drink["ingredients"]):
            print("There are enough resources")
        else:
            print("Not enough resources")



    elif choice == "latte":


    elif choice == "cappuccino":
        drink = MENU[choice]
        print(drink)
        if chk_resources(drink["ingredients"]):
            print("There are enough resources")
        else:
            print("Not enough resources")
  

    else:
        print("Invalid choice, try again")
