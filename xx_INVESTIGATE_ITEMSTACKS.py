import random as rd
import collections

# instead of a dict, use a Counter:
inventory = collections.Counter()

items = ["gunk","gear","bolt","wheel","pinion"]
drops = []

while True:
    enter = input("")
    if enter == "":
        drops = []
        quantity = 1
        drops.append([rd.choice(items),quantity])
        print("drops",drops)
        for add_to, quantity in drops:
            # if no value exists in 'inventory' for the key 
            # 'add_to', the value is assumed to be 0.
            inventory[add_to] += quantity

    print("inv", [[x, inventory[x]] for x in inventory])


