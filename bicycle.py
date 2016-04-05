#!/usr/bin/python3

import random

class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.purchased = False

class BikeShop(object):
    def __init__(self, name, inventory, balance):
        self.name = name
        self.inventory = inventory
        self.balance = balance
        self.markup = 20

    def do_inventory(self, inventory):
        self.inventory = inventory
        for bike in inventory:
            bike.cost = self.markup_price(bike)

    def get_customer_choice(self, customer):
        budget = customer.money                 
        customer_choice = []
        for bike in self.inventory:
            if bike.cost <= budget and bike.purchased == False:
                customer_choice.append(bike) 
                print("{0}, you might be interested in the {1} bike".format(customer.name, bike.name))
        return customer_choice
 
    def markup_price(self, bike):
        markup_cost = bike.cost * (1 + self.markup / 100)
        return markup_cost
        
    def sell(self, bike, customer):
        self.balance += bike.cost 
        bike.purchased = True
        customer.money -= bike.cost
        customer.owns = True
 
    def set_markup(self, markup):
        self.markup = markup
 
    def show_balance(self):
        return self.balance

    def show_inventory(self):
        current_inventory = []
        for bike in self.inventory:
            if not bike.purchased:
                current_inventory.append(bike)
        if current_inventory:
            print("We have the following bikes in stock")
            for bike in current_inventory:
                print("{0} for ${1}".format(bike.name, bike.cost))
        else:
            print("We currently have nothing in stock!")

class Customer(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.owns = False

    def choose_bike(self, bikes):
        self.choice = random.choice(bikes)
        return self.choice
        
    def set_owns(self, owns):
        self.owns = owns

    def show_balance(self):
        return self.money

