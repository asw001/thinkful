#!/usr/bin/python3


class Bicycle(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

class BikeShop(object):
    def __init__(self, name, inventory, balance):
        self.name = name
        self.inventory = inventory
        self.balance = balance

    def sell(self, markup, bike):
        self.markup = markup
        cost = bike.cost
        markup_cost = cost * (1 + markup / 100)
        self.balance += markup_cost 

    def show_balance(self):
        return self.balance

class Customer(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

