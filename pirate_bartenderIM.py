#!/usr/bin/python3

import sys
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

pirate_banter = ["Arrr!", "Avast!", "Shiver me timbers!", "Swab the deck!"]


def get_order(questions, pirate_banter):

    customer_order = {}

    print("Arrr. What'll ye be having?")
    print("{} Enter y for yes, or n for no. Arr. Press ENTER if ye don't care ".format(random.choice(pirate_banter)))

    for drink in questions:
        print(questions[drink])
        choice = input(">> ")
        if choice == '\n':
            break
        if choice.lower().strip() == 'y':
            customer_order[drink] = True    
        elif choice.lower().strip() == 'n':
            customer_order[drink] = False   
        else:
            print("whatever")

    if not customer_order:
        sys.exit()
    return customer_order

def mix_drink(order, ingredients):

    beverage = [] 
    for choice in order:
        if choice in ingredients and order[choice] == True: 
            beverage.append(random.choice(ingredients[choice]))

    if not beverage:
        print("We don't server that drink here. Now be on yer way!")
        sys.exit()
    
    if len(beverage) == 2:
        beverage.insert(1, "and")
    elif len(beverage) >= 3:
        e = len(beverage) - 1
        last_ingredient = beverage.pop(e)
        beverage.append("and")        
        beverage.append(last_ingredient)

    return ' '.join(beverage)

if __name__ == '__main__':
    order = get_order(questions, pirate_banter)
    #mix_drink(order, ingredients)
    print("Here's yer drink, matey.")
    print(mix_drink(order, ingredients))
