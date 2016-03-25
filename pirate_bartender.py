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


def get_order(questions):
    customer_order = {}
    piratical_exclamations = ["Arrr!", "Avast!", "Shiver me timbers!", "Swab the deck!"]
    print("Arrr. What'll ye be having?")
    for drink in questions:
        print(questions[drink])
        choice = input("{} Enter y for yes, or n for no. Arr. Press ENTER if ye don't care ".format(random.choice(piratical_exclamations)))
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

order = get_order(questions)

def mix_drink(order, ingredients):

    drink = ''  
    beverage = [] 
    for choice in order:
        if choice in ingredients: 
            beverage.append(random.choice(ingredients[choice]))

    for stuff in beverage:
       drink += stuff + " " 
        
    print("Arrr... here's your drink with {}".format(drink))

mix_drink(order, ingredients)
