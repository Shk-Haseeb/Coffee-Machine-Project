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

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
    

def is_resource_sufficient(menu_choice):
    for item in menu_choice:
        if menu_choice[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
    

def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transcation_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, menu_choice):
    for item in menu_choice:
        resources[item] -= menu_choice[item]
    print(f"Here is your {drink_name}! ")
        
    
    

is_on = True
profit = 0


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        report()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transcation_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])

