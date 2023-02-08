class Weapon:
    def __init__(self, name, effect, value, cost):
        self.name = name
        self.effect = effect
        self.value = value
        self.cost = cost
    def __repr__(self):
        return (f"{self.name} - a {self.effect} weapon for {self.value} damage")
    
Knife = Weapon ("Knife", "Physical", "10", "10")