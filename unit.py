
class Unit:
    n_units = 0
    def __init__(self, id=None, hp=50, damage=15):
        self.id = Unit.n_units if id is None else id
        Unit.n_units += 1

        self.hp = hp
        self.damage = damage

        self.max_hp = hp
        self.max_damage = damage

    def reset_unit(self):
        self.hp = self.max_hp
        self.damage = self.max_damage

    def attack(self, entity):
        entity.take_damage(self.damage)

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"\nID: {self.id} - ({self.hp}hp/{self.damage}d)" if self.is_alive() else f"\nID: {self.id} - DEAD"
    