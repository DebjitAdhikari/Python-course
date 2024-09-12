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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def make_espresso(source):
    resources["water"]=resources["water"]-source["water"]
    resources["coffee"]=resources["coffee"]-source["coffee"]
def make_coffe(source):
    resources["water"]=resources["water"]-source["water"]
    resources["milk"]=resources["milk"]-source["milk"]
    resources["coffee"]=resources["coffee"]-source["coffee"]
def make_payment(drink,work):
    global profit
    quarters=int(input("How many Quarters do you have ? "))
    dimes=int(input("How many Dimes do you have ? "))
    nickles=int(input("How many Nickles do you have ? "))
    pennies=int(input("How many Pennies do you have ? "))
    amount=QUARTERS*quarters+DIMES*dimes+NICKLES*nickles+PENNIES*pennies
    price=drink["cost"]
    if amount>=price:
        if work=="espresso":
            make_espresso(drink["ingredients"])
        else:
            make_coffe(drink["ingredients"])
        change=amount-price
        change=round(change,2) 
        profit= profit+amount
        print(f"Here is your change {change}$")
        print(f"Enjoy your drink.")
    else:
        print("You don't have enough money.")

def is_sufficient(source,work):
    if work=="espresso":
        if source["water"]<=resources['water'] and source["coffee"]<=resources['coffee']:
            return "yes"
        else:
            print("Resource not enough.")
    else:
        if source["water"]<=resources['water'] and source["coffee"]<=resources['coffee'] and source["milk"]<=resources['milk']:
            return "yes"
        else:
            print("Resources not enough.")
QUARTERS=0.25
DIMES=0.10
NICKLES=0.05
PENNIES=0.01
machine=True
while machine is True:
    work=input("What would you like ? (Espresso/Latte/Cappuccino): ").lower()
    if work=="off":
        machine=False
    elif work=="report":
        print(f"Water:- {resources['water']}ml\nMilk:- {resources['milk']}ml\nCoffe:- {resources['coffee']}gm\nMoney:- {profit}$")
    else:
        drink=MENU[work]
        enough=is_sufficient(drink["ingredients"],work)
        if enough=="yes":
            make_payment(drink,work)

        