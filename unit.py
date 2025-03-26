
class Unit:
    n_units = 0
    def __init__(self, id=None, hp=50, damage=15):
        self.id = Unit.n_units
        Unit.n_units += 1

        self.hp = hp
        self.damage = damage

    def attack(self, entity):
        entity.take_damage(self.damage)

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.hp} - {self.damage}" if self.is_alive() else "DEAD"
    