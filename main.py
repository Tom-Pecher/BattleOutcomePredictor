
from unit import Unit
from team import Team
from battle import Battle

strategies = ["Target_Random", "Target_Least_HP", "Target_Most_D", "Target_Most_D/HP"]

for s1 in strategies:
    for s2 in strategies:
        attackers = Team(name="Attackers", units=[Unit(hp=60, damage=15) for _ in range(5)] + [Unit(hp=100, damage=20)], strategy=s1)
        defenders = Team(name="Defenders", units=[Unit(hp=60, damage=15) for _ in range(4)] + [Unit(hp=100, damage=20) for _ in range(2)], strategy=s2)

        outcomes = []
        for _ in range(10000):
            b = Battle(attackers, defenders, print_console=False)
            outcomes.append(b.simulate(length=100, reset_all=True))
        print(f"{s1} vs {s2}: {sum(outcomes)/len(outcomes)}")
