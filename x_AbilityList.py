class Ability:
    def __init__(self, name, effect, damage, cost, rounds, chancetomiss):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.cost = cost
        self.rounds = rounds
        self.chancetomiss = chancetomiss

    def __repr__(self):
        return (f'''{self.name} \n   AP: {self.cost}''')

Attack = Ability ("Attack", "Physical", 20, 0, 1, 10)

LimitBreak = Ability ("Limit Break", "Legendary", 10, 0, 1, 0)

Lunge = Ability ("Lunge", "Physical", 10, 0, 1, 10)