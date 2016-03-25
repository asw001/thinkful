#!/usr/bin/python3

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


def interogate(questions):
    
    drink_preference = get_drink_pref(questions)
    greeting = "Arr. Welcome. What can I get for ye?"
    query1 = "What sort of drink would you be wantin'?"
    query2 = "Do ye like {} drinks? Enter 'y' for yes and 'n' for no "
    customer_choice = {}
    choice = True
    choice_table = {'y': True, 'n': False}
    
    print(greeting + " " + query1)
    
    while choice:
        for drink in drink_preference:
            choice = input(query2.format(drink))
            if choice.lower() != "y" or choice.lower() != "n":
                print("Arr. 'y' for yes, 'n' for no")
            else:
                customer_choice[drink] = choice_table[choice]
    
    return customer_choice
            

        
    
def get_drink_pref(questions):
    drink_preference = {}
    
    for drink in questions:
        drink_preference[drink] = False
        
    return drink_preference
    
    
interogate(questions)    