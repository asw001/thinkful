#!/usr/bin/python3

from bicycle import *
import random

mountain_bikeSM = Bicycle("Mountain Bike, Small", 40, 300.00, purchased=False)
mountain_bikeLG = Bicycle("Mountain Bike, Large", 60, 500.00, purchased=False)
city_bikeSM = Bicycle("City Bike, Small", 30, 499.00, purchased=False)
city_bikeLG = Bicycle("City Bike, Large", 40, 699.00, purchased=False)
child_bikeSM = Bicycle("Childrens Bike, Small", 25, 150.00, purchased=False)
child_bikeLG = Bicycle("Childrens Bike, Large", 30, 200.00, purchased=False)

customer1 = Customer("Sharon Jones", 1000.00, owns=False)
customer2 = Customer("Don Draper", 500.00, owns=False)
customer3 = Customer("Bill Blaskovitch", 600.00, owns=False)

customers = [customer1, customer2, customer3]

bikes = [mountain_bikeSM, mountain_bikeLG, city_bikeSM, city_bikeLG, child_bikeSM, child_bikeLG] 

shop1 = BikeShop("Amy's Bikes", bikes, 2000.00, 20)


for customer in customers:
    for bike in shop1.inventory:
        bike_cost = shop1.markup_price(bike)
        if bike_cost <= customer.money and bike.purchased == False and customer.owns == False:
            shop1.sell(bike, customer)
            print("{0} you bought {1} for $ {2}. You have $ {3} left over".format(customer.name, bike.name, bike_cost, customer.money))
            print("{0} Profits: {1}".format(shop1.name, shop1.show_balance()))
    for available_bike in shop1.inventory:
        if available_bike.purchased == False:
            print("Bike: {} is available".format(available_bike.name))
