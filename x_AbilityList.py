class Ability:
    def __init__(self, name, effect, damage, cost, misschance):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.cost = cost
        self.misschance = misschance

    def __repr__(self):
        return (f'''{self.name} \n   AP: {self.cost}''')

Attack = Ability ("Attack", "Physical", 20, 0, 10)

LimitBreak = Ability ("Limit Break", "Legendary", 10, 0, 0)