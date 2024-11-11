class Player:
    def __init__(self, player_data):
        self.name = player_data['name']
        self.nationality = player_data['nationality']
        self.assists = player_data['assists']
        self.goals = player_data['goals']
        self.team = player_data['team']
        self.games = player_data['games']
        self.id = player_data['id']
    
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Nationality: {self.nationality}\n"
                f"Team: {self.team}\n"
                f"Games Played: {self.games}\n"
                f"Goals: {self.goals}\n"
                f"Assists: {self.assists}\n"
                f"Player ID: {self.id}")