class Item:
    def __init__(self, name, effect, damage, hits, value):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.hits = hits
        self.value = value
    def __repr__(self):
        return (f"{self.name} - {self.effect} effect for {self.damage} points")


Potion = Item ("Potion", "Healing", 30, 1,50)
HiPotion = Item ("HiPotion", "Healing", 60, 1,100)

Grenade = Item ("Grenade", "Physical", 150, 1, 50)