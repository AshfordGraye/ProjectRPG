class Ability:
    def __init__(self, name, effect, damage, apcost, rounds, chancetomiss):
        self.name = name
        self.effect = effect
        self.damage = damage
        self.apcost = apcost
        self.rounds = rounds
        self.chancetomiss = chancetomiss

    def __repr__(self):
        if self.rounds > 1:
            return (f'''{self.name} - can hit {self.rounds} times.\n   AP: {self.apcost}''')
        else:
            return (f'''{self.name} \n   AP: {self.apcost}''')


ListItems = Ability("Items","Items",0,0,1,0) #THIS ONE JUST PRETENDS TO BE AN ITEM IN ORDER TO TRIGGER A FUNCTION IN COMBAT

#PHYSICAL ATTACKS

Attack = Ability ("Attack", "Physical", 20, 0, 1, 10)

LimitBreak = Ability ("Limit Break", "Legendary", 10, 0, 1, 0)

Lunge = Ability ("Lunge", "Physical", 10, 0, 1, 10)
KnifeCuts = Ability ("Knife Cuts", "Physical", 25, 10, 2, 30)

Punches = Ability ("Punches", "Physical", 15, 15, 3, 30)
StrongFist = Ability ("Strong Fist", "Physical", 30, 5, 1, 10)

#ARMATEK ABILITIES

Scan = Ability ("Scan", "Scan", 0, 5, 1, 0)