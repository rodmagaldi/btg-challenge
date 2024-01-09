"""
Game
"""

from app.strategies import GeneralStrategy

class Game:
    """
    Defines the game to be played according to a selected strategy
    """
    def __init__(self, strategy: GeneralStrategy):
        self.strategy = strategy

    def play_game(self, player_one_choice, player_two_choice):
        return self.strategy.determine_winner(player_one_choice, player_two_choice)
