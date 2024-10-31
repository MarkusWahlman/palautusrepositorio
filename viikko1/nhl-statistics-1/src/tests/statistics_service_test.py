import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_finds_player(self):
        player = self.stats.search("Semenko")
        self.assertAlmostEqual(player.name, "Semenko")
    
    def test_search_doesnt_find_player(self):
        player = self.stats.search("Lauri2002")
        self.assertAlmostEqual(player, None)

    def test_find_team_players(self):
        players = self.stats.team("EDM")
        player_names = [player.name for player in players]
        self.assertAlmostEqual(player_names, ["Semenko", "Kurri", "Gretzky"])

    def test_find_top(self):
        players = self.stats.top(4)
        player_names = [player.name for player in players]
        print(player_names)
        self.assertAlmostEqual(player_names, ['Gretzky', 'Lemieux', 'Yzerman', 'Kurri'])