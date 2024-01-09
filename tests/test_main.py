"""
Test suite
"""

import pytest
from app import create_app

class TestGame:
    """
    Tests the endpoint for playing the game in its different variations
    """
    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_invalid_inputs(self):
        response = self.client.post(
            '/',
            json={
                "player_one_choice": "invalid 1",
                "player_two_choice": "invalid 2"
            }
        )
        assert response.status_code == 400
        data = response.get_json()
        assert data.get("error") is not None

    @pytest.mark.parametrize("player_one_choice, player_two_choice, message, winner, strategy", [
        ("rock", "scissors", "Pedra esmaga tesoura.", "rock", None),
        ("scissors", "rock", "Pedra esmaga tesoura.", "rock", None),
        ("rock", "lizard", "Pedra esmaga lagarto.", "rock", None),
        ("lizard", "rock", "Pedra esmaga lagarto.", "rock", None),
        ("paper", "rock", "Papel cobre pedra.", "paper", None),
        ("rock", "paper", "Papel cobre pedra.", "paper", None),
        ("paper", "spock", "Papel refuta Spock.", "paper", None),
        ("spock", "paper", "Papel refuta Spock.", "paper", None),
        ("scissors", "paper", "Tesoura corta papel.", "scissors", None),
        ("paper", "scissors", "Tesoura corta papel.", "scissors", None),
        ("scissors", "lizard", "Tesoura decapita lagarto.", "scissors", None),
        ("lizard", "scissors", "Tesoura decapita lagarto.", "scissors", None),
        ("lizard", "spock", "Lagarto envenena Spock.", "lizard", None),
        ("spock", "lizard", "Lagarto envenena Spock.", "lizard", None),
        ("lizard", "paper", "Lagarto come papel.", "lizard", None),
        ("paper", "lizard", "Lagarto come papel.", "lizard", None),
        ("spock", "scissors", "Spock quebra tesoura.", "spock", None),
        ("scissors", "spock", "Spock quebra tesoura.", "spock", None),
        ("spock", "rock", "Spock vaporiza pedra.", "spock", None),
        ("rock", "spock", "Spock vaporiza pedra.", "spock", None),
        ("rock", "scissors", "Pedra esmaga tesoura.", "rock", "rock-paper-scissors"),
        ("scissors", "rock", "Pedra esmaga tesoura.", "rock", "rock-paper-scissors"),
        ("rock", "paper", "Papel cobre pedra.", "paper", "rock-paper-scissors"),
        ("paper", "rock", "Papel cobre pedra.", "paper", "rock-paper-scissors"),
        ("paper", "scissors", "Tesoura corta papel.", "scissors", "rock-paper-scissors"),
        ("scissors", "paper", "Tesoura corta papel.", "scissors", "rock-paper-scissors"),
    ])
    def test_outcome(self, player_one_choice, player_two_choice, message, winner, strategy):
        """
        Tests all possibble outcomes for players choosing different plays.
        """
        response = self.client.post(
            '/',
            json={
                "player_one_choice": player_one_choice, 
                "player_two_choice": player_two_choice,
                "strategy": strategy
            }
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == message
        assert data.get("player_one_choice") == player_one_choice
        assert data.get("player_two_choice") == player_two_choice
        assert data.get("winner") == winner

    @pytest.mark.parametrize("players_choice", ["rock", "paper", "scissors", "lizard", "spock"])
    def test_ties(self, players_choice):
        """
        Tests all possibble outcomes for players choosing the same play.
        """
        response = self.client.post(
            '/',
            json={
                "player_one_choice": players_choice,
                "player_two_choice": players_choice
            }
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Empate!"
        assert data.get("player_one_choice") == players_choice
        assert data.get("player_two_choice") == players_choice
        assert data.get("winner") == None
