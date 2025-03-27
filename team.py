
import random

class Team:
    n_teams = 0
    def __init__(self, units, name=None, strategy="Target_Least_HP"):
        self.name = f"Team{Team.n_teams}" if name is None else name
        Team.n_teams += 1
        self.units = units
        self.strategy = strategy

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
            
            if self.strategy == "Target_Random":
                unit.attack(random.choice(enemy_team_units))
            elif self.strategy == "Target_Least_HP":
                least_hp_unit = min(enemy_team_units, key=lambda x: x.hp)
                unit.attack(least_hp_unit)
            elif self.strategy == "Target_Most_D":
                most_d_unit = max(enemy_team_units, key=lambda x: x.damage)
                unit.attack(most_d_unit)
            else:
                raise Exception(f"Invalid strategy: {self.strategy}")
        return False
