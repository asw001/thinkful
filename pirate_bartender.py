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


def get_order(questions):

    for drink in questions:
        print("Do you like {} drinks".format(drink))
        choice = input("Enter y for yes or n for no. Arr. Or the ENTER key if you've had enough. Arr. ")
        
        if choice == '\n':
            break

        if choice.lower().strip() == 'y':
            print("you entered yes")
        elif choice.lower().strip() == 'n':
            print("you entered no")
        else:
            print("whatever")


get_order(questions)