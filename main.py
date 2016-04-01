#!/usr/bin/python3

from bicycle import *

mountain_bikeSM = Bicycle("Mountain Bike, Small", 40, 300.00)
mountain_bikeLG = Bicycle("Mountain Bike, Large", 60, 500.00)
city_bikeSM = Bicycle("City Bike, Small", 30, 499.00)
city_bikeLG = Bicycle("City Bike, Large", 40, 699.00)
child_bikeSM = Bicycle("Childrens Bike, Small", 25, 150.00)
child_bikeLG = Bicycle("Childrens Bike, Large", 30, 200.00)

customer1 = Customer("Sharon Jones", 1000.00)
customer2 = Customer("Don Draper", 500.00)
customer3 = Customer("Bill Blaskovitch", 200.00)

customers = [customer1, customer2, customer3]

bikes = [mountain_bikeSM, mountain_bikeLG, city_bikeSM, city_bikeLG, child_bikeSM, child_bikeLG] 

shop1 = BikeShop("Amy's Bikes", bikes, 2000.00)

print("We have the following in stock at {}."format(shop.name))

for bike in shop1.inventory:
    print("{0} for {1} dollars".format(bike.name, bike.cost))


for customer in customers:
    for bike in shop1.inventory:
        if bike.cost <= customer.money:
            print("{0}, you can buy the {1} for {2}".format(customer.name, bike.name, bike.cost))

    


