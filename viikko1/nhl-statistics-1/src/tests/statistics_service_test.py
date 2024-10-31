import unittest
from statistics_service import SortBy, StatisticsService
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
        self.assertEqual(player_names, ['Gretzky', 'Lemieux', 'Yzerman', 'Kurri'])

    def test_find_top_sort_by_assists(self):
        players = self.stats.top(4, SortBy.ASSISTS)
        player_names = [player.name for player in players]
        self.assertEqual(player_names, ['Gretzky', 'Yzerman', 'Lemieux', 'Kurri'])

    def test_find_top_sort_by_goals(self):
        players = self.stats.top(4, SortBy.GOALS)
        player_names = [player.name for player in players]
        self.assertEqual(player_names, ['Lemieux', 'Yzerman', 'Kurri', 'Gretzky'])