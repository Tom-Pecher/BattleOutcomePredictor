
import random
from unit import Unit

attackers = [Unit() for _ in range(5)]
defenders = [Unit() for _ in range(5)]

for tick in range(10):

    alive_attackers = [a for a in attackers if a.is_alive()]
    alive_defenders = [d for d in defenders if d.is_alive()]

    print(f"TICK {tick}")
    for a in alive_attackers:
        alive_defenders = [d for d in defenders if d.is_alive()]
        if len(alive_defenders) == 0:
            print("ATTACKERS WIN!")

            for a in attackers:
                print(f"Attackers: {a}")

            for d in defenders:
                print(f"Defenders: {d}")
            quit()
        
        a.attack(random.choice(alive_defenders))

    for d in alive_defenders:
        alive_attackers = [a for a in attackers if a.is_alive()]
        if len(alive_attackers) == 0:
            print("DEFENDERS WIN!")

            for a in attackers:
                print(f"Attackers: {a}")

            for d in defenders:
                print(f"Defenders: {d}")
            quit()

        d.attack(random.choice(alive_attackers))

    for a in attackers:
        print(f"Attackers: {a}")

    for d in defenders:
        print(f"Defenders: {d}")
    print()
