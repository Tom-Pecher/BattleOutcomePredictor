
class Battle:
    def __init__(self, team1, team2, print_console=True):
        self.team1 = team1
        self.team2 = team2
        self.print_console = print_console

    def __str__(self):
        return f"{self.team1}\n{self.team2}"
    
    def reset_battle(self):
        for team in [self.team1, self.team2]:
            team.reset_team()
    
    def perform_tick(self, attackers, defenders):
        if attackers.perform_turn(defenders):
            if self.print_console:
                print(self)
                print(f"\n{attackers.name.upper()} WIN!")
            return defenders.is_defeated()

    def simulate(self, length=100, reset_all=True):
        if reset_all:
            self.reset_battle()
            
        for tick in range(length):
            if self.print_console:
                print(f"TICK {tick}")

            if self.perform_tick(self.team1, self.team2):
                return 1
            
            if self.perform_tick(self.team2, self.team1):
                return -1
            
            if self.print_console:
                print(self)
                print()

        if self.print_console:
            print("DRAW!")
            print(self)
        return 0
