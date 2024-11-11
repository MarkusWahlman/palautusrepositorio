import requests
from player import Player

def check_player_finnish(player: Player):
    if player.nationality == "FIN":
        return True
    return False

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url, timeout=5).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    finnish_players = filter(check_player_finnish, players)
    sorted_finnish_players = sorted(finnish_players, key=lambda player: player.total_points, reverse=True)

    for player in sorted_finnish_players:
        print(player)

if __name__ == "__main__":
    main()
