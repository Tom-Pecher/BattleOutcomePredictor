
from unit import Unit
from team import Team
from battle import Battle

import random

for _ in range(100):
    attackers = Team(name="Attackers", units=[Unit(hp=random.randint(20, 100), damage=random.randint(5, 30)) for _ in range(5)], strategy="Target_Most_D")
    defenders = Team(name="Defenders", units=[Unit(hp=random.randint(20, 100), damage=random.randint(5, 30)) for _ in range(5)], strategy="Target_Least_HP")

    b = Battle(attackers, defenders, print_console=False)
    print(b.simulate(length=100, reset_all=True))
