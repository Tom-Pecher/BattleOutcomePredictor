
from unit import Unit
from team import Team
from battle import Battle

from matplotlib import pyplot as plt

x = []
y = []
for d in range(0, 100+1):
    d = d/10

    attackers = Team(name="Attackers", units=[Unit(hp=60, damage=15) for _ in range(5)], strategy="Random")
    defenders = Team(name="Defenders", units=[Unit(hp=135, damage=d) for _ in range(5)], strategy="Random")
    b = Battle(attackers, defenders, print_console=False)
    outcomes = []
    for _ in range(10000):
        outcomes.append(b.simulate(length=100, reset_all=True))

    x.append(d)
    y.append(sum(outcomes)/len(outcomes))
    print(f"{d}: {sum(outcomes)/len(outcomes)}")


plt.scatter(x, y)
plt.show()

x = []
y = []
for d in range(0, 100+1):
    d = d/10

    attackers = Team(name="Attackers", units=[Unit(hp=60, damage=15) for _ in range(5)])
    defenders = Team(name="Defenders", units=[Unit(hp=135, damage=d) for _ in range(5)])
    b = Battle(attackers, defenders, print_console=False)
    outcomes = []
    for _ in range(10000):
        outcomes.append(b.simulate(length=100, reset_all=True))

    x.append(d)
    y.append(sum(outcomes)/len(outcomes))
    print(f"{d}: {sum(outcomes)/len(outcomes)}")


plt.scatter(x, y)
plt.show()

# D1 = 7.5 - 1e-15

# attackers = Team(name="Attackers", units=[Unit(hp=60, damage=15) for _ in range(5)])
# defenders = Team(name="Defenders", units=[Unit(hp=135, damage=D1) for _ in range(5)])
# b = Battle(attackers, defenders, print_console=False)
# outcomes = []
# for _ in range(10000):
#     outcomes.append(b.simulate(length=15, reset_all=True))

# print(f"{D1}: {sum(outcomes)/len(outcomes)}")


# D2 = 7.5 - 1e-16

# attackers = Team(name="Attackers", units=[Unit(hp=60, damage=15) for _ in range(5)])
# defenders = Team(name="Defenders", units=[Unit(hp=135, damage=D2) for _ in range(5)])
# b = Battle(attackers, defenders, print_console=False)
# outcomes = []
# for _ in range(10000):
#     outcomes.append(b.simulate(length=15, reset_all=True))

# print(f"{D2}: {sum(outcomes)/len(outcomes)}")
