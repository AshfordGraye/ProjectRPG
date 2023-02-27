class Item:
    def __init__(self, name, effect, value, cost):
        self.name = name
        self.effect = effect
        self.value = value
        self.cost = cost
    def __repr__(self):
        return (f"{self.name} - {self.effect} effect for {self.value} points")


Potion = Item ("Potion", "Healing", 30, 50)
HiPotion = Item ("HiPotion", "Healing", 60, 100)