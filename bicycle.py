#!/usr/bin/python3


class Bicycle(object):
    def __init__(self, name, weight, cost, purchased):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.purchased = purchased

class BikeShop(object):
    def __init__(self, name, inventory, balance, markup):
        self.name = name
        self.inventory = inventory
        self.balance = balance
        self.markup = markup

    def markup_price(self, bike):
        markup_cost = bike.cost * (1 + self.markup / 100)
        return markup_cost
        
    def sell(self, bike, customer):
        price = self.markup_price(bike)
        self.balance += price
        bike.purchased = True
        customer.money -= price
        customer.owns = True
 
    def show_balance(self):
        return self.balance

class Customer(object):
    def __init__(self, name, money, owns):
        self.name = name
        self.money = money
        self.owns = owns 

    def show_balance(self):
        return self.money
