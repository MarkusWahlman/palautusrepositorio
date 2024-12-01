class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.leading_player = None

    def add_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        elif player_name == self.player2_name:
            self.player2_score = self.player2_score + 1
        else:
            print("Invalid player name")

        if self.player1_score > self.player2_score:
            self.leading_player = self.player1_name
        elif self.player2_score > self.player1_score:
            self.leading_player = self.player2_name
        else:
            self.leading_player = None

    def _score_call(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
           return "Forty"


    def get_score(self):
        if not self.leading_player:
            if self.player1_score > 2:
                return "Deuce"
            return self._score_call(self.player1_score)+"-All"

        if self.player1_score < 4 and self.player2_score < 4:
            return self._score_call(self.player1_score) + "-" + self._score_call(self.player2_score)
        
        score_difference = abs(self.player1_score - self. player2_score)
        if score_difference > 1:
            return "Win for " + self.leading_player
        return "Advantage " + self.leading_player
