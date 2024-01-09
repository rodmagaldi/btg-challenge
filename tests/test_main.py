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
            json={"player_one_choice": "invalid 1", "player_two_choice": "invalid 2"}
        )
        assert response.status_code == 400
        data = response.get_json()
        assert len(data.get("errors")) == 2

    @pytest.mark.parametrize("player_one_choice, player_two_choice, message, winner", [
        ("rock", "scissors", "Pedra esmaga tesoura.", "rock"),
        ("scissors", "rock", "Pedra esmaga tesoura.", "rock"),
        ("rock", "lizard", "Pedra esmaga lagarto.", "rock"),
        ("lizard", "rock", "Pedra esmaga lagarto.", "rock"),
        ("paper", "rock", "Papel cobre pedra.", "paper"),
        ("rock", "paper", "Papel cobre pedra.", "paper"),
        ("paper", "spock", "Papel refuta Spock.", "paper"),
        ("spock", "paper", "Papel refuta Spock.", "paper"),
        ("scissors", "paper", "Tesoura corta papel.", "scissors"),
        ("paper", "scissors", "Tesoura corta papel.", "scissors"),
        ("scissors", "lizard", "Tesoura decapita lagarto.", "scissors"),
        ("lizard", "scissors", "Tesoura decapita lagarto.", "scissors"),
        ("lizard", "spock", "Lagarto envenena Spock.", "lizard"),
        ("spock", "lizard", "Lagarto envenena Spock.", "lizard"),
        ("lizard", "paper", "Lagarto come papel.", "lizard"),
        ("paper", "lizard", "Lagarto come papel.", "lizard"),
        ("spock", "scissors", "Spock quebra tesoura.", "spock"),
        ("scissors", "spock", "Spock quebra tesoura.", "spock"),
        ("spock", "rock", "Spock vaporiza pedra.", "spock"),
        ("rock", "spock", "Spock vaporiza pedra.", "spock"),
    ])
    def test_outcome(self, player_one_choice, player_two_choice, message, winner):
        """
        Tests all possibble outcomes for players choosing different plays.
        """
        response = self.client.post(
            '/',
            json={"player_one_choice": player_one_choice, "player_two_choice": player_two_choice}
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
            json={"player_one_choice": players_choice, "player_two_choice": players_choice}
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get("message") == "Empate!"
        assert data.get("player_one_choice") == players_choice
        assert data.get("player_two_choice") == players_choice
        assert data.get("winner") == None
