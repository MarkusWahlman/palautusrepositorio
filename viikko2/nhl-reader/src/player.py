import requests
from typing import List
from rich.console import Console
from rich.table import Table

class Player:
    def __init__(self, player_data):
        self.name = player_data.get('name')
        self.nationality = player_data.get('nationality')
        self.assists = player_data.get('assists')
        self.goals = player_data.get('goals')
        self.total_points = self.assists + self.goals
        self.team = player_data.get('team')
        self.games = player_data.get('games')
        self.id = player_data.get('id')
    
    def __str__(self):
            return f"{self.name:<20} {self.team}  {self.goals} + {self.assists} = {self.total_points}"

class PlayerReader:
    def __init__(self, url: str):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=5).json()
        if "error" in response:
            return []
        return [Player(player_data) for player_data in response]

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality: str):
        filtered_players = filter(lambda player: player.nationality == nationality, self.players)
        return sorted(filtered_players, key=lambda player: player.total_points, reverse=True)

def display_players(players: List[Player], nationality: str, season: str):
    console = Console()
    table = Table(title=f"Top Scorers from {nationality} - NHL Season {season}")

    table.add_column("Player", justify="left", style="cyan", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Games", justify="center", style="green")
    table.add_column("Goals", justify="center", style="yellow")
    table.add_column("Assists", justify="center", style="yellow")
    table.add_column("Total Points", justify="center", style="bold red")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.games),
            str(player.goals),
            str(player.assists),
            str(player.total_points),
        )

    console.print(table)