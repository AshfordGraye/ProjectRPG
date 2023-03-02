from x_AbilityList import *

class Weapon:
    def __init__(self, name, effect, damage, special):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.special = special
    def __repr__(self):
        if self.special == "":
            return (f"{self.name} - {self.effect} weapon for {self.damage} points.")
        else:
            return (f"{self.name} - {self.effect} weapon for {self.damage} points. Gives abiility: {self.special.name} for {self.special.cost} AP cost.")
        


BareKnuckles = Weapon ("Bare Knuckles", "Physical", 10, StrongFist)
Knife = Weapon ("Knife", "Physical", 15, KnifeCuts)
PowerFist = Weapon ("PowerFist", "Armatek", 18, StrongFist)