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

#PHYSICAL ATTACKS

Attack = Ability ("Attack", "Physical", 20, 0, 1, 10)

LimitBreak = Ability ("Limit Break", "Legendary", 10, 0, 1, 0)

Punches = Ability ("Punches", "Physical Damage", 30, 15, 3, 25)

StrongFist = Ability ("Strong Fist", "Physical", 30, 5, 1, 5)

Lunge = Ability ("Lunge", "Physical Damage", 30, 5, 1 ,20)
KnifeCuts = Ability ("Knife Cuts", "Physical", 25, 10, 2, 30)

Punches = Ability ("Punches", "Physical", 15, 15, 3, 30)
StrongFist = Ability ("Strong Fist", "Physical", 30, 5, 1, 10)
AnchorStrike = Ability ("Anchor Strike", "Physical", 15, 15, 1, 15)
PistolShot = Ability ("Pistol Shot", "Physical", 40, 20, 1, 10)
VibraSwordSlice = Ability ("VibraSword Slice", "Physical", 40, 20, 1, 10)
VibraSwordSlashes = Ability ("VibraSword Slashes", "Physical", 25, 30, 3, 20)


#ARMATEK ABILITIES

Scan = Ability ("Scan", "Scan", 0, 5, 1, 0)
LoaderFist = Ability ("Loader Fist", "Armatek", 25, 25, 2, 30)
ArmaScopeShot = Ability ("ArmaScope Shot", "Physical", 40, 30, 1, 1)