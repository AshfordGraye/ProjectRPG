class Weapon:
    def __init__(self, name, effect, value, cost):
        self.name = name
        self.effect = effect
        self.value = value
        self.cost = cost
    def __repr__(self):
        return (f"{self.name} - {self.effect} weapon for {self.value} damage")


BareKnuckles = Weapon ("Bare Knuckles", "Physical", "10", "10")
Knife = Weapon ("Knife", "Physical", "10", "0")
PowerFist = Weapon ("PowerFist", "Armatek", "10", "10")