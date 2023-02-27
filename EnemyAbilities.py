class EnemyMove:

    def __init__(self, name, effect, damage):
        self.name = name
        self.effect = effect
        self.damage = damage


Lunge = EnemyMove ("Lunge", "SinglePhysical", 10)