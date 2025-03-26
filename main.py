
import random
from unit import Unit
from team import Team

attackers = Team([Unit() for _ in range(5)])
defenders = Team([Unit() for _ in range(5)])

for tick in range(10):

    alive_attackers = attackers.get_alive_units()
    alive_defenders = defenders.get_alive_units()

    print(f"TICK {tick}")
    for a in alive_attackers:
        alive_defenders = defenders.get_alive_units()
        
        if defenders.is_defeated():
            print(f"Attackers: {attackers}")
            print(f"Defenders: {defenders}")
            print("ATTACKERS WIN!")
            quit()
        
        a.attack(random.choice(alive_defenders))

    for d in alive_defenders:
        alive_attackers = attackers.get_alive_units()

        if attackers.is_defeated():
            print(f"Attackers: {attackers}")
            print(f"Defenders: {defenders}")
            print("DEFENDERS WIN!")
            quit()

        d.attack(random.choice(alive_attackers))

    print(f"Attackers: {attackers}")
    print(f"Defenders: {defenders}")
    print()

print("DRAW!")
print(f"Attackers: {attackers}")
print(f"Defenders: {defenders}")
