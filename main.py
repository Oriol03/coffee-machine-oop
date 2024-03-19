from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#declartion of objects
drink=Menu()
coffee=CoffeeMaker()
money=MoneyMachine()

machine_on=True

while machine_on:
    choisir=input(f"What would you like?  {drink.get_items()}  ")
    if choisir=="off":
       machine_on=False
    elif choisir=="report":
        try :
            with open ("report.txt","r") as file :
                r=file.read()
                print(r)
        except FileNotFoundError:
            with open("report.txt","w") as file :
                file.write(f"{coffee.report()}\nMoney: {money.CURRENCY} {money.profit}")
        
        
    elif choisir=="entrance" :
        produit=["water","milk","coffee"]
        for prod in coffee.resources :
            p=int(input(f"How much {prod} "))
            coffee.resources[prod]+=p
        with open("report.txt","w") as file :
            file.write(f"{coffee.report()}\nMoney: {money.CURRENCY} {money.profit}")
    else :
        if drink.find_drink(choisir)[0] :
            item=drink.find_drink(choisir)[1]
            if coffee.is_resource_sufficient(item):
                if money.make_payment(item.cost):
                    coffee.make_coffee(item)
                    with open("report.txt","w") as file :
                        file.write(f"{coffee.report()}\nMoney: {money.CURRENCY} {money.profit}")
                

""" i want to write a code of coffee machine that allows me to records the report in file
(everyday ), for tomorow the file will be initialezed by 0 for all item

so enjoy to developp this programm 

""" 
        
    
    

