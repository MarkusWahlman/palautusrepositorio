import requests


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

class PlayerReader:
    def __init__(self, url: str):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=5).json()
        return [Player(player_data) for player_data in response]

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality: str):
        filtered_players = filter(lambda player: player.nationality == nationality, self.players)
        return sorted(filtered_players, key=lambda player: player.total_points, reverse=True)