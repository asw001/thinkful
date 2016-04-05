#!/usr/bin/python3

from bicycle import *

mountain_bikeSM = Bicycle("Mountain Bike, Small", 40, 300.00)
mountain_bikeLG = Bicycle("Mountain Bike, Large", 60, 500.00)
city_bikeSM = Bicycle("City Bike, Small", 30, 499.00)
city_bikeLG = Bicycle("City Bike, Large", 40, 599.00)
child_bikeSM = Bicycle("Childrens Bike, Small", 25, 90.00)
child_bikeLG = Bicycle("Childrens Bike, Large", 30, 200.00)

customer1 = Customer("Sharon Jones", 1000.00)
customer2 = Customer("Don Draper", 500.00)
customer3 = Customer("Bill Blaskovitch", 200.00)

customers = [customer1, customer2, customer3]

bikes = [mountain_bikeSM, mountain_bikeLG, city_bikeSM, city_bikeLG, child_bikeSM, child_bikeLG] 

shop1 = BikeShop("Amy's Bikes", bikes, 2000.00)

shop1.do_inventory(bikes)

for customer in customers:
    shop1.get_customer_choice(customer)

shop1.show_inventory()
