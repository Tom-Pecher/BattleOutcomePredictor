
from unit import Unit
from team import Team
from battle import Battle

# for d in range(700, 800):
#     d = d/100

#     attackers = Team(name="Attackers", units=[Unit(hp=60, damage=15) for _ in range(5)])
#     defenders = Team(name="Defenders", units=[Unit(hp=135, damage=d) for _ in range(5)])
#     b = Battle(attackers, defenders, print_console=False)
#     outcomes = []
#     for _ in range(10000):
#         outcomes.append(b.simulate(length=15, reset_all=True))

#     print(f"{d}: {sum(outcomes)/len(outcomes)}")

D1 = 7.5 - 1e-15

attackers = Team(name="Attackers", units=[Unit(hp=60, damage=15) for _ in range(5)])
defenders = Team(name="Defenders", units=[Unit(hp=135, damage=D1) for _ in range(5)])
b = Battle(attackers, defenders, print_console=False)
outcomes = []
for _ in range(10000):
    outcomes.append(b.simulate(length=15, reset_all=True))

print(f"{D1}: {sum(outcomes)/len(outcomes)}")


D2 = 7.5 - 1e-16

attackers = Team(name="Attackers", units=[Unit(hp=60, damage=15) for _ in range(5)])
defenders = Team(name="Defenders", units=[Unit(hp=135, damage=D2) for _ in range(5)])
b = Battle(attackers, defenders, print_console=False)
outcomes = []
for _ in range(10000):
    outcomes.append(b.simulate(length=15, reset_all=True))

print(f"{D2}: {sum(outcomes)/len(outcomes)}")
