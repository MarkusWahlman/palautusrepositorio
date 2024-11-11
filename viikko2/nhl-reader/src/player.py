class Player:
    def __init__(self, player_data):
        self.name = player_data['name']
        self.nationality = player_data['nationality']
        self.assists = player_data['assists']
        self.goals = player_data['goals']
        self.total_points = self.assists + self.goals
        self.team = player_data['team']
        self.games = player_data['games']
        self.id = player_data['id']
    
    def __str__(self):
            return f"{self.name:<20} {self.team}  {self.goals} + {self.assists} = {self.total_points}"