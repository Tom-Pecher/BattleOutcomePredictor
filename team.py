
import random

class Team:
    n_teams = 0
    def __init__(self, units, name=None):
        self.name = f"Team{Team.n_teams}" if name is None else name
        Team.n_teams += 1
        self.units = units

    def __str__(self):
        return f"{self.name}: {', '.join([str(unit) for unit in self.units])}"
    
    def reset_team(self):
        for unit in self.units:
            unit.reset_unit()
    
    def get_alive_units(self):
        return [unit for unit in self.units if unit.is_alive()]
    
    def is_defeated(self):
        return len(self.get_alive_units()) == 0
    
    def perform_turn(self, enemy_team):
        for unit in self.get_alive_units():
            enemy_team_units = enemy_team.get_alive_units()
            
            if enemy_team.is_defeated():
                return True
            
            unit.attack(random.choice(enemy_team_units))
        return False
