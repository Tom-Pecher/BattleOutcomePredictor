
class Team:
    def __init__(self, units):
        self.units = units

    def __str__(self):
        return f"Team: {', '.join([str(u) for u in self.units])}"
    
    def get_alive_units(self):
        return [u for u in self.units if u.is_alive()]
    
    def is_defeated(self):
        return len(self.get_alive_units()) == 0