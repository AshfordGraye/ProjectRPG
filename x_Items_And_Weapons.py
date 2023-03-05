from x_Attacks_And_Abilities import *


class Item:
    def __init__(self, name, effect, damage, hits, value):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.hits = hits
        self.value = value
    def __repr__(self):
        return (f"{self.name} - {self.effect} effect for {self.damage} points")

# DEFENSIVE / BUFFS

Potion = Item ("Potion", "Healing", 30, 1,50)
HiPotion = Item ("HiPotion", "Healing", 60, 1,100)

# OFFENSIVE / DEBUFFS

Grenade = Item ("Grenade", "Physical", 150, 1, 50)


class Weapon:
    def __init__(self, name, effect, damage, special, value):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.special = special
        self.value = value
    def __repr__(self):
        if self.special == "":
            return (f"{self.name} - {self.effect} weapon for {self.damage} points.")
        else:
            return (f"{self.name} - {self.effect} weapon for {self.damage} points. Gives abiility: {self.special.name} for {self.special.apcost} AP cost.")

BareKnuckles = Weapon ("Bare Knuckles", "Physical", 10, StrongFist, 0)
Knife = Weapon ("Knife", "Physical", 15, KnifeCuts, 50)

class Armatek:
    def __init__(self, name, effect, damage, special, value):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.special = special
        self.value = value
    def __repr__(self):
        if self.special == "":
            return (f"{self.name} - {self.effect} weapon for {self.damage} points.")
        else:
            return (f"{self.name} - {self.effect} weapon for {self.damage} points. Gives abiility: {self.special.name} for {self.special.apcost} AP cost.")
        
ScanningGlove = Armatek ("Scanning Glove", "Armatek", 0, Scan, 100)
ArmaGauntlet = Armatek ("Mecha Gauntlet", "Armatek", 18, StrongFist, 50)