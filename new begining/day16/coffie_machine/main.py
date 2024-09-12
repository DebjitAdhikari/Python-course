from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
maker=CoffeeMaker()

latte=MenuItem("latte",200,150,24,2.5)
espresso=MenuItem("espresso",50,0,18,1.5)
cappuccino=MenuItem("cappuccino",250,100,24,3.0)
# print(latte.ingredients,espresso.ingredients,cappuccino.ingredients)

s=menu.find_drink("latte")
print(s.name)
maker.report()